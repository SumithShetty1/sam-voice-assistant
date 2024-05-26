from sam_functions.speak import speak
import webbrowser
import pyautogui
from search_bar import search_bar
import time


def search(query, intent_data):
    try:
        if intent_data['intent'] == "search_google":
            # Remove the specific phrases and clean up the query
            search_query = ""

            for prep in intent_data['text']:
                if prep in query:
                    # Extract search query from the query based on the preposition
                    parts = query.split(prep)
                    if len(parts) > 1:
                        search_query = parts[1].strip()
                    break

            search_url = f"https://www.google.com/search?q={search_query}"
            speak(f"Searching the web for {search_query} sir.")
            webbrowser.open(search_url)

        elif intent_data['intent'] == "search_youtube":
            # Remove the specific phrases and clean up the query
            search_query = ""

            for prep in intent_data['text']:
                if prep in query:
                    # Extract search query from the query based on the preposition
                    parts = query.split(prep)
                    if len(parts) > 1:
                        search_query = parts[1].strip()
                    break

            search_url = f"https://www.youtube.com/results?search_query={search_query}"
            speak(f"Searching YouTube for {search_query} sir.")
            webbrowser.open(search_url)

        elif intent_data['intent'] == "search_spotify":
            # Remove the specific phrases and clean up the query
            search_query = ""

            for prep in intent_data['text']:
                if prep in query:
                    # Extract search query from the query based on the preposition
                    parts = query.split(prep)
                    if len(parts) > 1:
                        search_query = parts[1].strip()
                    break

            search_url = f"https://open.spotify.com/search/{search_query}"
            speak(f"Searching Spotify for {search_query} sir.")
            webbrowser.open(search_url)

        elif intent_data['intent'] == "search_linkedin":
            # Remove the specific phrases and clean up the query
            search_query = ""

            for prep in intent_data['text']:
                if prep in query:
                    # Extract search query from the query based on the preposition
                    parts = query.split(prep)
                    if len(parts) > 1:
                        search_query = parts[1].strip()
                    break

            search_url = f"https://www.linkedin.com/search/results/all/?keywords={search_query}"
            speak(f"Searching LinkedIn for {search_query} sir.")
            webbrowser.open(search_url)

        elif intent_data['intent'] == "search_amazon":
            # Remove the specific phrases and clean up the query
            search_query = ""

            for prep in intent_data['text']:
                if prep in query:
                    # Extract search query from the query based on the preposition
                    parts = query.split(prep)
                    if len(parts) > 1:
                        search_query = parts[1].strip()
                    break

            search_url = f"https://www.amazon.in/s?k={search_query}"
            speak(f"Searching Amazon for {search_query} sir.")
            webbrowser.open(search_url)

        elif intent_data['intent'] == "search_twitter":
            # Remove the specific phrases and clean up the query
            search_query = ""

            for prep in intent_data['text']:
                if prep in query:
                    # Extract search query from the query based on the preposition
                    parts = query.split(prep)
                    if len(parts) > 1:
                        search_query = parts[1].strip()
                    break

            search_url = f"https://twitter.com/search?q={search_query}"
            speak(f"Searching Twitter for {search_query} sir.")
            webbrowser.open(search_url)

        elif intent_data['intent'] == "search_github":
            # Remove the specific phrases and clean up the query
            search_query = ""

            for prep in intent_data['text']:
                if prep in query:
                    # Extract search query from the query based on the preposition
                    parts = query.split(prep)
                    if len(parts) > 1:
                        search_query = parts[1].strip()
                    break

            search_url = f"https://github.com/search?q={search_query}"
            speak(f"Searching GitHub for {search_query} sir.")
            webbrowser.open(search_url)

        elif intent_data['intent'] == "search_wikipedia":
            # Remove the specific phrases and clean up the query
            search_query = ""

            for prep in intent_data['text']:
                if prep in query:
                    # Extract search query from the query based on the preposition
                    parts = query.split(prep)
                    if len(parts) > 1:
                        search_query = parts[1].strip()
                    break

            search_url = f"https://en.wikipedia.org/wiki/{search_query}"
            speak(f"Searching Wikipedia for {search_query} sir.")
            webbrowser.open(search_url)

        elif intent_data['intent'] == "search_facebook":
            # Remove the specific phrases and clean up the query
            search_query = ""

            for prep in intent_data['text']:
                if prep in query:
                    # Extract search query from the query based on the preposition
                    parts = query.split(prep)
                    if len(parts) > 1:
                        search_query = parts[1].strip()
                    break

            search_url = f"https://www.facebook.com/search/top/?q={search_query}"
            speak(f"Searching Facebook for {search_query} sir.")
            webbrowser.open(search_url)

        elif intent_data['intent'] == "search_instagram":
            # Remove the specific phrases and clean up the query
            search_query = ""

            for prep in intent_data['text']:
                if prep in query:
                    # Extract search query from the query based on the preposition
                    parts = query.split(prep)
                    if len(parts) > 1:
                        search_query = parts[1].strip()
                    break

            search_url = f"https://www.instagram.com/explore/tags/{search_query}"
            speak(f"Searching Instagram for {search_query} sir.")
            webbrowser.open(search_url)

        elif intent_data['intent'] == "search_netflix":
            # Remove the specific phrases and clean up the query
            search_query = ""

            for prep in intent_data['text']:
                if prep in query:
                    # Extract search query from the query based on the preposition
                    parts = query.split(prep)
                    if len(parts) > 1:
                        search_query = parts[1].strip()
                    break

            search_url = f"https://www.netflix.com/search?q={search_query}"
            speak(f"Searching Netflix for {search_query} sir.")
            webbrowser.open(search_url)

        elif intent_data['intent'] == "search_bing":
            pyautogui.press("win")
            # Type "edge" to search for Microsoft Edge
            pyautogui.write("edge")
            # Press Enter to open Microsoft Edge
            pyautogui.press("enter")
            # Wait for Edge to open
            pyautogui.sleep(2)

            # Type the Bing search URL in the address bar
            # Remove the specific phrases and clean up the query
            search_query = ""

            for prep in intent_data['text']:
                if prep in query:
                    # Extract search query from the query based on the preposition
                    parts = query.split(prep)
                    if len(parts) > 1:
                        search_query = parts[1].strip()
                    break

            search_url = f"https://www.bing.com/search?q={search_query}"
            pyautogui.write(search_url)
            pyautogui.press("enter")

            # Display assistant's message
            speak(f"Searching Bing for {search_query} sir")

        elif intent_data['intent'] == "search_file_explorer":
            pyautogui.hotkey("win", 'e')
            time.sleep(2)

            # Type the Bing search URL in the address bar
            # Remove the specific phrases and clean up the query
            search_query = ""

            for prep in intent_data['text']:
                if prep in query:
                    # Extract search query from the query based on the preposition
                    parts = query.split(prep)
                    if len(parts) > 1:
                        search_query = parts[1].strip()
                    break

            # Press Ctrl + F to focus on the search
            pyautogui.hotkey("ctrl", "f")
            time.sleep(1)  # Add a short delay to ensure the search box opens

            # Type the search query
            pyautogui.write(search_query)
            pyautogui.press("enter")

            # Display assistant's message
            speak(f"Searching for {search_query} sir")

        else:
            search_bar(query, intent_data)

    except IndexError:
        speak("Please specify the search query sir")
    except Exception as e:
        speak("Error performing search")
        speak("Sorry, I couldn't perform the search sir")
