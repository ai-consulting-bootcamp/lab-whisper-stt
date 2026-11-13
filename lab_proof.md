# Whisper STT Lab Proof

This file is the reviewer entry point. The complete workflow, executed cells, and outputs are in the [Whisper STT implementation notebook](./LAB%20%7C%20Whisper%20STT%20Implementation.ipynb).

## Workflow and code

The notebook loads the sample recording, makes an unprompted and prompted 30-second transcription, splits the full recording into audio chunks, transcribes each chunk, offsets local segment timestamps to the original recording, and exports timestamped TXT, SRT, and JSON files.

Core chunk transcription and timestamp-offset logic:

```python
result = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file,
    response_format="verbose_json",
    timestamp_granularities=["segment"],
)

offset_seconds = chunk_start_ms / 1000
for segment in result.segments:
    combined_segments.append({
        "start": round(offset_seconds + segment.start, 2),
        "end": round(offset_seconds + segment.end, 2),
        "text": segment.text.strip(),
    })
```

## Run and input

- **Input:** [MS072.mp3](./MS072.mp3), an MP3 recording, 133.04 seconds long, stereo, 44.1 kHz, 128 kbps (2,128,693 bytes).
- **Run:** Transcribed the complete recording in three 1-minute chunks with `whisper-1`, requesting verbose JSON segment timestamps. The source was split into 60.0 s, 60.0 s, and 13.0 s files.
- **Evidence:** The notebook reported all three chunks transcribed and saved 23 timestamped segments. The first segment was `[00:00:00.00–00:00:06.00]` “Now you just pretend you hadn't talked to me any before, and you tell me about the government moving you up here.”
- **Prompt comparison:** The prompted and unprompted 30-second results were nearly identical. The prompted version changed punctuation and rendered “you understand?” as “Do you understand?”; there was no clear lexical accuracy gain in this clip.

Chunk audio: [chunk 1](./audio/chunks/MS072_1min_001.mp3) · [chunk 2](./audio/chunks/MS072_1min_002.mp3) · [chunk 3](./audio/chunks/MS072_1min_003.mp3)

## Final exports

- [Readable timestamped transcript (TXT)](./transcripts/MS072_transcript_with_timestamps.txt)
- [Subtitle transcript (SRT)](./transcripts/MS072_transcript.srt)
- [Structured transcript (JSON)](./transcripts/MS072_transcript.json)
- [Unprompted 30-second result](./transcripts/MS072_first_30s_unprompted.txt) · [Prompted result](./transcripts/MS072_first_30s_prompted.txt)

The exports were read back and checked: the TXT is readable, the SRT contains 23 numbered cues, and the JSON contains 23 segments. SRT cues use the SubRip structure of sequential numbering, start/end timecodes in `HH:MM:SS,mmm` form, subtitle text, and a blank line between cues ([Library of Congress format description](https://www.loc.gov/preservation/digital/formats/fdd/fdd000569.shtml)).

## Failure encountered

The first `pydub` import failed with `ModuleNotFoundError: No module named 'pyaudioop'` under Python 3.14, where the standard-library `audioop` module is unavailable. Installing `audioop-lts` in the notebook environment and restarting the kernel fixed the import; the MP3 then loaded successfully.
