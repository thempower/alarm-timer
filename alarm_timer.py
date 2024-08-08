
#imprting library playsound 
from playsound import playsound
import os
import time
sound_path = 'alarm_timer/audio/standard.wav'
print(os.path.exists(sound_path))
#ANSI codes
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"
#path to default alarm file
minutes = int(input("How many minuts set a alarm on:"))
seconds = int(input("How many seconds set a alarm on:"))
alarm_sound = input("Which alarm sound you prefer: standard or retro?" )
total_seconds = minutes * 60 + seconds

#function which count remeaning time
def alarm(total_seconds):
   #checking of provided number is > 0 - execute or exit a program
   if total_seconds > 0:  
     time_elapsed = 0

     print(CLEAR)  
     while time_elapsed < total_seconds:
         #wait 1 sec
         time.sleep(1)
         time_elapsed += 1

         time_left = total_seconds - time_elapsed
         minutes_left = time_left // 60
         seconds_left = time_left % 60

         #printing remaining time & formating 
         print(f"{ CLEAR_AND_RETURN}Time remaining:{minutes_left:02d}:{seconds_left:02d}") 
         
    
         # checking when time is finished and starting alarm
         if time_left == 0:
            print(f"{CLEAR_AND_RETURN}IT is time to WAKE UP!!! ALARM IS GOING ON!!!")
            #checking alarmsound - default is standard
            if alarm_sound != "standard":
               playsound('audio/retro.wav')
            else: playsound('audio/standard.wav')

    
   else: print("Please provide a number > 0 and start the program again "), exit()


        
alarm(total_seconds)






