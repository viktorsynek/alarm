############################################   -== INFORMATION ==-   ############################################

#### THE PROGRAM WAS CREATED AND PUBLISHED BY:
#### https://github.com/viktorsynek
#### https://www.linkedin.com/in/viktor-synek/

#############################################   -== PROGRAM ==-   ###############################################

#IMPORT LIBRARIES
from datetime import datetime
from pydub import AudioSegment
from pydub.playback import play


while True:
    # CORRECT TIME FORMAT
    print("Enter time in 'HH:MM:SS am/pm'")
    print("Example: '08:11:00 am'")
    # USER GIVES THE TIME
    alarm_time = input('Input: ')

    # HANDLE INCORRECT FORMATS
    if len(alarm_time) != 11:
        print("Invalid format!") 
    else:
        if int(alarm_time[0:2]) > 12:
            print("") 
        elif int(alarm_time[3:5]) > 59:
            print("Invalid format!") 
        elif int(alarm_time[6:8]) > 59:
            print("Invalid format!")
        else:
            print(f"Setting alarm for {alarm_time}...")
            break

# CUT OUT ALL THE DATA FROM THE STRING
alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
alarm_period = alarm_time[9:].upper()

while True:
    now = datetime.now()

    current_hour = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_period = now.strftime("%p")

    # NESTED IF STATEMENTS [!]
    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_min == current_min:
                if alarm_sec == current_sec:
                    # LOCATE THE DIRECTORY TO THESE PROJECT FILES
                    # AND GET A .wav FORMATTED SOUND FILE, IF YOU WANT SOUND TO BE PLAYED
                    song = AudioSegment.from_wav("CHANGE.ME")
                    play(song)
                    break
