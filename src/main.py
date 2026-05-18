import sounddevice as sd
import numpy as np
import time

fs = 16000
buffer_size = 4096

print("Calibrating noise... stay quiet")
time.sleep(0.5)

# measure background noise
noise_levels = []
for _ in range(5):
    noise = sd.rec(buffer_size, samplerate=fs, channels=1)
    sd.wait()
    noise = noise.flatten()
    noise_levels.append(np.sqrt(np.mean(noise**2)))

noise_floor = np.mean(noise_levels)
threshold = noise_floor    # adaptive threshold

print("Noise level:", noise_floor)
print("Start humming...")

while True:
    audio_buffer = sd.rec(buffer_size, samplerate=fs, channels=1)
    sd.wait()

    audio_buffer = audio_buffer.flatten()
    volume = np.sqrt(np.mean(audio_buffer**2))

    if volume > threshold:
        break
    else:
        print("Waiting for voice...")

# FFT
fft_data = np.fft.fft(audio_buffer)
magnitude = np.abs(fft_data)

peak_index = np.argmax(magnitude)
frequency = peak_index * fs / buffer_size

print("Detected frequency:", frequency)


def freq_to_note(freq):
    A4 = 440
    n = 12 * np.log2(freq / A4)
    midi = int(round(n)) + 69
    notes = ['C','C#','D','D#','E','F',
             'F#','G','G#','A','A#','B']
    return notes[midi % 12]


note = freq_to_note(frequency)
print("Detected note:", note)


def harmony(note):
    notes = ['C','C#','D','D#','E','F',
             'F#','G','G#','A','A#','B']
    i = notes.index(note)
    return notes[(i+4)%12], notes[(i+7)%12]


h1, h2 = harmony(note)
print("Harmony:", h1, h2)


def note_to_freq(note, octave=4):
    notes = ['C','C#','D','D#','E','F',
             'F#','G','G#','A','A#','B']
    i = notes.index(note)
    midi = i + (octave + 1) * 12
    return 440 * (2 ** ((midi - 69) / 12))


freq1 = note_to_freq(h1)
freq2 = note_to_freq(h2)


def generate_tone(freq, duration=3):
    t = np.linspace(0, duration, int(fs * duration), False)
    return np.sin(2 * np.pi * freq * t)


main_tone = generate_tone(frequency)
harmony1 = generate_tone(freq1)
harmony2 = generate_tone(freq2)

output = (main_tone + harmony1 + harmony2) / 3

sd.play(output, fs)
sd.wait()

