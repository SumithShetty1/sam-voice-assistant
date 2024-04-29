import datetime
from sam_functions.speak import speak


# Function to tell date and time
def tell_time_and_date(query):
    try:
        # Get current date and time
        now = datetime.datetime.now()

        # Calculate yesterday, day before yesterday, tomorrow, and day after tomorrow
        yesterday = now - datetime.timedelta(days=1)
        day_before_yesterday = now - datetime.timedelta(days=2)
        tomorrow = now + datetime.timedelta(days=1)
        day_after_tomorrow = now + datetime.timedelta(days=2)

        if "day before yesterday" in query:
            # Format and speak the day before yesterday's date
            day_before_yesterday_date = day_before_yesterday.strftime("%A, %B %d, %Y")
            print(f"Sam: The day before yesterday was {day_before_yesterday_date}, sir.")
            speak(f"The day before yesterday was {day_before_yesterday_date} sir")

        elif "yesterday" in query:
            # Format and speak yesterday's date
            yesterday_date = yesterday.strftime("%A, %B %d, %Y")
            print(f"Sam: Yesterday was {yesterday_date}, sir.")
            speak(f"Yesterday was {yesterday_date} sir")

        elif "yesterday" in query and "day" in query:
            # Format and speak yesterday's day
            yesterday_day = yesterday.strftime("%A")
            print(f"Sam: Yesterday was {yesterday_day}, sir.")
            speak(f"Yesterday was {yesterday_day} sir")

        elif "yesterday" in query and "month" in query:
            # Format and speak yesterday's month
            yesterday_month = yesterday.strftime("%B")
            print(f"Sam: Yesterday was in the month of {yesterday_month}, sir.")
            speak(f"Yesterday was in the month of {yesterday_month} sir")

        elif "yesterday" in query and "year" in query:
            # Format and speak yesterday's year
            yesterday_year = yesterday.strftime("%Y")
            print(f"Sam: Yesterday was in the year {yesterday_year}, sir.")
            speak(f"Yesterday was in the year {yesterday_year} sir")

        elif "day after tomorrow" in query:
            # Format and speak the day after tomorrow's date
            day_after_tomorrow_date = day_after_tomorrow.strftime("%A, %B %d, %Y")
            print(f"Sam: The day after tomorrow will be {day_after_tomorrow_date}, sir.")
            speak(f"The day after tomorrow will be {day_after_tomorrow_date} sir")

        elif "tomorrow" in query:
            # Format and speak tomorrow's date
            tomorrow_date = tomorrow.strftime("%A, %B %d, %Y")
            print(f"Sam: Tomorrow will be {tomorrow_date}, sir.")
            speak(f"Tomorrow will be {tomorrow_date} sir")

        elif "tomorrow" in query and "day" in query:
            # Format and speak tomorrow's day
            tomorrow_day = tomorrow.strftime("%A")
            print(f"Sam: Tomorrow will be {tomorrow_day}, sir.")
            speak(f"Tomorrow will be {tomorrow_day} sir")

        elif "tomorrow" in query and "month" in query:
            # Format and speak tomorrow's month
            tomorrow_month = tomorrow.strftime("%B")
            print(f"Sam: Tomorrow will be in the month of {tomorrow_month}, sir.")
            speak(f"Tomorrow will be in the month of {tomorrow_month} sir")

        elif "tomorrow" in query and "year" in query:
            # Format and speak tomorrow's year
            tomorrow_year = tomorrow.strftime("%Y")
            print(f"Sam: Tomorrow will be in the year {tomorrow_year}, sir.")
            speak(f"Tomorrow will be in the year {tomorrow_year} sir")

        # Check if the query contains "time", "date", or both
        elif "time" in query and "date" in query:
            # Format the date and time
            current_date = now.strftime("%A, %B %d, %Y")
            current_time = now.strftime("%I:%M %p")

            # Speak both time and date
            print(f"Sam: Today is {current_date}. The time is {current_time}, sir.")
            speak(f"Today is {current_date}. The time is {current_time} sir")

        elif "time" in query and "day" in query:
            # Format and speak the current time and day
            current_time = now.strftime("%I:%M %p")
            current_day = now.strftime("%A")
            print(f"Sam: The time is {current_time} and today is {current_day}, sir.")
            speak(f"The time is {current_time} and today is {current_day} sir")

        elif "time" in query and "month" in query:
            # Format and speak the current time and month
            current_time = now.strftime("%I:%M %p")
            current_month = now.strftime("%B")
            print(f"Sam: The time is {current_time} and we are in the month of {current_month}, sir.")
            speak(f"The time is {current_time} and we are in the month of {current_month} sir")

        elif "time" in query and "year" in query:
            # Format and speak the current time and year
            current_time = now.strftime("%I:%M %p")
            current_year = now.strftime("%Y")
            print(f"Sam: The time is {current_time} and the current year is {current_year}, sir.")
            speak(f"The time is {current_time} and the current year is {current_year} sir")

        elif "time" in query:
            # Format and speak the current time
            current_time = now.strftime("%I:%M %p")
            print(f"Sam: The time is {current_time}, sir.")
            speak(f"The time is {current_time} sir")

        elif "hour" in query and "day" in query:
            # Format and speak the current hour and day
            current_hour = now.strftime("%I %p").lstrip('0').replace(' 0', ' ')
            current_day = now.strftime("%A")
            print(f"Sam: The current hour is {current_hour} and today is {current_day}, sir.")
            speak(f"The current hour is {current_hour} and today is {current_day} sir")

        elif "hour" in query and "month" in query:
            # Format and speak the current hour and month
            current_hour = now.strftime("%I %p").lstrip('0').replace(' 0', ' ')
            current_month = now.strftime("%B")
            print(f"Sam: The current hour is {current_hour} and we are in the month of {current_month}, sir.")
            speak(f"The current hour is {current_hour} and we are in the month of {current_month} sir")

        elif "hour" in query and "year" in query:
            # Format and speak the current hour and year
            current_hour = now.strftime("%I %p").lstrip('0').replace(' 0', ' ')
            current_year = now.strftime("%Y")
            print(f"Sam: The current hour is {current_hour} and the current year is {current_year}, sir.")
            speak(f"The current hour is {current_hour} and the current year is {current_year} sir")

        elif "hour" in query:
            # Format and speak the current hour
            current_hour = now.strftime("%I %p").lstrip('0').replace(' 0', ' ')
            print(f"Sam: The current hour is {current_hour}, sir.")
            speak(f"The current hour is {current_hour} sir")

        elif "date" in query:
            # Format and speak the current date
            current_date = now.strftime("%A, %B %d, %Y")
            print(f"Sam: Today is {current_date}, sir.")
            speak(f"Today is {current_date} sir")

        elif "day" in query:
            # Format and speak the current day
            current_day = now.strftime("%A")
            print(f"Sam: Today is {current_day}, sir.")
            speak(f"Today is {current_day} sir")

        elif "month" in query:
            # Format and speak the current month
            current_month = now.strftime("%B")
            print(f"Sam: We are in the month of {current_month}, sir.")
            speak(f"We are in the month of {current_month} sir")

        elif "year" in query:
            # Format and speak the current year
            current_year = now.strftime("%Y")
            print(f"Sam: The current year is {current_year}, sir.")
            speak(f"The current year is {current_year} sir")

    except Exception as e:
        print(f"Sam: An error occurred: {e}")
        print("Sam: Oops! Something went wrong while trying to get the time and date.")
        speak("Oops! Something went wrong while trying to get the time and date.")
