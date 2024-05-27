from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL, COMError
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from sam_functions.speak import speak
import eel


def get_audio_interface():
    devices = AudioUtilities.GetSpeakers()  # Get the speakers' devices
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL,
                                 None)  # Activate the interface for the audio endpoint volume
    return cast(interface, POINTER(IAudioEndpointVolume))  # Cast the interface to an audio endpoint volume pointer


def volume_up(step):
    try:
        volume = get_audio_interface()
        current_volume = volume.GetMasterVolumeLevel()
        max_volume = 0
        new_volume = min(current_volume + step, max_volume)
        if new_volume == current_volume:
            speak("Volume is already at its maximum sir")
        else:
            volume.SetMasterVolumeLevel(new_volume, None)
            speak("Volume increased sir")
    except COMError as e:
        speak(f"Failed to increase volume")


def volume_down(step):
    try:
        volume = get_audio_interface()
        current_volume = volume.GetMasterVolumeLevel()
        min_volume = -65.25
        new_volume = max(current_volume - step, min_volume)
        if abs(new_volume - current_volume) < 0.01:
            speak("Volume is already at its minimum sir")
        else:
            volume.SetMasterVolumeLevel(new_volume, None)
            speak("Volume decreased sir")
    except COMError as e:
        speak(f"Failed to decrease volume")


def mute_volume():
    try:
        volume = get_audio_interface()
        is_muted = volume.GetMute()
        if not is_muted:
            volume.SetMute(1, None)
            eel.DisplayMessage("Volume muted sir")
            eel.receiverText("Volume muted sir")
        else:
            eel.DisplayMessage("Volume is already muted sir")
            eel.receiverText("Volume is already muted sir")
    except COMError as e:
        eel.DisplayMessage("Failed to mute volume")
        eel.receiverText("Failed to mute volume")


def unmute_volume():
    try:
        volume = get_audio_interface()
        is_muted = volume.GetMute()
        if is_muted:
            volume.SetMute(0, None)
            speak("Volume unmuted sir")
        else:
            speak("Volume is already unmuted sir")
    except COMError as e:
        speak(f"Failed to unmute volume")
