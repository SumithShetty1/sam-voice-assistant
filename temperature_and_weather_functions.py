import requests
from bs4 import BeautifulSoup
from sam_functions.speak import speak


def temperature(query, intent_data):
    try:
        # Initialize location as None
        location = None

        # Loop through each preposition pattern
        for prep in intent_data['text']:
            if prep in query:
                # Extract location from the query based on the preposition
                location = query.split(prep)[1].strip()
                break

        if location:
            # Constructing the search URL with the specified location
            url = f"https://www.google.com/search?q=temperature+{location}"

            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe iBp4i AP7Wnd").text
            if "°C" in temp:
                speak(f"Current temperature in {location} is {temp} sir")
            else:
                speak("Please specify a location sir.")
        else:
            speak("Please specify a location sir.")

    except Exception as e:
        speak("Sorry, I couldn't fetch the temperature information at the moment.")


def weather(query, intent_data):
    try:
        # Initialize location as None
        location = None

        # Loop through each preposition pattern
        for prep in intent_data['text']:
            if prep in query:
                # Extract location from the query based on the preposition
                location = query.split(prep)[1].strip()
                break

        if location:
            # Constructing the search URL
            url = f"https://www.google.com/search?q=weather+{location}"

            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")

            try:
                weather_condition = data.find("div", class_="BNeawe tAd8D AP7Wnd").text
            except Exception as e:
                speak("Please specify a location sir.")
                return

            # Remove time information from weather_condition
            weather_condition = weather_condition.split("\n")[1]

            speak(f"Current weather in {location} is {weather_condition} sir")
        else:
            speak("Please specify a location sir.")

    except Exception as e:
        speak("Sorry, I couldn't fetch the weather information at the moment.")
