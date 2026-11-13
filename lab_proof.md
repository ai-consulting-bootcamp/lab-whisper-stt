# Lab Proof: Whisper STT Implementation

## 1. Project overview

This project uses OpenAI Whisper to transcribe meeting audio.

Implemented features:

- Basic transcription without chunking
- Prompted transcription
- Unprompted transcription
- Audio chunking
- Timestamp extraction
- TXT, SRT, and JSON exports

## 2. Code and workflow

The complete workflow is available in:

- [stt.ipynb](stt.ipynb)

The project uses:

- Python virtual environment: `.venv`
- OpenAI Python SDK
- pydub
- FFmpeg

The API key was stored in `.env` and excluded through `.gitignore`.

## 3. Input

Input audio file:

- `audio/Wisconsin, Well witching sample .mp3`
- Format: MP3
- Duration: approximately 66.7 seconds
- Channels: mono
- Sample rate: 44,100 Hz

The file was verified successfully with FFmpeg and pydub.

## 4. Run/query and input

The basic transcription request was:

```python
with audio_file.open("rb") as file:
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=file
    )

print(transcription.text)


The guided transcription used this contextual prompt:

This is a conversational oral-history recording about well witching and finding groundwater.
Relevant terms may include water veins, peach stick, wells, right angles,
north, south, east, and west. Preserve the natural conversational wording.

Chunked transcription used 30-second chunks for this short sample.


5. Evidence produced
The basic transcription returned an OpenAI Transcription object and readable text.

The input audio was split into three chunks:
- Approximately 30 seconds
- Approximately 30 seconds
- Approximately 6.7 seconds
Timestamped segment evidence was saved in:
- [chunked_segments.json](transcripts/chunked_segments.json)


6. Final outputs
- [Basic transcription](transcripts/basic_transcription.txt)
- [Prompted transcription](transcripts/prompted_transcription.txt)
- [Unprompted transcription](transcripts/unprompted_transcription.txt)
- [Timestamped segments](transcripts/chunked_segments.json)
- [Human-readable TXT export](exports/chunked_transcription.txt)
- [SRT subtitle export](exports/chunked_transcription.srt)
- [JSON export](exports/chunked_transcription.json)


7. Prompted versus unprompted comparison
The prompted and unprompted transcriptions were generated from the same audio file.

The comparison focused on terms such as:
- well witching
- water veins
- peach stick
- right angles
- compass directions
The prompt provided useful contextual vocabulary, although the differences were limited because the sample was a short conversational recording.
8. Failure or limitation
Python 3.14 initially caused pydub to fail because the older pydub version expected the removed audioop module.

FFmpeg also required PATH configuration before it could be called directly from PowerShell.