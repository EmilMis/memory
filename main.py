import numpy as np
import random
import time
import os
import time, sys
from pygame import mixer
import keyboard

def start_animation():
    striing = r""" 
        $$\      $$\                                                       
        $$$\    $$$ |                                                      
        $$$$\  $$$$ | $$$$$$\  $$$$$$\$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ 
        $$\$$\$$ $$ |$$  __$$\ $$  _$$  _$$\ $$  __$$\ $$  __$$\ $$ |  $$ |
        $$ \$$$  $$ |$$$$$$$$ |$$ / $$ / $$ |$$ /  $$ |$$ |  \__|$$ |  $$ |
        $$ |\$  /$$ |$$   ____|$$ | $$ | $$ |$$ |  $$ |$$ |      $$ |  $$ |
        $$ | \_/ $$ |\$$$$$$$\ $$ | $$ | $$ |\$$$$$$  |$$ |      \$$$$$$$ |
        \__|     \__| \_______|\__| \__| \__| \______/ \__|       \____$$ |
                                                                 $$\   $$ |
                                                                 \$$$$$$  |
                                                                  \______/
            """
    for i in range(len(striing)):
        print(striing[i], end="")
        time.sleep(0.00005)

def play_music():
    mixer.init()

    sound = mixer.Sound(r"""C:\Users\emilm\Downloads\MEMORY\y.wav""")
    sound.play()

def start_screen():
    os.system("cls")
    covered = 0
    string = "Pritisni 'q'"
    start_animation()
    while not keyboard.is_pressed('q'):
        play_music()
        os.system("cls")
        for i in range(22):
            try:  # used try so that if user pressed other than the given key error will not be shown
                if keyboard.is_pressed('q'):  # if key 'q' is pressed
                    print('You Pressed A Key!')
                    break  # finishing the loop
            except:
                break
            print(r"""
            
        $$\      $$\                                                       
        $$$\    $$$ |                                                      
        $$$$\  $$$$ | $$$$$$\  $$$$$$\$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ 
        $$\$$\$$ $$ |$$  __$$\ $$  _$$  _$$\ $$  __$$\ $$  __$$\ $$ |  $$ |
        $$ \$$$  $$ |$$$$$$$$ |$$ / $$ / $$ |$$ /  $$ |$$ |  \__|$$ |  $$ |
        $$ |\$  /$$ |$$   ____|$$ | $$ | $$ |$$ |  $$ |$$ |      $$ |  $$ |
        $$ | \_/ $$ |\$$$$$$$\ $$ | $$ | $$ |\$$$$$$  |$$ |      \$$$$$$$ |
        \__|     \__| \_______|\__| \__| \__| \______/ \__|       \____$$ |
                                                                 $$\   $$ |
                                                                 \$$$$$$  |
                                                                  \______/
                                                                  
                                                                  
            """)
            print(string)
            time.sleep(0.5)
            os.system("cls")
            try:  # used try so that if user pressed other than the given key error will not be shown
                if keyboard.is_pressed('q'):  # if key 'q' is pressed
                    print('You Pressed A Key!')
                    break  # finishing the loop
            except:
                break
            print(r"""


        $$\      $$\                                                       
        $$$\    $$$ |                                                      
        $$$$\  $$$$ | $$$$$$\  $$$$$$\$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ 
        $$\$$\$$ $$ |$$  __$$\ $$  _$$  _$$\ $$  __$$\ $$  __$$\ $$ |  $$ |
        $$ \$$$  $$ |$$$$$$$$ |$$ / $$ / $$ |$$ /  $$ |$$ |  \__|$$ |  $$ |
        $$ |\$  /$$ |$$   ____|$$ | $$ | $$ |$$ |  $$ |$$ |      $$ |  $$ |
        $$ | \_/ $$ |\$$$$$$$\ $$ | $$ | $$ |\$$$$$$  |$$ |      \$$$$$$$ |
        \__|     \__| \_______|\__| \__| \__| \______/ \__|       \____$$ |
                                                                 $$\   $$ |
                                                                 \$$$$$$  |
                                                                  \______/
                                                                  
            """)
            print(string)
            time.sleep(0.5)
            os.system("cls")
            try:  # used try so that if user pressed other than the given key error will not be shown
                if keyboard.is_pressed('q'):  # if key 'q' is pressed
                    print('You Pressed A Key!')
                    break  # finishing the loop
            except:
                break
            print(r"""



        $$\      $$\                                                       
        $$$\    $$$ |                                                      
        $$$$\  $$$$ | $$$$$$\  $$$$$$\$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ 
        $$\$$\$$ $$ |$$  __$$\ $$  _$$  _$$\ $$  __$$\ $$  __$$\ $$ |  $$ |
        $$ \$$$  $$ |$$$$$$$$ |$$ / $$ / $$ |$$ /  $$ |$$ |  \__|$$ |  $$ |
        $$ |\$  /$$ |$$   ____|$$ | $$ | $$ |$$ |  $$ |$$ |      $$ |  $$ |
        $$ | \_/ $$ |\$$$$$$$\ $$ | $$ | $$ |\$$$$$$  |$$ |      \$$$$$$$ |
        \__|     \__| \_______|\__| \__| \__| \______/ \__|       \____$$ |
                                                                 $$\   $$ |
                                                                 \$$$$$$  |
                                                                  \______/
            """)
            print(string)
            time.sleep(0.5)
            os.system("cls")
            try:  # used try so that if user pressed other than the given key error will not be shown
                if keyboard.is_pressed('q'):  # if key 'q' is pressed
                    print('You Pressed A Key!')
                    break  # finishing the loop
            except:
                break
            print(r"""


        $$\      $$\                                                       
        $$$\    $$$ |                                                      
        $$$$\  $$$$ | $$$$$$\  $$$$$$\$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ 
        $$\$$\$$ $$ |$$  __$$\ $$  _$$  _$$\ $$  __$$\ $$  __$$\ $$ |  $$ |
        $$ \$$$  $$ |$$$$$$$$ |$$ / $$ / $$ |$$ /  $$ |$$ |  \__|$$ |  $$ |
        $$ |\$  /$$ |$$   ____|$$ | $$ | $$ |$$ |  $$ |$$ |      $$ |  $$ |
        $$ | \_/ $$ |\$$$$$$$\ $$ | $$ | $$ |\$$$$$$  |$$ |      \$$$$$$$ |
        \__|     \__| \_______|\__| \__| \__| \______/ \__|       \____$$ |
                                                                 $$\   $$ |
                                                                 \$$$$$$  |
                                                                  \______/
                                                                  
            """)
            print(string)
            time.sleep(0.5)
            os.system("cls")
            try:  # used try so that if user pressed other than the given key error will not be shown
                if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                    print('You Pressed A Key!')
                    break  # finishing the loop
            except:
                break  # if user pressed a key other than the given key the loop will break
    os.system("cls")
def get_pos(element):
    element_in_list = "[" + element + "]"
    list = construct_fake(x, y)[0]
    location = np.argwhere(list == element_in_list)
    return location[0][0], location[0][1]

def construct_fake(x, y):

    stuff = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    fake_list = [0] * x * y

    for i in range(len(fake_list)):
        fake_list[i] = "[" + str(stuff[i]) + "]"
        choice_list.append(stuff[i])
    arr = np.array(fake_list)
    # Convert 1D array to a 2D numpy array of 2 rows and 3 columns
    arr_2d = np.reshape(arr, (x, y))
    return arr_2d, fake_list


def construct(x, y):
    list = [0] * x * y

    num = 1

    for i in range(0, len(list), 2):
        list[i] = num
        list[i + 1] = num
        num += 1

    random.shuffle(list)

    arr = np.array(list)
    # Convert 1D array to a 2D numpy array of 2 rows and 3 columns
    arr_2d = np.reshape(arr, (x, y))
    return arr_2d, list

def animation(x, y):
    fake_list = construct_fake(x, y)[0]
    for i in range(x):
        for n in range(y):
            print(fake_list[i][n], end=" ")
            time.sleep(0.5)
        print()
        time.sleep(0.5)

def print_board(x, y, reveal1):
    real_board = construct(x, y)[0]
    fake_board = construct_fake(x, y)[0]
    reveal1_x = get_pos(reveal1)[0]
    reveal1_y = get_pos(reveal1)[1]
    for i in range(x):
        for n in range(y):
            try:
                revealed2 = revealed[0]
                revealed2_x = get_pos(revealed2)[0]
                revealed2_y = get_pos(revealed2)[1]
                if(i == revealed2_x) and (n == revealed2_y):
                    print(" " + str(real_board[i][n]) + " ", end=" ")
                if (i == reveal1_x) and (n == reveal1_y):
                    print(" " + str(real_board[i][n]) + " ", end=" ")
                    revealed.append(reveal1)
                else:
                    print(fake_board[i][n], end=" ")
            except:

                if(i == reveal1_x) and (n == reveal1_y):
                    print(" " + str(real_board[i][n]) + " ", end=" ")
                    revealed.append(reveal1)
                else:
                    print(fake_board[i][n], end=" ")
        print()

start_screen()

x = int(input("> "))
y = int(input("> "))

revealed = []

choice_list = []
num_list = construct(x, y)[1]
construct_fake(x, y)

list1 = construct(x, y)[0]
animation(x, y)

upis = input("Unesi Polje: ")
print_board(x, y, upis)