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

## Getting Started
To get a local copy up and running, follow these steps:

**1. Clone the repository:**
   ```bash
   git clone https://github.com/SumithShetty1/sam-voice-assistant.git
   ```
**2. Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```
**3. Run the program**

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
