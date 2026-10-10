"""Whisper STT lab: prompted/unprompted transcription, chunking and exports.

Adapted from the student's stt.ipynb. Requires: pip install openai pydub python-dotenv
For pydub audio decoding, install ffmpeg.

Example:
    python whisper_transcription.py --audio audio/meeting.wav --prompt "Project names: ..."

The script sends audio to the OpenAI API; API usage may incur charges.
"""

import argparse
import json
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
from pydub import AudioSegment


def get_client():
    load_dotenv()
    key = os.getenv("OPENAI_ADMIN_KEY") or os.getenv("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("Set OPENAI_ADMIN_KEY (or OPENAI_API_KEY) in your local .env file")
    return OpenAI(api_key=key)


def transcribe_file(client, path, prompt=None):
    """Transcribe one audio file and return verbose segment timestamps."""
    with open(path, "rb") as audio:
        args = dict(model="whisper-1", file=audio, response_format="verbose_json",
                    timestamp_granularities=["segment"])
        if prompt:
            args["prompt"] = prompt
        return client.audio.transcriptions.create(**args)


def transcribe_chunked(client, audio_path, chunk_minutes=10, prompt=None, temp_dir=None):
    """Split audio into chunks and shift timestamps to the original audio timeline."""
    from tempfile import TemporaryDirectory

    audio = AudioSegment.from_file(audio_path)
    chunk_ms = int(chunk_minutes * 60 * 1000)
    if chunk_ms <= 0:
        raise ValueError("chunk_minutes must be greater than zero")
    segments = []
    texts = []
    with TemporaryDirectory(dir=temp_dir) as folder:
        for i, start_ms in enumerate(range(0, len(audio), chunk_ms)):
            part = audio[start_ms:start_ms + chunk_ms]
            # Export mp3 for more compact uploads than uncompressed WAV.
            path = Path(folder) / f"chunk_{i:03d}.mp3"
            part.export(path, format="mp3", bitrate="64k")
            if path.stat().st_size > 25 * 1024 * 1024:
                raise ValueError(f"Chunk {i} exceeds 25 MB; reduce --chunk-minutes")
            result = transcribe_file(client, path, prompt=prompt)
            texts.append(result.text)
            offset = start_ms / 1000.0
            for seg in (result.segments or []):
                segments.append({"start": round(float(seg.start) + offset, 3),
                                 "end": round(float(seg.end) + offset, 3),
                                 "text": seg.text.strip()})
            print(f"Chunk {i + 1}: {result.text}")
    return {"text": " ".join(texts).strip(), "segments": segments,
            "duration_seconds": len(audio) / 1000.0}


def srt_timestamp(seconds):
    milliseconds = round(seconds * 1000)
    hours, remainder = divmod(milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    secs, ms = divmod(remainder, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{ms:03d}"


def export_results(data, folder, name):
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    (folder / f"{name}.json").write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    lines = [f"[{srt_timestamp(s['start'])} - {srt_timestamp(s['end'])}] {s['text']}"
             for s in data["segments"]]
    (folder / f"{name}.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    blocks = [f"{i}\n{srt_timestamp(s['start'])} --> {srt_timestamp(s['end'])}\n{s['text']}"
              for i, s in enumerate(data["segments"], 1)]
    (folder / f"{name}.srt").write_text("\n\n".join(blocks) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Transcribe meeting audio with Whisper")
    parser.add_argument("--audio", required=True, help="Path to a local audio recording")
    parser.add_argument("--prompt", default="", help="Context/technical vocabulary for guided transcription")
    parser.add_argument("--chunk-minutes", type=float, default=10)
    parser.add_argument("--output", default="outputs")
    args = parser.parse_args()
    if not Path(args.audio).is_file():
        parser.error(f"Audio file not found: {args.audio}")
    client = get_client()
    print("Transcribing without prompt...")
    plain = transcribe_chunked(client, args.audio, args.chunk_minutes)
    export_results(plain, args.output, "unprompted")
    print("\nWithout prompt:\n", plain["text"])
    if args.prompt:
        print("\nTranscribing with prompt...")
        guided = transcribe_chunked(client, args.audio, args.chunk_minutes, prompt=args.prompt)
        export_results(guided, args.output, "prompted")
        print("\nWith prompt:\n", guided["text"])
        print("\nCompare both outputs in outputs/unprompted.txt and outputs/prompted.txt")
    else:
        print("\nSupply --prompt to also generate the guided comparison.")
    print(f"\nExports saved to {args.output}/")


if __name__ == "__main__":
    main()
