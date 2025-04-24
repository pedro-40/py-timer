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
        h=int(input(Fore.GREEN+"how many hours... / "))
        m=int(input("a few minutes... / "))
        s=int(input("a few seconds... /"))
    
        if h < 0 or m < 0 or s < 0:
            print(Fore.RED+"please enter a positive number...")
            time.sleep(5)

            clear()

            banner()
        
        if s >= 60:
            w = s // 60
            m += w
            s= s - (w*60)
      
        if m >= 60:
            e= m // 60
            h += e
            m = m -(e*60)


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



            
            i=input("enter music directory... /")
            M=input("music name ... /")


        print(Fore.CYAN+f"{h} hours : {m} minutes : {s} seconds")
        total=h*3600+m*60+s
        print("The timer starts after 10 seconds. :)")
        time.sleep(10)
        while total > 0 :

            clear()
            banner()

            print(Fore.MAGENTA+f"secondes :{total}")
            total -= 1
            time.sleep(1)
        while total == 0 and alarm.lower()=="y":

            clear()

            banner()

            os.chdir(i)
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
