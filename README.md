# Audio Signal Processing with Python

This project is a hands-on experiment with digital audio and the different ways a computer can look at and work with sound.

It starts with something very simple: recording a few seconds of audio through a microphone. After recording, the raw signal is converted into a NumPy array so it can be analyzed and visualized.

From there, the project explores several parts of audio processing. The original waveform is plotted to see how the sound changes over time, and a spectrogram is used to get a different view of the recorded signal.

The recorded audio is also modified by increasing its amplitude and removing very weak signal values. The changed signal is then played back so the difference between the original and processed sound can be observed.

The last part of the project focuses on frequency analysis. An FFT (Fast Fourier Transform) is applied to the audio signal to see which frequencies are present and how strong they are. The resulting frequency spectrum is plotted for a clearer look at the sound in the frequency domain.

### Main Tools

* Python
* NumPy
* PyAudio
* Matplotlib

### What This Project Explores

This project was built to practice the basic ideas behind audio signal processing, including:

* Recording audio from a microphone
* Working with raw audio samples
* Visualizing waveforms
* Creating spectrograms
* Modifying audio signals
* Playing processed audio
* Analyzing frequency content with FFT

### A Look at the Process

The overall flow is:

**Record → Analyze → Visualize → Modify → Play → Transform to Frequency Domain**

The goal was not to build a complicated audio application, but to understand what is happening to a sound signal at each stage and to see the results directly through Python.

### Running the Project

Install the required libraries:

```bash
pip install pyaudio numpy matplotlib
```

Then run:

```bash
python audio_processing.py
```

A working microphone and audio output device are required.

### Why I Built This

I created this project to get more familiar with audio data and to understand how sound can be represented mathematically.

Working with the waveform and FFT made it possible to see that audio is more than just something we hear — it is also a signal that can be measured, changed, and analyzed with code.
