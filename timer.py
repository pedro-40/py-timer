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
                
    print(Fore.BLUE +"""
             _   _                     
 _ __  _   _| |_(_)_ __ ___   ___ _ __ 
| '_ \| | | | __| | '_ ` _ \ / _ \ '__|
| |_) | |_| | |_| | | | | | |  __/ |   
| .__/ \__, |\__|_|_| |_| |_|\___|_|   
|_|    |___/  

"""+Fore.RESET)
    
def choice() :

    while True :

        choice = input(Fore.BLUE+"DO you want to start timer ? (Y,n) ")
        if (
            choice.lower()=="y" or 
            choice=="") :

            time_set()

        elif choice.lower()=="n" :

            exit()

        else :
            print(Fore.RED+"this choice is not in choices " )
            time.sleep(3)
            clear()
    
    return choice()


    


def time_set():

    time1 = list(input(Fore.BLUE+"Enter Time in HH:MM:SS format : "+Fore.RESET).split(":"))

    try:

        for i in range(len(time1)) : time1[i] = int(time1[i])

    except :

        print(Fore.RED+"Entered Time is invalid\nExample valid time : 12:36:00\n"+Fore.RESET)
        return time_set()


    def time_format (time) :

        if len(time1) != 3 :
            print(Fore.RED+"Entered Time is invalid\nExample valid time : 12:36:00\n"+Fore.RESET)
            return time_set() 
        
        if (

            time1[0] < 0 or
            time1[1] < 0 or
            time1[2] < 0 
        ):
            print(Fore.RED+"Entered Time is invalid\nExample valid time : 12:36:00\n"+Fore.RESET)
            return time_set() 
        
        if (

            time1[1] > 60 or
            time1[2] > 60 
        ):
            print(Fore.RED+"Entered Time is invalid\nExample valid time : 12:36:00\n"+Fore.RESET)
            return time_set()

    time_format(time1)

    clear()

    print(Fore.BLUE+f"The time you set : {time1[0]}:{time1[1]}:{time1[2]} \n"+Fore.RESET)

    def alarm_choice () :
        
        alarm = input(Fore.BLUE+"Do you want to set an alarm? (Y/n)"+Fore.RESET)

        if (
            alarm.lower()=="y" or
            alarm ==""
        ):
            alarm_set()

        elif alarm.lower() == "n":
            
            pass

        else:
            print(Fore.RED+"this choice is not in choices "+Fore.RESET)

            time.sleep(3)
            clear()
            alarm_choice()

    alarm_choice()

    return time1


def alarm_set () : 
    
    def alarm_dow () :
        print(8 * 40)

        os.mkdir("my-alarms")

        def_alarm = os.listdir("my-alarms")

        if "beep1.mp3" not in def_alarm :
            url = "https://sedatoseda.com/wp-content/uploads/Cuckoo-Clock-Alarm-Sound.mp3"

            request= requests.get(url)
            if request.status_code == 200 :
                os.chdir("my-alarms")
                with open('beep1.mp3', 'wb') as f:
                    for chunk in request.iter_content(chunk_size=1024):  
                        f.write(chunk)

    def cp_alarm () :

        alarm_cp = input(Fore.BLUE+"Do you want to sing a song? (Y/n) "+Fore.RESET)

        if (
            alarm_cp.lower() == "y" or
            alarm_cp == ""
        ):
            you = os.path.expanduser("~")
            music_directory = os.path.join(you, "Music")
            os.chdir(music_directory)
            m = os.listdir()

            Music_choice = input(Fore.BLUE+"Enter the name of the music (enter h for help) "+Fore.RESET)

            if Music_choice.lower() == "h" :
                for i in m :
                    print (i)
            
            elif Music_choice not in m :
                pass
            

    dirc = os.listdir()

    if "my-alarms" not in dirc :
        alarm_dow() 
    cp_alarm()    

while True:

    clear()

    choice()

    alarm_set()

    #choice=input(Fore.RED+"Do you want to start the timer? (y/n)" )
    #if 'y' == choice.lower():
    #    time_set()
       
        #alarm=input("Do you want to set an alarm?(y/n) ")
        #if alarm.lower()=="y" :
        #    folder_list=os.listdir()
        #    
        #    if "my-alarms" not in folder_list:
        #        os.mkdir("my-alarms")
        #    default_alarm = os.listdir()
#
#
        #    if "beep1.mp3" not in default_alarm:
        #        url_download = "https://sedatoseda.com/wp-content/uploads/Cuckoo-Clock-Alarm-Sound.mp3"
#
        #        request = requests.get(url_download)
#
        #        if request.status_code == 200 :
        #            os.chdir("my-alarms")
#
        #            with open('beep1.mp3', 'wb') as f:
#
        #                for chunk in request.iter_content(chunk_size=1024):  
        #                    f.write(chunk)
#
        #    alarm_choice = input("Do you want to sing a song?(y/n)   ")
#
        #    if alarm_choice.lower() == "n":
        #        
#
        #        M ="beep1.mp3"
#
        #    if alarm_choice.lower() == "y" :
#
        #        song_copy = input("Do you want me to list the names of the songs?  (y/n)  ")
#
        #        if song_copy.lower() == "y" :
#
        #            you = os.path.expanduser("~")
        #            music_directory = os.path.join(you, "Music")
        #            os.chdir(music_directory)
#
#
        #            m = os.listdir()
#
        #            for i in m :
        #                print (i)
#
        #            cp_song = input("Enter the name of the song you want.   ")
        #            
        #            if cp_song in m :
#
        #                if os.name == "nt" :
#
        #                    os.system(f"copy {m}")
        #                    os.chdir("../my-alarms")
        #                    os.system(f"paste {m}")
        #                else:
        #                    os.system(f'cp {m} ../my-alarms')
                            


       # print(Fore.CYAN+f"{hour} hours : {minutes} minutes : {seconds} seconds")
#
       # total_time = hour*3600+minutes*60+seconds
#
       # print("The timer starts after 10 seconds. :)")
       # time.sleep(10)
       # while total_time > 0 :
#
       #     clear()
       #     
#
       #     print(Fore.MAGENTA+f"secondes :{total_time}")
       #     total_time -= 1
       #     time.sleep(1)
#
       # while total_time == 0 and alarm.lower()=="y":
#
       #     clear()
#
       #     
       #     while True :
       #         os.chdir("../my-alarms")
       #         pygame.mixer.init()
       #         sound=pygame.mixer.Sound(M)
       #         sound.play()
       #         for_off=input(Fore.BLUE+"for off enter y ... /")
       #         if "y"==for_off.lower() :
       #             pygame.mixer.quit()
       #             break
#

              
    #elif 'n' == choice.lower() :
    #    clear()
    #    break
#
#
    #
    #else:
    #    print("this choice is not in choices ... /")
    #    time.sleep(5)
    #    clear()
        
