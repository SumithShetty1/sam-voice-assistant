import pyttsx3
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume  # https://pypi.org/project/pycaw/
import screen_brightness_control as sbc  # https://pypi.org/project/screen-brightness-control/
from AppOpener import open, close  # https://pypi.org/project/appopener/


# Function to convert text to speech
def speak(audio):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    # Speak the provided audio
    engine.say(audio)
    # Blocks while processing all the currently queued commands
    engine.runAndWait()


# Function to open applications
def open_application(app_name):
    try:
        open(app_name, throw_error=True, match_closest=True)
        print(f"Sam: Opening {app_name} sir.")
        speak(f"Opening {app_name} sir.")
    except Exception as e:
        print(e)
        print(f"Sam: Sorry, I couldn't find an application named {app_name}.")
        speak(f"Sorry, I couldn't find an application named {app_name}.")


def close_application(app_name):
    try:
        close(app_name, throw_error=True, match_closest=False)
        print(f"Sam: Closed {app_name} sir")
        speak(f"Closed {app_name} sir")
    except Exception as e:
        print(e)
        print(f"Sam: Sorry, I couldn't find an application named {app_name}.")
        speak(f"Sorry, I couldn't find an application named {app_name}.")


# Function to increase volume
def volume_up(step):
    devices = AudioUtilities.GetSpeakers()  # Get the speakers' devices
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)  # Activate the interface for the audio endpoint volume
    volume = cast(interface, POINTER(IAudioEndpointVolume))  # Cast the interface to an audio endpoint volume pointer
    current_volume = volume.GetMasterVolumeLevel()  # Get the current master volume level
    max_volume = 0
    new_volume = min(current_volume + step, max_volume)
    # Check if the new volume is equal to the current volume
    if new_volume == current_volume:
        # Print and speak a message indicating that the volume is already at its maximum
        print("Sam: Volume is already at its maximum.")
        speak("Volume is already at its maximum.")
    else:
        # Set the master volume level to the new volume
        volume.SetMasterVolumeLevel(new_volume, None)
        print("Sam: Volume increased.")
        speak("Volume increased.")


# Function to decrease volume
def volume_down(step):
    devices = AudioUtilities.GetSpeakers()  # Get the speakers' devices
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)  # Activate the interface for the audio endpoint volume
    volume = cast(interface, POINTER(IAudioEndpointVolume))  # Cast the interface to an audio endpoint volume pointer
    current_volume = volume.GetMasterVolumeLevel()
    min_volume = -65.25
    new_volume = max(current_volume - step, min_volume)
    # Check if the absolute difference between the new volume and the current volume is very small
    if abs(new_volume - current_volume) < 0.01:  # Using a tolerance threshold for comparison
        print('Sam: Volume is already at its minimum.')
    else:
        # Set the master volume level to the new volume
        volume.SetMasterVolumeLevel(new_volume, None)
        print("Sam: Volume decreased.")
        speak("Volume decreased.")


# Function to mute volume
def mute_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    # Get the current mute status
    is_muted = volume.GetMute()
    # Check if volume is not already muted
    if not is_muted:
        # Mute volume
        volume.SetMute(1, None)
        print("Sam: Volume muted.")
        speak("Volume muted.")
    else:
        print("Sam: Volume is already muted.")
        speak("Volume is already muted.")


# Function to unmute volume
def unmute_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    # Get the current mute status
    is_muted = volume.GetMute()
    # Check if volume is currently muted
    if is_muted:
        # Unmute volume
        volume.SetMute(0, None)
        print("Sam: Volume unmuted.")
        speak("Volume unmuted.")
    else:
        print("Sam: Volume is already unmuted.")
        speak("Volume is already unmuted.")


# Function to increase brightness
def increase_brightness(step):
    # Get the current brightness level
    current_brightness = sbc.get_brightness()[0]  # Access the first brightness level
    max_brightness = 100  # Maximum brightness level
    new_brightness = min(current_brightness + step, max_brightness)
    # Check if the brightness is already at its maximum
    if new_brightness == current_brightness:
        print("Sam: Brightness is already at its maximum.")
        speak("Brightness is already at its maximum.")
    else:
        # Set the new brightness level
        sbc.set_brightness(new_brightness)
        print("Sam: Brightness increased.")
        speak("Brightness increased.")


# Function to decrease brightness
def decrease_brightness(step):
    # Get the current brightness level
    current_brightness = sbc.get_brightness()[0]  # Access the first brightness level
    min_brightness = 0  # Minimum brightness level
    new_brightness = max(current_brightness - step, min_brightness)
    # Check if the brightness is already at its minimum
    if new_brightness == current_brightness:
        print("Sam: Brightness is already at its minimum.")
        speak("Brightness is already at its minimum.")
    else:
        # Set the new brightness level
        sbc.set_brightness(new_brightness)
        print("Sam: Brightness decreased.")
        speak("Brightness decreased.")
