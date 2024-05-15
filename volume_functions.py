from sam_functions.speak import speak
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


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
        speak("Volume is already at its maximum boss")
    else:
        # Set the master volume level to the new volume
        volume.SetMasterVolumeLevel(new_volume, None)
        speak("Volume increased boss")


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
        speak('Volume is already at its minimum boss')
    else:
        # Set the master volume level to the new volume
        volume.SetMasterVolumeLevel(new_volume, None)
        speak("Volume decreased boss")


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
        speak("Volume muted boss")
    else:
        speak("Volume is already muted boss")


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
        speak("Volume unmuted boss")
    else:
        speak("Volume is already unmuted boss")