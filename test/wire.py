"""
PyAudio Example:

Make a wire between input and output (i.e., record a few samples
and play them back immediately).

Full Duplex version; see wire2.py for Half Duplex. """


import pyaudio
import sys

chunk = 1024
WIDTH = 2
RATE = 44100
RECORD_SECONDS = 5

CHANNELS = 1 if sys.platform == 'darwin' else 2
p = pyaudio.PyAudio()

stream = p.open(format =
                p.get_format_from_width(WIDTH),
                channels = CHANNELS,
                rate = RATE,
                input = True,
                output = True,
                frames_per_buffer = chunk)

print("* recording")
for _ in range(int(44100 / chunk * RECORD_SECONDS)):
    data = stream.read(chunk)
    stream.write(data, chunk)
print("* done")

stream.stop_stream()
stream.close()
p.terminate()
