import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import wave

p = pyaudio.PyAudio()

SABAD = 1024
RATE = 16000
SECONDS = 5

stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=RATE,
    input=True,
    frames_per_buffer=SABAD
)

frames = []

print("🎤 Recording started! Please speak...")

for i in range(int(RATE / SABAD * SECONDS)):
    a = stream.read(SABAD)
    frames.append(a)

print("Recording finished!")

audio_data = np.frombuffer(
    b"".join(frames),
    dtype=np.int16
)

stream.stop_stream()
stream.close()
p.terminate()

plt.figure()
plt.plot(audio_data)
plt.title("Original Sound")
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.show()

print("Audio data type:", type(audio_data))
print("Audio data:", audio_data)
print("Chunk type:", type(a))
print("Chunk length:", len(a))

audio_data = audio_data * 5

plt.close()
plt.specgram(audio_data, Fs=16000)
plt.show()

male_sound = audio_data

p = pyaudio.PyAudio()

out = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=16000,
    output=True,
    frames_per_buffer=SABAD
)

print("Playing original sound...")

out.write(
    audio_data.astype(np.int16).tobytes()
)

print("Playback finished!")

out.stop_stream()
out.close()
p.terminate()

audio_data = audio_data[10000:50000]

for x in range(len(audio_data)):
    if audio_data[x] < 100 and audio_data[x] > -100:
        audio_data[x] = 0

print("Very weak sounds were removed.")

plt.figure()
plt.plot(audio_data)
plt.title("Changed Sound")
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.show()

p = pyaudio.PyAudio()

out = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=10000,
    output=True,
    frames_per_buffer=SABAD
)

print("Playing changed sound...")

out.write(
    audio_data.astype(np.int16).tobytes()
)

print("Changed sound playback finished!")

out.stop_stream()
out.close()
p.terminate()

out_fft = np.fft.fft(audio_data)

tpCount = len(audio_data)

values = np.arange(int(tpCount / 2))

timeperiod = tpCount / 16000

frequencies = values / timeperiod

out_fft = out_fft[0:20000]

out_fft = abs(out_fft)

plt.close()
plt.plot(out_fft)
plt.title("FFT of Audio Signal")
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.show()

print("FFT shape:", out_fft.shape)

plt.close()
plt.plot(frequencies, out_fft)
plt.title("Frequency Spectrum")
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.show()

print("FFT shape:", out_fft.shape)
print("Maximum FFT value:", max(out_fft))
