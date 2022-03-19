import datetime
import pygame
from pygame import *
import sys
import pickle
import os
from pygame import mixer
os.system("clear")

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

pygame.init()
pygame.font.init()
pygame.mixer.init()
fps = pygame.time.Clock()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("beepboopblap's alarm app")

# colors
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
brown = (165, 42, 42)
pink = (247, 49, 188)

# fonts
Calibri60 = pygame.font.SysFont("Calibri", 60)
Calibri100 = pygame.font.SysFont("Calibri", 100)
Calibri120 = pygame.font.SysFont("Calibri", 120)
Calibri40 = pygame.font.SysFont("Calibri", 40)
Inconsolata65 = pygame.font.Font("inconsolata.regular.ttf", 65)
Inconsolata90 = pygame.font.Font("inconsolata.regular.ttf", 90)
Inconsolata50 = pygame.font.Font("inconsolata.regular.ttf", 50)

# text
set_reminder_label = Inconsolata50.render("Set Alarm",1 , white)
view_reminders_label = Inconsolata50.render("View Schedule",1 , white)
exit_label = Inconsolata50.render("Exit", 1, red)
chooser = Inconsolata50.render(">", 1, white)
set_reminder_instruct = Inconsolata50.render("Set Alarm in Terminal", 1, white)
press_esc = Inconsolata50.render("Press 'ESC' to Escape", 1, red)
reminders_title = Inconsolata90.render("Reminders", 1, yellow)

# sfx and music 
pygame.mixer.music.load("alarm1.ogg")

# variables
running = True
menu = True
set_reminder = False
view_reminders = False
alarm_detect = True
point = 0
date_alarm1 = ()
time_alarm1 = ()
alarm_names = ["MyAlarm"]
month_input = ""
day_input = ""
hour_input = ""
minutes_input = ""
seconds_input = ""


# load data
alarm_names = pickle.load(open("alarms.txt", "rb"))

while running == True:

    # save data
    pickle.dump(alarm_names, open("alarms.txt", "wb"))

    now = datetime.datetime.now()
    current_month = now.strftime("%m")
    current_day = now.strftime("%d")
    current_hour = now.strftime("%H")
    current_minute = now.strftime("%M")

    if alarm_detect == True:
        if month_input == int(current_month) and day_input == int(current_day) and hour_input == int(current_hour) and minutes_input == int(current_minute):
            pygame.mixer.music.play(-1)
            




    
    if set_reminder == True:

        # time
        now = datetime.datetime.now()
        time_now = now.strftime("Time: %H:%M:%S")
        date_now = now.strftime("Date: %Y-%m-%d")
        time_now_label = Inconsolata65.render(str(time_now), 1, yellow)
        date_now_label = Inconsolata65.render(str(date_now), 1, blue)

        # graphics 
        window.fill(black)
        window.blit(set_reminder_instruct, (45, 500))
        window.blit(time_now_label, (55, 120))
        window.blit(date_now_label, (55, 200))

        pygame.display.update()
        fps.tick(25)

        # event check
        for event in pygame.event.get():
            if event.type == QUIT:
                pickle.dump(alarm_names, open("alarms.txt", "wb"))
                pygame.quit()

        user_input_name = input("Create Alarm Name (input '' to escape): ")
        if user_input_name in alarm_names:
            print("Alarm name already exists!")
            continue
        elif user_input_name == "":
            menu = True
            set_reminder = False

        elif user_input_name not in alarm_names:

            alarm_names.append(user_input_name)
            month_input = int(input("Set Month: "))
            day_input = int(input("Set Day: "))
            hour_input = int(input("Set Hour: "))
            minutes_input = int(input("Set Minute: "))           
            print("Alarm Created!")
            set_reminder = False
            menu = True



    elif menu == True:

        # time
        now = datetime.datetime.now()
        time_now = now.strftime("Time: %H:%M:%S")
        date_now = now.strftime("Date: %Y-%m-%d")
        time_now_label = Inconsolata65.render(str(time_now), 1, yellow)
        date_now_label = Inconsolata65.render(str(date_now), 1, blue)

        # event check
        for event in pygame.event.get():
            if event.type == QUIT:
                pickle.dump(alarm_names, open("alarms.txt", "wb"))
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    point -= 1
                elif event.key == K_DOWN:
                    point += 1
                elif event.key == K_RETURN:
                    if point == 0:
                        set_reminder = True
                        menu = False
                    elif point == 1:
                        view_reminders = True
                        menu = False
                    elif point == 2:
                        pickle.dump(alarm_names, open("alarms.txt", "wb"))
                        pygame.quit()
                        

        point = point % 3

        # graphics
        window.fill(black)
        window.blit(time_now_label, (55, 120))
        window.blit(date_now_label, (55, 200))
        window.blit(set_reminder_label, (175, 400))
        window.blit(view_reminders_label, (175, 500))
        window.blit(exit_label, (175, 600))

        if point == 0:
            window.blit(chooser, (133, 400))
        elif point == 1:
            window.blit(chooser, (133, 500))
        elif point == 2:
            window.blit(chooser, (133, 600))

    elif view_reminders == True:
        
        # event checker
        for event in pygame.event.get():
            if event.type == QUIT:
                pickle.dump(alarm_names, open("alarms.txt", "wb"))
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    create_task = view_reminders
                    menu = True

        # graphics 
        window.fill(black)
        window.blit(reminders_title, (95,70))
        window.blit(press_esc, (35, 700))

        x = 150
        y = 330

        for alarm in alarm_names:
            alarm = Inconsolata50.render(alarm, 1, white)
            window.blit(alarm, (x, y))
            y += 75



    pygame.display.update()
    fps.tick(25)
