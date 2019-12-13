from flask import Flask
import sounddevice as sd
from scipy.io.wavfile import write

class RecordAudio():
    fs=44100
    second=15
    print("Recording...")
    record_voice=sd.rec(int(second * fs), samplerate = fs, channels = 2)
    sd.wait()
    write("output.wav", fs, record_voice) 

