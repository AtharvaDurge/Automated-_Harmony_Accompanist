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
```

---

## ▶️ How to Run

### Prerequisites

* Python 3.8 or higher installed — [download here](https://www.python.org/downloads/)
* A working microphone connected to your computer
* Git (optional, for cloning) — [download here](https://git-scm.com/)

### Step 1 — Clone the Repository

```bash
git clone https://github.com/your-username/automated-harmony-accompanist.git
cd automated-harmony-accompanist
```

> If you downloaded the ZIP instead, extract it and open a terminal inside the project folder.

### Step 2 — Create a Virtual Environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

> You should see `(.venv)` appear at the start of your terminal prompt, confirming the environment is active.

### Step 3 — Install Dependencies

```bash
pip install -r Requirements.txt
```

This installs:

| Package | Version |
|---|---|
| numpy | ≥ 1.26.0 |
| sounddevice | ≥ 0.5.0 |

> **macOS users:** `sounddevice` may require PortAudio. Install it with Homebrew: `brew install portaudio`
>
> **Linux users:** Install PortAudio via your package manager: `sudo apt install portaudio19-dev` (Debian/Ubuntu)

### Step 4 — Run the Application

```bash
python src/main.py
```

### Step 5 — Use It

1. When you see `Calibrating noise... stay quiet`, remain silent for about half a second while the app measures your room's background noise level.
2. Once you see `Start humming...`, hum or sing a steady note into your microphone.
3. The app detects your pitch, identifies the note, and immediately plays back a 3-note major chord (your note + major third + perfect fifth) for 3 seconds.

**Example output:**

```
Calibrating noise... stay quiet
Noise level: 0.0023
Start humming...
Detected frequency: 261.63
Detected note: C
Harmony: E G
```

### Stopping the App

Press `Ctrl + C` in the terminal at any time to quit.

---

## 🔧 Troubleshooting

**No audio input detected / app keeps printing "Waiting for voice..."**
Your microphone volume may be too low. Try speaking louder, moving closer to the mic, or increasing input gain in your system's sound settings.

**`sounddevice` import error on macOS or Linux**
PortAudio is not installed. Follow the OS-specific instructions in Step 3 above.

**`No Default Input Device` error**
No microphone is detected by your system. Check that your mic is plugged in and set as the default input device in your OS audio settings.