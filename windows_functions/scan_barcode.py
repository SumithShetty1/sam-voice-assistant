import time
import pyautogui
from sam_functions.speak import speak
from sam_functions.listen import listen
from check_functions import check_camera_opening


# Function to initiate barcode scanning using the camera
def scan_barcode():
    try:
        pyautogui.hotkey('win')
        time.sleep(0.2)
        pyautogui.typewrite('Camera')
        time.sleep(0.2)
        pyautogui.press('enter')
        time.sleep(3)

        if check_camera_opening():
            # Camera app opening found, proceed with the operation
            pass
        else:
            # Camera app not found within 10 seconds, ask the user whether to continue waiting or exit
            speak("The camera app is taking longer than usual to open. Do you want to continue waiting boss?")

            while True:
                confirm = listen()
                if confirm == "":
                    continue
                if "yes" in confirm:
                    if not check_camera_opening():
                        speak(
                            "The camera app is still taking time to open. Please manually open the camera app.")
                        return
                else:
                    speak("Closing camera app boss")
                    pyautogui.hotkey('alt', 'f4')
                    return

        # Attempt to locate the photo icon
        try:
            pyautogui.locateCenterOnScreen("images/light_mode/camera/photo.png", confidence=0.9,
                                           grayscale=True)
            pyautogui.press('down')
            time.sleep(0.2)
        except pyautogui.ImageNotFoundException:
            pass

        # Attempt to locate the video icon
        try:
            pyautogui.locateCenterOnScreen("images/light_mode/camera/video.png", confidence=0.9,
                                           grayscale=True)
            pyautogui.press('down')
            time.sleep(0.2)
            pyautogui.press('down')
            time.sleep(0.2)
        except pyautogui.ImageNotFoundException:
            pass

        # Attempt to locate the barcode icon
        pyautogui.locateCenterOnScreen("images/light_mode/camera/barcode.png", confidence=0.9, grayscale=True)

        speak("Please show the barcode in front of the camera boss.")

    except Exception as e:
        speak("An error occurred")
        speak("Oops! Something went wrong while trying to scan the barcode boss.")
        pyautogui.hotkey('alt', 'f4')
