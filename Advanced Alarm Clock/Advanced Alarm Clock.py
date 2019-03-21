#
# Alarm Clock with 2 features that the user can set for a certain time or for counting bacwards
#

import pygame
import time
import datetime

pygame.mixer.init()
pygame.mixer.music.load("C:/AlarmSong.mp3")

option=input("""
             1. Press one to enter a time for counting backwards and ring
             2. Press two setting a certain time for ringing
              """)
if option == '1':
    alarmTimeFormat = input('Enter the format of time, like: seconds, minutes hours')
    alarmTime=int(input('Enter the amount of time'))
    if alarmTimeFormat=='minutes':
        alarmTime=60*alarmTime   #converts minutes to seconds, which is the argument the time library takes for time delay
    elif alarmTimeFormat=='hours':
        alarmTime=3600*alarmTime #converts hours to seconds
    time.sleep(alarmTime)
    pygame.mixer.music.play()



elif option=='2':
    setTime=input('What time do you want to set the alarm? ex: 10:30(space)AM')
    playingWithTime=setTime.split(':')
    playingWithTimeSomeMore=playingWithTime[1].split(" ")
    hourTime=playingWithTime[0]
    hourTime=int(hourTime)
    minuteTime=playingWithTimeSomeMore[0]
    minuteTime=int(minuteTime)
    dayNight=playingWithTimeSomeMore[1]

    if(dayNight=='PM'):
       hourTime=hourTime+12
    check=False
    while check==False:
        test = datetime.datetime.now().replace(hour=hourTime,minute=minuteTime,second=0,microsecond=0)
        if datetime.datetime.now() > test:
           check=True
           pygame.mixer.music.play()


userInput='play'
while userInput=='play':
    userInput=input('Press enter to stop alarm')
pygame.mixer.music.stop()