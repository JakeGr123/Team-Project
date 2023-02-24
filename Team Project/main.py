# Jake, Jackson, Lance, Austin
# Snake Game
# 02/23/23
import pygame
import os
import sys
from tkinter import *
import customtkinter

SIZE = 40
BACKGROUND = pygame.image.load('Background.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (500, 500))
def game():

    class Snake:
        def __init__(self):
            self.image = pygame.image.load("snake block.jpg").convert()
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.direction = 'down'
            self.length = 1
            self.x = [40]
            self.y = [40]
            
        def move_left(self):
            self.direction = 'left'

        def move_right(self):
            self.direction = 'right'

        def move_up(self):
            self.direction = 'up'

        def move_down(self):
            self.direction = 'down'

        def walk(self):
            # update body
            for i in range(self.length-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]
                
                


            # update head
            if self.direction == 'left':
                self.x[0] -= SIZE
            if self.direction == 'right':
                self.x[0] += SIZE
            if self.direction == 'up':
                self.y[0] -= SIZE
            if self.direction == 'down':
                self.y[0] += SIZE


            if self.x[0] < 0 or self.x[0] >= 500 or self.y[0] < 0 or self.y[0] >= 500:
                print('You Lost Monkey')
                pygame.quit()

        def draw(self, surface):
            for i in range(self.length):
                surface.blit(self.image, (self.x[i], self.y[i]))

    class Game:
        def __init__(self):
            self.surface = pygame.display.set_mode((500, 500))
            pygame.display.set_caption('Snake Game')
            self.snake = Snake()

        def run(self):
            clock = pygame.time.Clock()
            running = True
            while running:
                clock.tick(10)
        
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running = False
                        elif event.key == pygame.K_LEFT:
                            self.snake.move_left()
                        elif event.key == pygame.K_RIGHT:
                            self.snake.move_right()
                        elif event.key == pygame.K_UP:
                            self.snake.move_up()
                        elif event.key == pygame.K_DOWN:
                            self.snake.move_down()

                self.surface.blit(BACKGROUND, (0, 0))
                self.snake.walk()
                self.snake.draw(self.surface)
                pygame.display.update()

            pygame.quit()

    def play_game():
        pygame.init()
        game = Game()
        game.run()

    if __name__ == '__main__':
        play_game()

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
        

    