import os
import time
import pygame
import requests
from colorama import Fore 

def clear():

    if os.name=="nt":
       os.system("cls")
    else:
        os.system("clear")


def banner():
                
    print(Fore.BLUE +"""
             _   _                     
 _ __  _   _| |_(_)_ __ ___   ___ _ __ 
| '_ \| | | | __| | '_ ` _ \ / _ \ '__|
| |_) | |_| | |_| | | | | | |  __/ |   
| .__/ \__, |\__|_|_| |_| |_|\___|_|   
|_|    |___/  

""")

while True:

    clear()

    banner()

    choice=input(Fore.RED+"Do you want to start the timer? (y/n)" )
    if 'y' == choice.lower():
        hour = int(input(Fore.GREEN+"how many hours... / "))
        minutes = int(input("a few minutes... / "))
        seconds = int(input("a few seconds... /"))
    
        if hour < 0 or minutes < 0 or seconds < 0:
            print(Fore.RED+"please enter a positive number...")
            time.sleep(5)

            clear()

            banner()
        
        if seconds >= 60:
            w = seconds // 60
            minutes += w
            seconds = seconds - (w*60)
      
        if minutes >= 60:
            e= minutes // 60
            hour += e
            minutes = minutes -(e*60)


        alarm=input("Do you want to set an alarm?(y/n) ")
        if alarm.lower()=="y" :
            folder_list=os.listdir()
            
            if "my-alarms" not in folder_list:
                os.mkdir("my-alarms")
            default_alarm = os.listdir()


            if "beep1.mp3" not in default_alarm:
                url_download = "https://sedatoseda.com/wp-content/uploads/Cuckoo-Clock-Alarm-Sound.mp3"

                request = requests.get(url_download)

                if request.status_code == 200 :
                    os.chdir("my-alarms")

                    with open('beep1.mp3', 'wb') as f:

                        for chunk in request.iter_content(chunk_size=1024):  
                            f.write(chunk)

            alarm_choice = input("Do you want to sing a song?(y/n)   ")

            if alarm_choice.lower() == "n":
                

                M ="beep1.mp3"

            if alarm_choice.lower() == "y" :

                song_copy = input("Do you want me to list the names of the songs?  (y/n)  ")

                if song_copy.lower() == "y" :

                    you = os.path.expanduser("~")
                    music_directory = os.path.join(you, "Music")
                    os.chdir(music_directory)


                    m = os.listdir()

                    for i in m :
                        print (i)

                    cp_song = input("Enter the name of the song you want.   ")
                    
                    if cp_song in m :

                        if os.name == "nt" :

                            os.system(f"copy {m}")
                            os.chdir("../my-alarms")
                            os.system(f"paste {m}")
                        else:
                            os.system(f'cp {m} ../my-alarms')
                            


        print(Fore.CYAN+f"{hour} hours : {minutes} minutes : {seconds} seconds")

        total_time = hour*3600+minutes*60+seconds

        print("The timer starts after 10 seconds. :)")
        time.sleep(10)
        while total_time > 0 :

            clear()
            banner()

            print(Fore.MAGENTA+f"secondes :{total_time}")
            total_time -= 1
            time.sleep(1)

        while total_time == 0 and alarm.lower()=="y":

            clear()

            banner()
            while True :
                os.chdir("../my-alarms")
                pygame.mixer.init()
                sound=pygame.mixer.Sound(M)
                sound.play()
                for_off=input(Fore.BLUE+"for off enter y ... /")
                if "y"==for_off.lower() :
                    pygame.mixer.quit()
                    break


              
    elif 'n' == choice.lower() :
        clear()
        break


    
    else:
        print("this choice is not in choices ... /")
        time.sleep(5)
        clear()
        banner()
