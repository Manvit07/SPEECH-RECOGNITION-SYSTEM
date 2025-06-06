
# This is for speech recognition (needs internet)
!pip install SpeechRecognition pydub

# This is for using a cool AI model from HuggingFace (can work offline kinda)
!pip install transformers torchaudio soundfile

# Use this to upload from your computer
from google.colab import files
uploaded = files.upload()  # pick your file (like audio.wav)

# Get the file name
audio_path = list(uploaded.keys())[0]

import speech_recognition as sr
from pydub import AudioSegment

# so like, if the file is mp3, we gotta change it to wav coz google doesn’t like mp3s
if audio_path.endswith('.mp3'):
    sound = AudioSegment.from_mp3(audio_path)
    audio_path = 'converted_audio.wav'  # just naming it whatever
    sound.export(audio_path, format='wav')

# ok now if it’s a .webm file (some random format from phone maybe?), we try to convert that too
elif audio_path.endswith('.webm'):
    print(f"trying to change {audio_path} to wav lol...")
    try:
        # this needs ffmpeg i think... colab mostly has it but if not, gotta install it
        # like this maybe -> !apt-get install ffmpeg (do that separately if errors)
        sound = AudioSegment.from_file(audio_path, format="webm")
        audio_path = 'converted_audio.wav'
        sound.export(audio_path, format='wav')
        print("woohoo converted it ")
    except Exception as e:
        print("uh oh couldn’t convert the webm file. error was:")
        print(e)
        # not stopping the code... just moving on and praying it works

# now let’s try to hear what the person said in the audio
r = sr.Recognizer()

with sr.AudioFile(audio_path) as source:
    print("listening to the audio... hang tight")
    audio = r.record(source)  # grabbing the whole thing

# now we’ll use google’s thing to figure out the words
try:
    print("sending it to google... fingers crossed")
    text = r.recognize_google(audio)
    print("google thinks you said:")
    print(text)
except Exception as e:
    print("yikes couldn’t get the words out of the audio. error below ↓")
    print(e)

import torch
import soundfile as sf
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

# Load the brainy AI model and its processor
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

# Read the audio file
speech, sample_rate = sf.read(audio_path)

# If sample rate is not what the model wants, fix it
if sample_rate != 16000:
    import torchaudio
    print("Fixing audio sample rate...")
    speech = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)(torch.tensor(speech).float()).numpy()
    sample_rate = 16000

# Feed the audio to the model
input_values = processor(speech, sampling_rate=sample_rate, return_tensors="pt").input_values
logits = model(input_values).logits

# Get the most likely words
predicted_ids = torch.argmax(logits, dim=-1)
transcription = processor.decode(predicted_ids[0])

print("Wav2Vec2 thinks you said:")
print(transcription.lower())
