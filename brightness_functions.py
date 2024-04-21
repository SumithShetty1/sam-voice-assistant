from sam_functions.speak import speak
import screen_brightness_control as sbc


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


# Function to set brightness to a specific level
def set_brightness(level):
    max_brightness = 100  # Maximum brightness level
    min_brightness = 0  # Minimum brightness level

    # Ensure the brightness level is within the valid range
    new_brightness = max(min(level, max_brightness), min_brightness)

    # Get the current brightness level
    current_brightness = sbc.get_brightness()[0]  # Access the first brightness level

    # Check if the brightness is already at the desired level
    if new_brightness == current_brightness:
        print("Sam: Brightness is already at the desired level, sir")
        speak("Brightness is already at the desired level sir")
    else:
        # Set the new brightness level
        sbc.set_brightness(new_brightness)
        print("Sam: Brightness set to {}%, sir".format(new_brightness))
        speak("Brightness set to {} percent sir".format(new_brightness))
