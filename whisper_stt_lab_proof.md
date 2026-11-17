# Lab Proof - Whisper STT Implementation

## Reviewer entry point

This submission demonstrates a Whisper speech-to-text workflow. It downloads and verifies an MP3 file, transcribes it with and without context, splits it into chunks, adds timestamps using the original audio offsets, and exports the results as TXT, SRT, and JSON.

## Code / workflow export

The complete workflow is in [`whisper_stt.ipynb`](whisper_stt.ipynb).

Supporting files:

- Input audio: [`audio/maine_boatmaking.mp3`](audio/maine_boatmaking.mp3)
- Chunked audio folder: [`audio_chunks/`](audio_chunks/)
- TXT export: [`transcripts/maine_boatmaking_transcript.txt`](transcripts/maine_boatmaking_transcript.txt)
- SRT export: [`transcripts/maine_boatmaking_transcript.srt`](transcripts/maine_boatmaking_transcript.srt)
- JSON export: [`transcripts/maine_boatmaking_transcript.json`](transcripts/maine_boatmaking_transcript.json)

No API key or environment file is included.

## Run and input

The workflow uses `audio/maine_boatmaking.mp3` as its input.

The main run performs these operations:

1. Loads the approximately 100-second MP3 file.
2. Sends the complete file to Whisper for a basic transcription.
3. Sends the same file with a context prompt about Maine boatmaking and maritime terminology.
4. Splits the file into four 30-second chunks, with a final 10-second chunk.
5. Transcribes each chunk with segment timestamps.
6. Adds each chunk's start-time offset to the returned timestamps.
7. Exports the combined timestamped results.

## Evidence produced

The notebook outputs show:

- FFmpeg was available and working.
- `openai` and `pydub` were installed.
- The OpenAI client initialized successfully.
- The input file was found and loaded successfully.
- The audio duration was approximately 99.97 seconds.
- The audio had 2 channels and a 44,100 Hz sample rate.
- Basic Whisper transcription completed successfully.
- Prompted transcription completed successfully.
- Prompted and unprompted transcripts were compared.
- Four chunks were created with ranges 0-30, 30-60, 60-90, and 90-100 seconds.
- Chunk transcription returned timestamped segments.
- TXT, SRT, and JSON exports were created successfully.

## Final output

The final files are:

- [`maine_boatmaking_transcript.txt`](transcripts/maine_boatmaking_transcript.txt) for human-readable review.
- [`maine_boatmaking_transcript.srt`](transcripts/maine_boatmaking_transcript.srt) for subtitles and captions.
- [`maine_boatmaking_transcript.json`](transcripts/maine_boatmaking_transcript.json) for structured programmatic use.

The JSON export preserves the source path and timestamped transcript segments. The SRT export contains numbered subtitle entries with start and end times.

## Failure or limitation

The initial Pydub check failed because Python 3.14.6 no longer includes the older `audioop` module required by Pydub 0.25.1. Installing `audioop-lts` and restarting the notebook kernel resolved the compatibility issue.

The sample audio was only about 100 seconds and 1.6 MB, so it did not require chunking for the Whisper file-size limit. Chunking was performed to demonstrate the required long-audio workflow. The prompted and unprompted transcripts were identical for this sample, so an improvement from prompting was not observable in this run.

