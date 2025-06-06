# SPEECH-RECOGNITION-SYSTEM

*COMPANY*: CODTECH IT SOLUTIONS PVT.LTD

*NAME*: Manvit Mahesh Deshmukh

*INTERN ID*: CT12DL764

*DOMAIN*: Artificial intelligence.

*DURATION*: 12 weeks

*MENTOR*:  Neela Santhosh Kumar


# 🧠 Speech-to-Text Project (CodTech AI Internship - Task 2)

Hey there! 👋  
This project is part of Task 2 of the CodTech AI Internship program, and it's all about **converting speech (audio) into text** using Python. Basically, we're teaching the computer how to *listen* and *understand* what we're saying — which is kinda cool, right?

This project runs completely in **Google Colab**, which means you don’t need to install anything heavy on your PC. All the code is designed to look and feel like it’s written by a regular person (not some pro dev), so it’s super beginner-friendly.

---

## 💡 What This Project Does

This speech-to-text system takes any audio file you give it (like `.wav`, `.mp3`, or even `.webm`) and tries to convert what’s being said in the audio into readable text. You can talk into your phone, record a voice message, upload it, and then run the code to get your words in text form.

We tried two methods here:
1. **Using Google's Web Speech API** (via the `SpeechRecognition` library)
2. **Using Facebook's Wav2Vec2 AI Model** (through Hugging Face, fully local)

You can choose whichever one works better for you.

---

## 🚀 Features

- 🎙 Accepts multiple audio formats: `.wav`, `.mp3`, `.webm`
- 📢 Converts voice recordings to text
- 🔄 Automatically converts audio files to the correct format if needed
- 🤖 Option to use AI (Wav2Vec2) or Google API
- 👨‍💻 Code written in a chill, unprofessional human style — easy to follow

---

## 📦 Libraries Used

- `speech_recognition`: For using Google Web Speech API
- `pydub`: For converting audio formats
- `transformers`, `torchaudio`, `soundfile`: For using the Wav2Vec2 model
- `ffmpeg`: Needed in Colab for handling `.webm` or `.mp3` (already installed usually)

---

## 🎧 How to Use It (in Colab)

1. Open the Colab notebook.
2. Upload your audio file using the upload button.
3. Let the code convert your file to `.wav` if needed.
4. Run the speech-to-text code.
5. Boom 💥 — your text appears in the output.

You can also use a fun or weird voice just to test how well the system understands you. It’s actually fun to break it 😅

---

## 🧪 Sentences to Test

Try these for fun:
- “Hello, I am testing speech to text.”
- “The quick brown fox jumps over the lazy dog.”
- “I wonder if this thing can understand my accent.”
- “Hey, can you hear me clearly or not?”

You can even say random things like:
> "Umm... okay so like, this is a test, let’s see if it works lol"

---

## 📌 Limitations

- Google's API needs internet and sometimes gives errors if it can’t hear properly.
- The Wav2Vec2 model might take longer to run, especially on big audio files.
- Background noise and unclear speech can mess with accuracy.

---

## 🤝 Credits

This is a self-made, beginner-friendly project for learning AI, speech processing, and Python basics. Built with love during the **CodTech AI Internship 2025** 💙

Special thanks to:
- Google Colab (for making life easier)
- Hugging Face (for the amazing models)

---

## 📂 Output Example

**Audio File:** `test_audio.wav`  
**Output Text:** `"Hello, this is a speech to text demo using Google API."`

---

That’s pretty much it! Have fun messing with speech files and seeing what your computer thinks you're saying 😄
