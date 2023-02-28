# Jake, Jackson, Lance, Austin
# Snake Game
# 02/23/23
import pygame
import os
import sys
import random
from tkinter import *
import customtkinter
ANGLE = 0
BLACK = (0, 0, 0)
SIZE = 40
BACKGROUND = pygame.image.load('Background.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (500, 500))
def game():
    class Apple:
        def __init__(self, parent_screen):
            self.parent_screen = parent_screen
            self.image = pygame.image.load("monkey.png").convert()
            self.image = pygame.transform.scale(self.image, (50, 50 ))
            self.image.set_colorkey(BLACK)
            self.x = 120
            self.y = 120

        def draw(self):
            self.parent_screen.blit(self.image, (self.x, self.y))
            pygame.display.flip()

        def move(self):
            self.x = random.randint(1, 24) * SIZE
            self.y = random.randint(1, 19) * SIZE

    class Snake:
        def __init__(self):
            self.head_image = pygame.image.load('snake head.jpg').convert()
            self.head_image = pygame.transform.scale(self.head_image, (50, 50))
            self.head_image.set_colorkey(BLACK)
            self.body_image = pygame.image.load("snake block.jpg").convert()
            self.body_image = pygame.transform.scale(self.body_image, (50, 50))
            self.body_image.set_colorkey(BLACK)
            self.direction = 'down'
            self.length = 1
            self.head_x = 40
            self.head_y = 40
            self.body_x = [0 * (self.length - 1)] 
            self.body_y = [0 * (self.length - 1)] 

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
            for i in range(self.length - 2, -1, -1):
                self.body_x[i + 1] = self.body_x[i]
                self.body_y[i + 1] = self.body_y[i]
            self.body_x[0] = self.head_x
            self.body_y[0] = self.head_y

            # update head
            if self.direction == 'left':
                self.head_x -= SIZE
            if self.direction == 'right':
                self.head_x += SIZE
            if self.direction == 'up':
                self.head_y -= SIZE
            if self.direction == 'down':
                self.head_y += SIZE

            if self.head_x < 0:
                pygame.quit()

            if self.head_x >= 500:
                pygame.quit()

            if self.head_y < 0:
                pygame.quit()

            if self.head_y >= 500:
                pygame.quit()

        def draw(self, surface):
            surface.blit(self.head_image, (self.head_x, self.head_y))
            for i in range(self.length - 1):
                surface.blit(self.body_image, (self.body_x[i], self.body_y[i]))

    class Game:
        def __init__(self):
            self.surface = pygame.display.set_mode((500, 500))
            pygame.display.set_caption('Snake Game')
            self.snake = Snake()
            self.apple = Apple(self.surface)
            
        def reset(self):
            self.snake = Snake()
            self.apple = Apple(self.surface)

        def is_collision(self, x1, y1, x2, y2):
            if x1 >= x2 and x1 < x2 + SIZE:
                if y1 >= y2 and y1 < y2 + SIZE:
                    return True
            return False

        def play(self):
            self.apple.draw()

    if __name__ == '__main__':
        pygame.init()
        game1 = Game()

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
                        game1.snake.move_left()
                    elif event.key == pygame.K_RIGHT:
                        game1.snake.move_right()
                    elif event.key == pygame.K_UP:
                        game1.snake.move_up()
                    elif event.key == pygame.K_DOWN:
                        game1.snake.move_down()

            game1.surface.blit(BACKGROUND, (0, 0))
            game1.play()
            game1.snake.walk()
            game1.snake.draw(game1.surface)
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