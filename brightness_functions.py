from sam_functions import speak
import screen_brightness_control as sbc  # https://pypi.org/project/screen-brightness-control/


# Function to increase brightness
def increase_brightness(step):
    # Get the current brightness level
    current_brightness = sbc.get_brightness()[0]  # Access the first brightness level
    max_brightness = 100  # Maximum brightness level
    new_brightness = min(current_brightness + step, max_brightness)
    # Check if the brightness is already at its maximum
    if new_brightness == current_brightness:
        print("Sam: Brightness is already at its maximum, sir")
        speak("Brightness is already at its maximum sir")
    else:
        # Set the new brightness level
        sbc.set_brightness(new_brightness)
        print("Sam: Brightness increased, sir")
        speak("Brightness increased sir")


# Function to decrease brightness
def decrease_brightness(step):
    # Get the current brightness level
    current_brightness = sbc.get_brightness()[0]  # Access the first brightness level
    min_brightness = 0  # Minimum brightness level
    new_brightness = max(current_brightness - step, min_brightness)
    # Check if the brightness is already at its minimum
    if new_brightness == current_brightness:
        print("Sam: Brightness is already at its minimum, sir")
        speak("Brightness is already at its minimum sir")
    else:
        # Set the new brightness level
        sbc.set_brightness(new_brightness)
        print("Sam: Brightness decreased, sir")
        speak("Brightness decreased sir")
