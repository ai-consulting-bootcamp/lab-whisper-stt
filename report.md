# Whisper Speech-to-Text Lab Report

## 1. Objective

The objective of this lab was to test OpenAI Whisper for speech-to-text transcription, compare results with and without a prompt, and export the transcriptions in different formats.

## 2. Prompted vs. Unprompted Transcription

I recorded a short audio using my Mac microphone and tested it with Whisper.

Without a prompt, Whisper transcribed one phrase as “Play distance allowed for about 30 seconds.”

With a prompt, it produced “Play this text aloud for about 30 seconds.”

The second result was closer to the intended sentence. The prompted transcription also showed differences in punctuation and wording.

This suggests that context can help Whisper understand some expressions, although it does not guarantee that every word will be correct.

## 3. Audio Chunking

Audio chunking divides a long recording into smaller parts.

This can help process long meetings and make transcription easier to manage. However, dividing audio may affect sentences that continue between chunks.

In this test, the short recording was processed as one chunk, so I did not directly measure the benefits of splitting a long recording.

## 4. Challenges

One challenge was preparing the Python environment and installing the required libraries. I also needed to save the microphone recording as a WAV file to test the Python script.

The transcription contained some incorrect words, showing that automatic speech recognition is not always perfect.

## 5. Results and Recommendations

The program successfully generated TXT, JSON, and SRT files for both prompted and unprompted transcriptions.

I recommend providing relevant context for technical vocabulary, reviewing important transcriptions manually, and using audio chunking when working with longer recordings.

## 6. Conclusion

This lab helped me understand how Whisper converts speech into text and how prompts can influence transcription quality. It also showed the importance of validating AI-generated results.