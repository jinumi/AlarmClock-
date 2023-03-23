# Designed and Developed by Muhammad Umair Yaqub.
# Made in P A K I S T A N

# Import necessary modules
from datetime import datetime
from time import sleep
from playsound import playsound

# Get the time of the alarm from the user
while True:
    alarm_time = input("Enter the time of alarm to be set: HH:MM:SS AM or PM\n")
    try:
        # Extract the hour, minute, second, and period from the alarm_time string
        alarm_hour = int(alarm_time[0:2])
        alarm_minute = int(alarm_time[3:5])
        alarm_seconds = int(alarm_time[6:8])
        alarm_period = alarm_time[9:11].upper()
        if alarm_hour >= 0 and alarm_hour <= 12 and alarm_minute >= 0 and alarm_minute <= 59 and alarm_seconds >= 0 and alarm_seconds <= 59 and alarm_period in ['AM', 'PM']:
            break
        else:
            print("Invalid time format, please try again.")
    except:
        print("Invalid input format, please try again.")

# Print a message to indicate that the alarm is being set up
print("Setting up alarm...")

# Continuously check the current time against the alarm time until they match
while True:
    # Get the current time
    now = datetime.now()

    # Extract the current hour, minute, second, and period from the current time
    current_hour = int(now.strftime("%I"))
    current_minute = int(now.strftime("%M"))
    current_seconds = int(now.strftime("%S"))
    current_period = now.strftime("%p")

    # Check if the current period matches the alarm period
    if alarm_period == current_period:
        # Check if the current hour matches the alarm hour
        if alarm_hour == current_hour:
            # Check if the current minute matches the alarm minute
            if alarm_minute == current_minute:
                # Check if the current second matches the alarm second
                if alarm_seconds == current_seconds:
                    # Print a message to indicate that it's time to wake up
                    print("Wake up!")

                    # Play the alarm sound
                    # You can download the alarm sound from a link
                    playsound('audio.mp3')

                    # Break out of the while loop
                    break
    # Add a delay to the while loop to avoid the program from running continuously and using up system resources.
    sleep(1)
