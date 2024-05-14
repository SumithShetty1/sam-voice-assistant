import requests
from bs4 import BeautifulSoup
from sam_functions.speak import speak


def temperature(query):
    try:
        # Extracting the location from the query string
        location = query.split("temperature in ")[1]

        if location:
            # Constructing the search URL with the specified location
            url = f"https://www.google.com/search?q=temperature+{location}"

            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text

            if "°C" in temp:
                speak(f"Current temperature in {location} is {temp}, boss")
            else:
                speak("Sam: Please specify a location, boss.")
        else:
            speak("Sam: Please specify a location, boss.")

    except Exception as e:
        speak("Sam: Sorry, I couldn't fetch the temperature information at the moment.")


def weather(query):
    try:
        # Extracting the location from the query string
        location = query.split("weather in ")[1]

        if location:
            # Constructing the search URL
            url = f"https://www.google.com/search?q=weather+{location}"

            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")

            try:
                weather_condition = data.find("div", class_="BNeawe tAd8D AP7Wnd").text
            except Exception as e:
                speak("Sam: Please specify a location, boss.")
                return

            # Remove time information from weather_condition
            weather_condition = weather_condition.split("\n")[1]

            speak(f"Current weather in {location} is {weather_condition}, boss")
        else:
            speak("Sam: Please specify a location, boss.")

    except Exception as e:
        speak("Sam: Sorry, I couldn't fetch the weather information at the moment.")
