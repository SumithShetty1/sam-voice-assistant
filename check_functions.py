import requests
import darkdetect


# Function to check internet connectivity
def check_internet():
    try:
        requests.get('http://www.google.com', timeout=3)  # Attempt to make a request to Google
        return True
    except requests.ConnectionError:
        return False


# Function to check if the system is in dark mode
def check_dark_mode():
    theme = darkdetect.theme()
    if theme == 'Dark':
        return True
    else:
        return False
