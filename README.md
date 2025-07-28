# SAM - Voice Assistant

## Overview
SAM is an AI-powered voice assistant designed to assist users with various tasks through voice commands. Leveraging natural language processing (NLP) and voice recognition technologies, SAM enables seamless interaction and improves user productivity.

## Features
- **Voice Command Recognition**: Understands and processes user commands using intent recognition.
- **Natural Language Understanding**: Utilizes NLP techniques to interpret and respond to user queries effectively.
- **Voice Interaction**: Provides a smooth interaction experience through voice-based responses.
- **System Controls**: Allows users to manage system functionalities using voice commands.
- **Online Searches**: Capable of performing online searches based on user requests.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Backend**: Python
- **Desktop Interface**: Eel (for integrating Python backend with an HTML/CSS/JS frontend)
- **Deep Learning**: TensorFlow (Keras API)
- **Model Training**: The model was trained using a Bidirectional LSTM neural network with an embedding layer, trained for 100 epochs on a dataset of intents defined in `Intent.json`. The model uses the Adam optimizer with a learning rate of 0.001 and categorical crossentropy loss.

## Model Performance
- **Total Samples**: 3,045 natural language utterances (user queries) defined in `Intent.json`
- **Train-Test Split**: 80% for training (2,436 samples), 20% for testing (609 samples)
- **Test Accuracy**: 90.64%
- **Test Loss**: 0.7605
- **Classification Metrics**:
  - **Macro Average Precision**: 0.87
  - **Macro Average Recall**: 0.87
  - **Macro Average F1-Score**: 0.86
- The model was evaluated using a multi-class classification setup across all defined intents.

## Capabilities

### System Controls
- Lock System
- Sleep System
- Sign Out
- Restart System
- Shutdown System

### Assistant Controls
- Assistant State Control (Wake Up, Sleep Assistant, Exit SAM)
- Simple Dialogues (Greeting, Name, User Identity, Status, Capabilities, Thank You, Goodbye, Apology, Hobbies, Dreams, Meaning of Life, Robot, Good Day)

### Date and Time
- Get Current Time / Hour / Date / Day / Month / Year
- Get Yesterday's Date / Day / Month / Year
- Get Day Before Yesterday
- Get Tomorrow's Date / Day / Month / Year
- Get Day After Tomorrow
- Tell Combined Time and Date Info (e.g., Time and Date, Time and Day)

### Internet & Network
- Check Internet Connection
- Respond to Internet On / Off Commands (acknowledges user requests, does not toggle internet)

### Wi-Fi Functions
- Toggle Wi-Fi (Action Center / Settings)
- Show Available Wi-Fi Networks (Action Center / Settings)

### Bluetooth Functions
- Toggle Bluetooth (Action Center / Settings)
- Show Paired Bluetooth Devices (Action Center / Settings)

### Airplane Mode
- Toggle Airplane Mode (Action Center / Settings)

### Power Modes & Display
- Toggle Battery Saver
- Toggle Night Light Mode (Action Center / Settings)
- Toggle Do Not Disturb Mode
- Toggle Nearby Sharing (Action Center / Settings)
- Toggle Hotspot
- Toggle Light / Dark Mode

### File and Window Operations
- Open Application
- Close Application
- Close Current Window
- Access System Settings (launch both general or specific settings pages)
- Create File

### Hardware Controls
- Increase / Decrease / Set Brightness
- Increase / Decrease Volume
- Mute / Unmute Volume

### Keyboard & Shortcut Control
- Simulate Individual Key Presses (e.g., F1-F12, media keys, arrows, etc.)
- Execute Voice-Triggered Keyboard Shortcuts:
  - Clipboard: Copy, Cut, Paste, Undo, Redo, Select All
  - Search/File: Find, Save, Print, New Tab, New Window
  - Window Management: Task View, Switch Apps, Show Desktop, Minimize/Maximize/Snap Windows
  - Formatting: Bold, Italic, Underline, Align Left/Center/Right
  - System: Open Start Menu, Run Dialog, Power User Menu, System Properties

### Search & Information
- Search on Windows
- Search in File Explorer
- Search on Web Platforms (Google, YouTube, Spotify, LinkedIn, Amazon, Twitter, GitHub, Wikipedia, Facebook, Instagram, Netflix, Bing)

### Camera & Media
- Take Photo
- Start Video Recording
- Scan Barcode
- Take Screenshot (Normal / Snipping Tool)
- Record Screen (Normal / Snipping Tool)
- Record Audio
- Play Songs on Spotify
- Play Videos on YouTube

### Location-Based Environment Info
- Get Current Temperature of a Location
- Get Current Weather Condition of a Location

## How to Use This Source Code

### Prerequisites
- Python 3.12.3 
- PyCharm (recommended IDE for development)

### 1. Clone the Repository:
   ```bash
   git clone https://github.com/SumithShetty1/sam-voice-assistant.git
  ```

### 2. Navigate to the Project Directory:
  ```bash
   cd sam-voice-assistant
  ```

### 3. Install the Required Python Packages:
  ```bash
   pip install -r requirements.txt
  ```

### 4. Run the Program:
You can run the project directly from PyCharm or by using the terminal.

## Installed Packages
- [Setuptools](https://pypi.org/project/setuptools/): A package development library for Python, enhancing the functionality of the built-in `distutils`. It simplifies the process of packaging and distributing Python projects.
  ```bash
  pip install setuptools
  ```
  
- [speech_recognition](https://pypi.org/project/SpeechRecognition/): A library for performing speech recognition with support for several engines and APIs.
  ```bash
  pip install SpeechRecognition
  ```
  
- [pyttsx3](https://pypi.org/project/pyttsx3/): A text-to-speech conversion library in Python.
  ```bash
  pip install pyttsx3
  ```
  
- [pyaudio](https://pypi.org/project/PyAudio/): Provides Python bindings for PortAudio, the cross-platform audio I/O library.
  ```bash
  pip install PyAudio
  ```
  
- [wikipedia](https://pypi.org/project/wikipedia/): A Python library that makes it easy to access and parse data from Wikipedia.
  ```bash
  pip install wikipedia
  ```
  
- [AppOpener](https://pypi.org/project/appopener/): A package for opening and closing applications programmatically.
  ```bash
  pip install AppOpener
  ```
  
- [pycaw](https://pypi.org/project/pycaw/): A Python library for manipulating audio devices in Windows.
  ```bash
  pip install pycaw
  ```
  
- [screen_brightness_control](https://pypi.org/project/screen-brightness-control/): A Python library for controlling screen brightness.
  ```bash
  pip install screen-brightness-control
  ```
  
- [pyautogui](https://pypi.org/project/PyAutoGUI/): A cross-platform GUI automation library for Python.
  ```bash
  pip install PyAutoGUI
  ```
  
- [pillow](https://pypi.org/project/Pillow/): A Python Imaging Library (PIL) fork for image processing.
  ```bash
  pip install Pillow
  ```
  
- [opencv-python](https://pypi.org/project/opencv-python/): A library for computer vision tasks.
  ```bash
  pip install opencv-python
  ```
  
- [darkdetect](https://pypi.org/project/darkdetect/): A package to detect system dark mode on macOS, Windows, and Linux with a dark GTK theme.
  ```bash
  pip install darkdetect
  ```
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/): A Python library for pulling data out of HTML and XML files.
  ```bash
  pip install beautifulsoup4
  ```
  
- [eel](https://pypi.org/project/eel/): A Python library for creating simple Electron-like desktop apps with Flask-like Python functions.
  ```bash
  pip install eel
  ```
  
- [TensorFlow](https://pypi.org/project/tensorflow/): TensorFlow is a popular Python library for machine learning and deep learning tasks. It can be installed using pip with the following command:
  ```bash
  pip install tensorflow
  ```
  
## Error
- import eel
  \Lib\site-packages\eel\__init__.py", line 16, in <module>
- import bottle.ext.websocket as wbs
  ModuleNotFoundError: No module named 'bottle.ext.websocket'

- If you ever get the above error then,
Fortunately, bottle-websocket can be used and should work the same.
I got mine working using Python 3.12.
You just have to change an import in __init__.py in the eel module.

- Find this import line:
  ```bash
  import bottle.ext.websocket as wbs

- and replace it with the one below:
  ```bash
  import bottle_websocket as wbs
  ```

## Disclaimer
This project is a personal/portfolio project created for educational and demonstration purposes. It is not affiliated with or endorsed by any existing company or product that may share a similar name.
