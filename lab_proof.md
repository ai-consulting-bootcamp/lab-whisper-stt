## Files 

[whisper_lab.ipynb](./whisper_lab.ipynb)
[step4_prompted.json](./transcripts/step4_prompted.json)
[step5_unprompted.json](./transcripts/step5_unprompted.json)
[transcript.txt](./transcripts/transcript.txt)
[transcript.srt](./transcripts/transcript.srt)
[transcript.json](./transcripts/transcript.json)
[.gitignore](./.gitignore)

## Approach 
1. Setup: Installed openai, pydub, python-dotenv and audioop-lts; installed ffmpeg via conda. The API Key is loaded from .env. 
2. Sample audio: I chose the audio file: California, Moon landing (CA138clip.mp3). Casual conversation about the moon landing.
3. Basic transcription: The first 30 seocnds are cut out with pydub, saved as mp3 and sent to client.audio.transcriptions.create(model="whisper-1"). The default response (Transcription object) only contains .text. The call took 4.1 s.
4. Guided approach: same snippet with a context pormpt describing the topic and temp = 0. Result saved as JSON.
5. Unguided approach: same snippet, same settings, no prompt. Both versions are compared word by word with difflib. 
6. Chunking: The full recording is split into 30s chunks. The last one is a bit shorter. Each chunk stores its start offset. 
7. Chunks with timestamp: each chunk is transcribed wth response_format="verbose_json" and timestamp_granularities=["segment"]. Whispers timestamps restart at 0 for every chunk, so the chunks start offset is added to every segment. try/except per chunk and a 1s pause between calls handle errors and rate limits.
8. Export: The 14 combined segmetns are exported as TXT, SRT and JSON. 

### Model choice: I used whisper-1 because the newer transcription models (gpt-4o-transcribe, gpt-4o-mini-transcribe) do not return segment-level timestamps, which Steps 7 and 8 require.

## Example Run: Prompted vs Unpropmted

### Input
- Audio: first 30 s of CA138clip.mp3
- Model: whisper-1, temperature=0 in both runs
- Prompt (guided run only):
  A casual conversation about the Apollo moon landing. Topics: NASA, astronauts, lunar surface, kangaroo hop, splashdown, ticker-tape parade in New York.

### Evidence 
- Without prompt: 
It was rather interesting just to watch them gathering their materials and bouncing around their, what do they call it, kangaroo walk or something like that. Who named it that? I don't know. I bet those men are going to get quite a reception when they get back to New York. Oh yes, I'll be so glad when they land back now. I think that's pretty well a fact because they've landed so many safely now.
- With prompt: 
It was rather interesting just to watch them gathering their materials and bouncing around their, what they call it, kangaroo walk or something like that. Who named it that? I don't know. I bet those men are going to get quite a reception when they get back to Earth. Yes, I'll be so glad when they land back now, but I think that's pretty well a fact because they've landed so many safely now.
### difflib output: 
Word-level similarity: 93.3%

## Final Output
Transcript of CA138clip.mp3
Model: whisper-1 | Chunks: 3 x 30s | Prompt: guided

[00:00.00 - 00:13.00]  It was rather interesting just to watch them gathering their materials and bouncing around their, what they call it, kangaroo walk or something like that.
[00:13.00 - 00:15.00]  Who named it that? I don't know.
[00:15.00 - 00:19.00]  I bet those men are going to get quite a reception when they get back to Earth.
[00:19.00 - 00:30.00]  Yes, I'll be so glad when they land back now, but I think that's pretty well a fact because they've landed so many safely now.
[00:31.00 - 00:35.00]  I feel relieved. Just getting off of the moon was the thing that was...
[00:35.00 - 00:38.00]  Have they met with the one that was circling?
[00:38.00 - 00:44.00]  Yes, they've rendezvoused. So I understand. That wasn't shown either, so I...
[00:44.00 - 00:53.00]  But they say they have rendezvoused, so that's a matter of making the circles and then coming down.
[00:53.00 - 00:57.00]  What do you sort of imagine for the future? Do you imagine them sending a...
[00:57.00 - 01:00.00]  I think they will. I think they will.
[01:00.00 - 01:07.76]  We'll do some more exploring up there, because that was such a very small area, when you
[01:07.76 - 01:18.68]  think of it, that they just gathered rocks and, oh, samples of soil and all, and they
[01:18.68 - 01:24.84]  did a probe for some samples, and just what was going to come of that, I don't know, I'd
[01:24.84 - 01:25.88]  be glad to read it.

### Failure / Limitation
## The prompt fixes content but changes the style 
Without a prompt, Whisper misheard "Earth" as "New York". This is a content error that would mislead anyone searching the transcript. The context prompt fixed it, even though "New York" itself appeared in the prompt, so Whisper did not simply copy words from the prompt (it also kept the spoken "kangaroo walk" instead of the prompt's "kangaroo hop").

However, the prompt also made the transcript "cleaner" than the actual speech: it dropped the spoken filler words "do" and "Oh". Whisper does not follow the prompt as an instruction; it treats it as preceding text and adopts its style. Because my prompt was a clean sentence without fillers, the output became cleaner too.