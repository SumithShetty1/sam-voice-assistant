import datetime
from sam_functions.speak import speak


# Function to tell date and time
def tell_time_and_date(intent_data):
    try:
        # Get current date and time
        now = datetime.datetime.now()

        # Calculate yesterday, day before yesterday, tomorrow, and day after tomorrow
        yesterday = now - datetime.timedelta(days=1)
        day_before_yesterday = now - datetime.timedelta(days=2)
        tomorrow = now + datetime.timedelta(days=1)
        day_after_tomorrow = now + datetime.timedelta(days=2)

        if intent_data['intent'] == "day_before_yesterday":
            # Format and speak the day before yesterday's date
            day_before_yesterday_date = day_before_yesterday.strftime("%A, %B %d, %Y")
            speak(f"The day before yesterday was {day_before_yesterday_date} sir.")

        elif intent_data['intent'] == "yesterday_date":
            # Format and speak yesterday's date
            yesterday_date = yesterday.strftime("%A, %B %d, %Y")
            speak(f"Yesterday was {yesterday_date} sir.")

        elif intent_data['intent'] == "yesterday_day":
            # Format and speak yesterday's day
            yesterday_day = yesterday.strftime("%A")
            speak(f"Yesterday was {yesterday_day} sir.")

        elif intent_data['intent'] == "yesterday_month":
            # Format and speak yesterday's month
            yesterday_month = yesterday.strftime("%B")
            speak(f"Yesterday was in the month of {yesterday_month} sir.")

        elif intent_data['intent'] == "yesterday_year":
            # Format and speak yesterday's year
            yesterday_year = yesterday.strftime("%Y")
            speak(f"Yesterday was in the year {yesterday_year} sir.")

        elif intent_data['intent'] == "day_after_tomorrow_date":
            # Format and speak the day after tomorrow's date
            day_after_tomorrow_date = day_after_tomorrow.strftime("%A, %B %d, %Y")
            speak(f"The day after tomorrow will be {day_after_tomorrow_date} sir.")

        elif intent_data['intent'] == "tomorrow_date":
            # Format and speak tomorrow's date
            tomorrow_date = tomorrow.strftime("%A, %B %d, %Y")
            speak(f"Tomorrow will be {tomorrow_date} sir.")

        elif intent_data['intent'] == "tomorrow_day":
            # Format and speak tomorrow's day
            tomorrow_day = tomorrow.strftime("%A")
            speak(f"Tomorrow will be {tomorrow_day} sir.")

        elif intent_data['intent'] == "tomorrow_month":
            # Format and speak tomorrow's month
            tomorrow_month = tomorrow.strftime("%B")
            speak(f"Tomorrow will be in the month of {tomorrow_month} sir.")

        elif intent_data['intent'] == "tomorrow_year":
            # Format and speak tomorrow's year
            tomorrow_year = tomorrow.strftime("%Y")
            speak(f"Tomorrow will be in the year {tomorrow_year} sir.")

        # Check if the query contains "time", "date", or both
        elif intent_data['intent'] == "time_and_date":
            # Format the date and time
            current_date = now.strftime("%A, %B %d, %Y")
            current_time = now.strftime("%I:%M %p")

            # Speak both time and date
            speak(f"Today is {current_date}. The time is {current_time} sir.")

        elif intent_data['intent'] == "time_and_day":
            # Format and speak the current time and day
            current_time = now.strftime("%I:%M %p")
            current_day = now.strftime("%A")
            speak(f"The time is {current_time} and today is {current_day} sir.")

        elif intent_data['intent'] == "time_and_month":
            # Format and speak the current time and month
            current_time = now.strftime("%I:%M %p")
            current_month = now.strftime("%B")
            speak(f"The time is {current_time} and we are in the month of {current_month} sir.")

        elif intent_data['intent'] == "time_and_year":
            # Format and speak the current time and year
            current_time = now.strftime("%I:%M %p")
            current_year = now.strftime("%Y")
            speak(f"The time is {current_time} and the current year is {current_year} sir.")

        elif intent_data['intent'] == "current_time":
            # Format and speak the current time
            current_time = now.strftime("%I:%M %p")
            speak(f"The time is {current_time} sir.")

        elif intent_data['intent'] == "current_hour_day":
            # Format and speak the current hour and day
            current_hour = now.strftime("%I %p").lstrip('0').replace(' 0', ' ')
            current_day = now.strftime("%A")
            speak(f"The current hour is {current_hour} and today is {current_day} sir.")

        elif intent_data['intent'] == "current_hour_month":
            # Format and speak the current hour and month
            current_hour = now.strftime("%I %p").lstrip('0').replace(' 0', ' ')
            current_month = now.strftime("%B")
            speak(f"The current hour is {current_hour} and we are in the month of {current_month} sir.")

        elif intent_data['intent'] == "current_hour_year":
            # Format and speak the current hour and year
            current_hour = now.strftime("%I %p").lstrip('0').replace(' 0', ' ')
            current_year = now.strftime("%Y")
            speak(f"The current hour is {current_hour} and the current year is {current_year} sir.")

        elif intent_data['intent'] == "current_hour":
            # Format and speak the current hour
            current_hour = now.strftime("%I %p").lstrip('0').replace(' 0', ' ')
            speak(f"The current hour is {current_hour} sir.")

        elif intent_data['intent'] == "current_date":
            # Format and speak the current date
            current_date = now.strftime("%A, %B %d, %Y")
            speak(f"Today is {current_date} sir.")

        elif intent_data['intent'] == "current_day":
            # Format and speak the current day
            current_day = now.strftime("%A")
            speak(f"Today is {current_day} sir.")

        elif intent_data['intent'] == "current_month":
            # Format and speak the current month
            current_month = now.strftime("%B")
            speak(f"We are in the month of {current_month} sir.")

        elif intent_data['intent'] == "current_year":
            # Format and speak the current year
            current_year = now.strftime("%Y")
            speak(f"The current year is {current_year} sir.")

    except Exception as e:
        speak("An error occurred")
        speak("Oops! Something went wrong while trying to get the time and date.")
