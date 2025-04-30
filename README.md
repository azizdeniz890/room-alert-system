# Room Alert System with YOLOv5 and ESP32

This is a school project for detecting people in a room using YOLOv5 via an IP camera. When a person is detected, a Bluetooth signal is sent to an ESP32, which displays a message and activates a buzzer.

## Project Structure

```
ROOM_ALERT_PROJECT/
├── python/
│   ├── tespit.py           # Basic version (prints to terminal)
│   ├── tespit+b.py         # Sends Bluetooth signal to ESP32
│   └── yolov5s.pt          # YOLOv5s model (used in both scripts)
├── esp32/
│   └── esp32_arduino.ino   # ESP32 code for display and buzzer
├── environment.yml         # Conda environment file
├── requirements.txt        # For pip-based setup
├── Dockerfile              # Optional Docker support
└── README.md
```

## Setup (Python)

### Option 1: Conda

```
conda env create -f environment.yml
conda activate room_alert_env
python python/tespit+b.py
```

### Option 2: pip

```
python -m venv room_alert_env
.\room_alert_env\Scripts\activate
pip install -r requirements.txt
python python/tespit+b.py
```

```
Replace `COM4` with the correct serial/Bluetooth device on your system.

## Notes

- The YOLOv5 model used is `yolov5s.pt`.
- ESP32 must be paired over Bluetooth, and the correct COM port must be set in the script.
- OLED and buzzer are controlled by the ESP32 when a detection is received.
