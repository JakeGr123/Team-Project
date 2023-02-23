# Jake, Jackson, Lance, Austin
# Snake Game
# 02/23/23
import pygame
import os
import sys
from tkinter import *
import customtkinter




def game():

    pygame.init()
    BLACK = (0, 0, 0)
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Snake Game')


    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get(): 

            if event.type == pygame.QUIT:
                pygame.quit()
                
                
           
        clock.tick(60)
        pygame.display.update()
    pygame.quit()




customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

def Play():
    root.withdraw()
    game()
   




root = customtkinter.CTk()

root.geometry('400x500')

button = customtkinter.CTkButton(master=root, text='Play', command=Play, hover_color='purple', corner_radius=70, height=50,)
button.place(relx=0.5, rely=0.5, anchor=CENTER)                                    

root.mainloop()
        

    