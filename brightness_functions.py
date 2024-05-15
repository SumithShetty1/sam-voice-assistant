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
        speak("Brightness is already at its maximum, boss")
    else:
        # Set the new brightness level
        sbc.set_brightness(new_brightness)
        speak("Brightness increased, boss")


# Function to decrease brightness
def decrease_brightness(step):
    # Get the current brightness level
    current_brightness = sbc.get_brightness()[0]  # Access the first brightness level
    min_brightness = 0  # Minimum brightness level
    new_brightness = max(current_brightness - step, min_brightness)
    # Check if the brightness is already at its minimum
    if new_brightness == current_brightness:
        speak("Brightness is already at its minimum, boss")
    else:
        # Set the new brightness level
        sbc.set_brightness(new_brightness)
        speak("Brightness decreased, boss")


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
        speak("Brightness is already at the desired level, boss")
    else:
        # Set the new brightness level
        sbc.set_brightness(new_brightness)
        speak("Brightness set to {}%, boss".format(new_brightness))
