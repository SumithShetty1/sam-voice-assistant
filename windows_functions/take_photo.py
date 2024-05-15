import time
import pyautogui
import cv2
import os
from sam_functions.speak import speak
from sam_functions.listen import listen
from check_functions import check_camera_opening


# Function to create a directory if it doesn't exist
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


# Function to take a photo using the camera app
def take_photo_in_camera():
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
            speak("The camera app is taking longer than usual to open. Do you want to continue waiting, boss?")

            while True:
                confirm = listen()
                if confirm == "":
                    continue
                if "yes" in confirm:
                    if not check_camera_opening():
                        speak("The camera app is still taking time to open. Please manually open the camera app.")
                        return
                else:
                    speak("Closing camera app, boss")
                    pyautogui.hotkey('alt', 'f4')
                    return

        # Attempt to locate the video icon
        try:
            pyautogui.locateCenterOnScreen("images/light_mode/camera/video.png", confidence=0.9, grayscale=True)
            pyautogui.press('down')
            time.sleep(0.2)
        except pyautogui.ImageNotFoundException:
            pass

        # Attempt to locate the barcode icon
        try:
            pyautogui.locateCenterOnScreen("images/light_mode/camera/barcode.png", confidence=0.9,
                                           grayscale=True)
            pyautogui.press('up')
            time.sleep(0.2)
        except pyautogui.ImageNotFoundException:
            pass

        # Attempt to locate the photo icon
        pyautogui.locateCenterOnScreen("images/light_mode/camera/photo.png", confidence=0.9, grayscale=True)

        # Prompt user that photo will be taken after 3 seconds
        speak("I'll capture a photo in 3 seconds, boss.")
        time.sleep(3)
        pyautogui.press('enter')
        time.sleep(1)
        speak(f"Photo has been taken, boss.")
    except Exception as e:
        speak("An error occurred")
        speak("Oops! Something went wrong while trying to capture the photo, boss.")
        pyautogui.hotkey('alt', 'f4')


# Function to take a photo using the webcam
def take_photo(query):
    try:
        if "in camera" in query:
            take_photo_in_camera()
            return

        # Extract file name from query if mentioned
        file_name = "photo.jpg"
        if "name it as" in query or "save it as" in query:
            name_query = query.split("name it as ")[1] if "name it as" in query else query.split("save it as ")[1]
            file_name = name_query.split()[0] + ".jpg"

        # Define the base directory for the camera roll
        base_directory = os.path.join(os.path.expanduser("~"), "Documents", "Sam Virtual Assistant", "Pictures",
                                      "Camera Roll")

        # Create the base directory if it doesn't exist
        create_directory(base_directory)

        # Construct the full file path
        file_path = os.path.join(base_directory, file_name)

        # Check if the file already exists
        count = 1
        while os.path.exists(file_path):
            # Append a number to the filename
            file_name = f"photo ({count}).jpg"
            file_path = os.path.join(base_directory, file_name)
            count += 1

        camera_index = 0

        # Open the camera
        cap = cv2.VideoCapture(camera_index)

        # Check if the camera is opened successfully
        if not cap.isOpened():
            speak("Sorry, I couldn't open the camera, boss.")
            return

        # Prompt user that photo will be taken after 3 seconds
        speak("I'll capture a photo in 3 seconds, boss.")

        # Create a window to display the live feed from the webcam
        cv2.namedWindow("Live Feed", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Live Feed", 800, 600)

        start_time = time.time()
        while time.time() - start_time < 3:
            # Capture a frame
            ret, frame = cap.read()

            if ret:
                # Display the frame in the window
                cv2.imshow("Live Feed", frame)

            # Check for user input to break the loop and capture the photo
            if cv2.waitKey(1) == ord('\n'):
                break

        # Capture a frame
        ret, frame = cap.read()

        if ret:
            # Save the captured frame as an img
            cv2.imwrite(file_path, frame)
            speak(f"Photo has been taken and saved as {file_name}, boss.")

        # Release the camera
        cap.release()
        cv2.destroyAllWindows()

    except Exception as e:
        speak("An error occurred")
        speak("Oops! Something went wrong while trying to capture the photo, boss.")
