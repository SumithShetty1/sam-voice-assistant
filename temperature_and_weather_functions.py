import requests
from bs4 import BeautifulSoup
from sam_functions.speak import speak


def temperature(query):
    try:
        # Extracting the location from the query string
        location = query.split("temperature in ")[1]

        # Constructing the search URL
        url = f"https://www.google.com/search?q=temperature+in+{location}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text

        print(f"Current temperature in {location} is {temp}, sir")
        speak(f"Current temperature in {location} is {temp} sir")
    except Exception as e:
        print("Sam: Sorry, I couldn't fetch the temperature information at the moment.")
        speak("Sorry I couldn't fetch the temperature information at the moment.")


def weather(query):
    try:
        # Extracting the location from the query string
        location = query.split("weather in ")[1]

        # Constructing the search URL
        url = f"https://www.google.com/search?q=weather+in+{location}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        weather_condition = data.find("div", class_="BNeawe tAd8D AP7Wnd").text

        # Remove time information from weather_condition
        weather_condition = weather_condition.split("\n")[1]

        print(f"Current weather in {location} is {weather_condition}, sir")
        speak(f"Current weather in {location} is {weather_condition} sir")
    except Exception as e:
        print("Sam: Sorry, I couldn't fetch the weather information at the moment.")
        speak("Sorry I couldn't fetch the weather information at the moment.")
