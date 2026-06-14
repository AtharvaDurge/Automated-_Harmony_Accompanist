# Automated Harmony Accompanist 🎵

Automated Harmony Accompanist is an interactive, real-time Python application that listens to a hummed vocal input and instantly synthesizes a matching 3-part major triad chord harmony. By combining Digital Signal Processing (DSP) techniques with fundamental music theory, this tool provides automated vocal accompaniment on the fly.

---

## 🚀 Features

* **Adaptive Noise Calibration:** Measures ambient room noise for 0.5 seconds upon startup to establish a dynamic, reliable voice-activation threshold.
* **FFT Pitch Detection:** Analyzes the dominant frequency component of captured audio arrays using Fast Fourier Transform (FFT).
* **Music Theory Mapping:** Converts raw physical frequencies (Hz) into standard musical notes and MIDI values.
* **Instant Harmony Synthesis:** Mathematically computes major third and perfect fifth intervals to generate and play back a balanced, 3-part synthesized major chord.

---

## 🛠️ Tech Stack

* **Python 3**
* **NumPy** — Fast Fourier Transform (FFT) processing and audio array manipulation.
* **Sounddevice** — Low-latency, real-time microphone input sampling and audio playback.

---

## 📁 Folder Structure

```text
automated-harmony-accompanist/
│
├── src/
│   └── main.py              # Main application logic
│               
├── README.md                # Project documentation
└── Requirements.txt         # Project dependencies
