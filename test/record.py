"""
PyAudio example:
Record a few seconds of audio and save to a WAVE file.
"""


import pyaudio
import wave
import sys

chunk = 1024
FORMAT = pyaudio.paInt16
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

CHANNELS = 1 if sys.platform == 'darwin' else 2
p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                frames_per_buffer = chunk)

print("* recording")
all = []

for _ in range(int(RATE / chunk * RECORD_SECONDS)):
    data = stream.read(chunk)
    all.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

# write data to WAVE file
data = b''.join(all)
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(data)
wf.close()
