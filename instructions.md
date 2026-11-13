# Whisper STT Implementation

> **How you'll submit this lab**
>
> This repo is your lab. Fork it, do the work described below in your fork, then open a pull
> request back into this repository. An AI reviewer will check your PR against `rubric.md` and
> leave feedback directly on the PR. See `README.md` for the full workflow.

**Scenario**  
You're working as an AI consultant for a company that needs to transcribe meeting recordings. Your client has hours of meeting audio that need to be converted to text with timestamps for easy reference and searchability. You'll use OpenAI's Whisper API to transcribe the audio, implement chunking for long recordings, and extract timestamps for each segment. This lab will teach you both guided (with prompts) and unguided (without prompts) transcription approaches.

**Learning Objectives**
- [ ] Set up OpenAI Whisper API access
- [ ] Transcribe audio files using Whisper
- [ ] Implement audio chunking for long recordings
- [ ] Extract timestamps from transcriptions
- [ ] Use prompts to guide transcription (guided approach)
- [ ] Transcribe without prompts (unguided approach)
- [ ] Compare results between prompted and unprompted transcriptions
- [ ] (Optional - Advanced) Export transcriptions with timestamps in multiple formats

**Estimated Time:** 150-180 minutes

**Prerequisites:**
- [ ] Basic understanding of Python
- [ ] Familiarity with API concepts
- [ ] Understanding of audio file formats
- [ ] Completion of previous API labs

---

## Introduction

Welcome to the Whisper STT (Speech-to-Text) Implementation lab! In this exercise, you'll learn how to use OpenAI's Whisper API to transcribe audio files. Whisper is a powerful speech recognition model that can handle multiple languages, accents, and audio qualities.

**What you'll build:**
- Audio transcription system using Whisper API
- Chunking system for long audio files
- Timestamp extraction and formatting
- Comparison between prompted and unprompted transcriptions
- Export functionality for transcriptions

**Why this matters:**
Speech-to-text is a fundamental AI capability used in:
- Meeting transcription and note-taking
- Accessibility features (captions, subtitles)
- Voice assistants and voice commands
- Content creation and podcast transcription
- Customer service call analysis

**Success criteria:**
- [ ] Successfully transcribe audio files
- [ ] Implement chunking for long recordings
- [ ] Extract and format timestamps
- [ ] Compare prompted vs. unprompted results
- [ ] Export transcriptions in readable format

---

## Background Story

Your client has recorded important business meetings and needs them transcribed. The requirements are:

1. **Accurate transcription** - Must capture all spoken content
2. **Timestamps** - Need to know when each part was said
3. **Long recordings** - Some meetings are 2+ hours long
4. **Context awareness** - Technical terms and names should be correct
5. **Searchable format** - Easy to search through transcripts

You'll implement a solution that:
- Handles long audio files by chunking them
- Provides timestamps for easy navigation
- Uses prompts to improve accuracy for technical content
- Exports results in a useful format

---

## Step-by-Step Instructions

### Step 1: Setting Up the Environment

**Objective:** Install required libraries and set up project structure.

**What to do:**
1. Install required packages
2. Set up OpenAI API access
3. Prepare audio file handling

**Required packages:**
```bash
pip install openai pydub
```

**Note:** `pydub` requires `ffmpeg` for audio processing. Install it:
- **Windows:** Download from [ffmpeg.org](https://ffmpeg.org/download.html) or use `choco install ffmpeg`
- **Mac:** `brew install ffmpeg`
- **Linux:** `sudo apt-get install ffmpeg`


You can use the [`stt.ipynb`](https://github.com/ai-consulting-bootcamp/ac-bootcamp-public/blob/main/notebooks/week-1/submodule-4-speech-recognition/stt.ipynb) notebook as a starting point. 
You will need to change the data sources and implement some extra functionality that will be described in the steps below.


**Expected outcome:** You should have the environment set up with necessary directories.

**Checkpoint:** Verify that OpenAI client initializes and directories are created.

---

### Step 2: Downloading Sample Meeting Audio

**Objective:** Get a sample meeting audio file for transcription.

**What to do:**
1. Download a sample meeting audio file
2. Verify the file is accessible
3. Check audio properties

**Sample Audio :**

**Option 1: Use Provided Sample**
We'll provide a sample meeting audio. Download from:
- **Sample Meeting Audio:** [Meeting Sample](https://dare.wisc.edu/audio/)

**Option 2: Use Your Own Audio**
If you have your own meeting audio, place it in the `audio/` directory.

**Expected outcome:** You should have an audio file ready for transcription.

**Checkpoint:** Verify that the audio file exists and can be loaded.

---

### Step 3: Basic Transcription (Without Chunking)

**Objective:** Transcribe a short audio file to understand the basic API usage.

**What to do:**
1. Transcribe a short part of the audio file
2. Understand the API response format
3. Extract basic transcription text

**Expected outcome:** You should see the transcribed text and basic information.

**Checkpoint:** Verify that transcription works and you can see the output.

---

### Step 4: Transcription with Prompts (Guided Approach)

**Objective:** Use prompts to guide transcription and improve accuracy.

**What to do:**
1. Create prompts with context (technical terms, names, etc.)
2. Transcribe with prompts
3. Compare results

**Expected outcome:** You should see transcription results that may be more accurate due to the prompt context.

**Checkpoint:** Verify that prompted transcription works and results are saved.

---

### Step 5: Transcription Without Prompts (Unguided Approach)

**Objective:** Transcribe the same audio without prompts for comparison.

**What to do:**
1. Transcribe without any prompt
2. Compare with prompted results
3. Analyze differences


**Expected outcome:** You should see both transcriptions and be able to compare them.

**Checkpoint:** Verify that both approaches work and you can compare results.

---

### Step 6: Implementing Audio Chunking

**Objective:** Split long audio files into chunks for processing.

**What to do:**
1. Split audio into manageable chunks (e.g., 10-minute segments)
2. Process each chunk separately
3. Combine results with proper timestamps

**Expected outcome:** You should have audio files split into chunks.

**Checkpoint:** Verify that chunks are created correctly.

---

### Step 7: Transcribing Chunks with Timestamps

**Objective:** Transcribe each chunk and combine with proper timestamps.

**What to do:**
1. Transcribe each chunk
2. Adjust timestamps to account for chunk offset
3. Combine all transcriptions
4. Export with timestamps

**Expected outcome:** You should have a complete transcription with timestamps from chunked audio.

**Checkpoint:** Verify that chunked transcription works and timestamps are correct.

---

### Step 8: Exporting with Timestamps

**Objective:** Export transcriptions in readable formats with timestamps.

This is new. Take your time to research and implement!

**What to do:**
1. Create human-readable format with timestamps
2. Export to text file
3. Export to SRT (subtitle) format
4. Export to JSON


**Expected outcome:** You should have transcriptions exported in multiple formats.

**Checkpoint:** Verify that exports work and files are readable.

---

## Submission Guidelines

### What to Submit

**Required deliverables:**
- [ ] Your complete `whisper_transcription.py` file with:
  - Basic transcription functions
  - Chunking implementation
  - Prompted and unprompted transcription
  - Timestamp extraction
  - Export functions
- [ ] Sample transcriptions (JSON, text, SRT formats)
- [ ] Screenshots or output showing:
  - Successful transcriptions
  - Comparison between prompted and unprompted
  - Timestamp extraction
  - Chunked transcription results
- [ ] A brief report (1 page) including:
  - Differences between prompted and unprompted transcriptions
  - Benefits of chunking for long audio
  - Challenges you faced
  - Recommendations for improving accuracy

### How to Submit

**Upload your work:**
1. **For code files:** Upload your Python script
2. **For transcriptions:** Upload sample output files
3. **For screenshots:** Upload PNG or JPG images
4. **For reports:** Upload PDF or text files

**Important notes:**
- Include your API key setup (but not the actual key!)
- Show examples of both prompted and unprompted transcriptions
- Document your chunking strategy
- Explain timestamp handling

**Due date:** Check with your instructor for the specific due date.

---

## Troubleshooting

**Common issues and solutions:**

**Issue 1: "File size too large" error**
- **Solution:** 
  - Whisper API has a 25MB file size limit
  - Use chunking for large files
  - Compress audio if needed
  - Convert to supported format (mp3, wav, etc.)

**Issue 2: "ffmpeg not found" error**
- **Solution:** 
  - Install ffmpeg (see Step 1)
  - Add ffmpeg to your system PATH
  - On Windows, may need to restart terminal

**Issue 3: "API rate limit exceeded"**
- **Solution:** 
  - Add delays between API calls
  - Process chunks sequentially with delays
  - Check your API tier limits

**Issue 4: "Timestamps are incorrect after chunking"**
- **Solution:** 
  - Make sure you're adding chunk offset to timestamps
  - Verify chunk start times are calculated correctly
  - Check that segments are being adjusted properly

**Issue 5: "Transcription quality is poor"**
- **Solution:** 
  - Use prompts with relevant context
  - Ensure audio quality is good (clear, minimal noise)
  - Specify language parameter correctly
  - Check audio format and sample rate

**Issue 6: "Chunking creates too many small files"**
- **Solution:** 
  - Adjust chunk_length_minutes parameter
  - For very long files, use larger chunks (15-20 minutes)
  - Consider processing in batches

---

## Additional Resources

**Reference materials:**
- [OpenAI Whisper API Documentation](https://platform.openai.com/docs/guides/speech-to-text)
- [Whisper Model Details](https://github.com/openai/whisper)
- [Audio Processing with pydub](https://github.com/jiaaro/pydub)

**Tools and software:**
- [OpenAI Platform](https://platform.openai.com/) - API dashboard
- [FFmpeg](https://ffmpeg.org/) - Audio processing tool
- [Audacity](https://www.audacityteam.org/) - Audio editor (for testing)

**Further reading:**
- [Speech Recognition Best Practices](https://platform.openai.com/docs/guides/speech-to-text/prompting)
- [Audio Chunking Strategies](https://github.com/openai/whisper/discussions)
- [Subtitle Format Specifications](https://en.wikipedia.org/wiki/SubRip)

---

## To-Do List

- [ ] Complete Step 1: Setting Up the Environment
- [ ] Complete Step 2: Downloading Sample Meeting Audio
- [ ] Complete Step 3: Basic Transcription (Without Chunking)
- [ ] Complete Step 4: Transcription with Prompts (Guided Approach)
- [ ] Complete Step 5: Transcription Without Prompts (Unguided Approach)
- [ ] Complete Step 6: Implementing Audio Chunking
- [ ] Complete Step 7: Transcribing Chunks with Timestamps
- [ ] Complete Step 8: Exporting with Timestamps
- [ ] Compare prompted vs. unprompted results
- [ ] Test with different audio files
- [ ] Submit your work

---

## Learning Reflection

After completing this lab, reflect on what you've learned:

1. **Speech-to-Text:** How does Whisper convert audio to text?
2. **Prompts:** How do prompts improve transcription accuracy?
3. **Chunking:** Why is chunking necessary for long audio files?
4. **Timestamps:** How are timestamps useful in transcriptions?
5. **API Usage:** What are best practices for using the Whisper API?
6. **Error Handling:** What challenges did you face with audio processing?

**Key takeaways:**
- Whisper provides powerful speech-to-text capabilities
- Prompts can significantly improve accuracy for technical content
- Chunking is essential for processing long audio files
- Timestamps enable navigation and searchability
- Proper error handling is crucial for production systems
- Multiple export formats serve different use cases

These skills are essential for building transcription systems and working with audio data in AI applications.

---

*Excellent work on implementing Whisper STT! You've learned how to transcribe audio, handle long recordings, and extract timestamps - skills that are valuable in many AI applications.*
