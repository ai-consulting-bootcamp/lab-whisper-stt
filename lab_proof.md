# Whisper STT Implementation Lab — Proof

## Workflow

The workflow was implemented in [whisper_stt_lab_final.ipynb](whisper_stt_lab_final.ipynb) using the `AC_PT_OCT` Jupyter kernel.

The notebook:

1. Validates the input audio and FFmpeg.
2. Runs an unprompted Whisper transcription.
3. Runs a prompted transcription using customs and freight terminology.
4. Splits the audio into 60-second chunks.
5. Transcribes each chunk with segment timestamps.
6. Adds each chunk's offset to create timestamps for the original recording.
7. Exports TXT, SRT, and JSON files.

## Input and run

- Input file: [TX048clip.mp3](TX048clip.mp3)
- Format: MP3
- Duration: 104.39 seconds
- Sample rate: 44,100 Hz
- Channels: 1
- File size: 1.17 MB
- Chunk length: 60 seconds
- Number of chunks: 2
- Whisper model: `whisper-1`

The prompted transcription used domain terms including CEDAS, pedimentos, appraisal sheet, bottling equipment, St. Louis, tariff duty, ad valorem rate, and Vistas. The input audio and prompt were processed by the notebook workflow linked above.

## Evidence produced

- The audio inspection completed successfully.
- The unprompted transcription completed successfully.
- The prompted transcription completed successfully.
- Both transcriptions recognized the tested domain terms.
- Chunking created `chunk_000.mp3` and `chunk_001.mp3`.
- Chunk transcription produced 25 timestamped segments.
- JSON validation confirmed 25 saved segments.
- SRT validation confirmed correctly formatted subtitle timestamps.

The prompted and unprompted transcriptions had a calculated similarity score of 47.07%. This shows that the prompt influenced wording while both versions retained the main technical vocabulary.

## Final outputs

- [Timestamped TXT](transcription_outputs/transcription_with_timestamps.txt)
- [Timestamped SRT](transcription_outputs/transcription_with_timestamps.srt)
- [Timestamped JSON](transcription_outputs/transcription_with_timestamps.json)
- [Final notebook](whisper_stt_lab_final.ipynb)

## Failure or limitation

The assignment notes that `pydub` requires FFmpeg for audio processing. Homebrew installation was attempted, but it could not complete because Homebrew was blocked while installing its Portable Ruby dependency. FFmpeg was then made available through the existing Anaconda installation.

The dedicated `AC_PT_OCT` environment uses Python 3.14, while the installed `pydub` version expects the removed `audioop` module. The workflow was therefore adapted to call FFmpeg directly for audio inspection and chunking. This keeps the work in the required kernel but means the final implementation does not rely on `pydub` for those operations.

Chunk boundaries may split a sentence or word between files, so a production system could use overlapping chunks and deduplication. The workflow also does not identify individual speakers.
