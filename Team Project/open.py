
# PyGame Tutorial -- Mike Webb
# V 3.0 -- 1/9/23
import pygame, sys
import os
lives = 250
x=0
y=0
hit_corner_x= False
hit_corner_y= False

def play():
    pygame.mixer.music.load(os.path.join('Assets','expppl.mp3'))
    pygame.mixer.music.play(loops=0)


    def draw(self,win):
        
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
pygame.init()   # this initiates the application
x=0
y=0
red = (255, 0, 0)
white = (255, 255, 255)
hit_corner_x= False
hit_corner_y= False
lives_left = str(lives)
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Pygame Tutorial')
rectangle = pygame.image.load(os.path.join('Assets', 'destroyer.png'))
rectangle = pygame.transform.scale(rectangle, (400, 250))
clock = pygame.time.Clock()
car = pygame.image.load(os.path.join('Assets', 'among us cake.gif'))
pygame.display.set_icon(car)
# Load rocket and space background images
rocket1 = pygame.image.load(os.path.join('Assets', 'hampyship.png'))
rocket = pygame.transform.scale(rocket1, (100, 100))
bg = pygame.image.load(os.path.join('Assets', 'background.jpg'))
x_pos = 20
y_pos = 20
step = 15
angle = 0
move_right = False
move_left = False
move_down = False
move_up = False
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)
def play():
    pygame.mixer.music.load(os.path.join('Assets','expppl.mp3'))
    pygame.mixer.music.play(loops=0)
while True:
    
    if hit_corner_x==False:
        x+=20
    else:
        x-=20
    if hit_corner_y==False:
        y+=10
    else:
        y-=10
    
    if x>=800:
        hit_corner_x=True
    if x<=0:
        hit_corner_x=False
    if y>=550:
        hit_corner_y=True
    if y<=0:
        hit_corner_y=False
   # Update box position and draw box with rocket image
    if move_left:
       x_pos -= step*2
       angle = 90
    if move_right:
       x_pos += step
       angle = 270
    if move_up:
       y_pos -= step
       angle = 0
    if move_down:
       y_pos += step
       angle = 180
    screen.blit(bg, (0, 0))
    screen.blit(rectangle, (x, y))
   # set bounds so that the image can't leave the screen bounds
    if x_pos > x and x_pos < x+400 and y_pos > y and y_pos < y+250:
        lives -=1
        print(lives)
       # Set the square's position to just outside the surface of the surface and place it on opposite side of it
        '''if move_left:
           x_pos = 300
        elif move_right:
           x_pos = 749
        elif move_up:
           y_pos = 0
        elif move_down:
           y_pos = 200'''
    if x_pos < 0:
       x_pos = 0
    if x_pos > 1100:
       x_pos = 1100
    if y_pos < 0:
       y_pos = 0
    if y_pos > 700:
       y_pos = 700
   # Drawing the rect & attaching the image to it
    box = pygame.draw.rect(screen, 'black', (x_pos, y_pos, 20, 20), 1)

    if move_left and x_pos > 1100:  # Check if box is at the left edge of the screen
       x_pos -= step
       angle = 90
    if move_right and x_pos < 1100:  # Check if box is at the right edge of the screen
       x_pos += step
       angle = 270
    if move_up and y_pos > 0:  # Check if box is at the top edge of the screen
       y_pos -= step
       angle = 0
    if move_down and y_pos < 700:  # Check if box is at the bottom edge of the screen
       y_pos += step
       angle = 180

   # Rotate rocket image in the direction it is headed... made is a perfect square
    rotated_rocket = pygame.transform.rotate(rocket, angle)
    rotated_rect = rotated_rocket.get_rect(center=rocket.get_rect(topleft=(x_pos, y_pos)).center)

   # Blit the rotated rocket image on screen with the direction... rotated rocket
    screen.blit(rotated_rocket, rotated_rect)
    if lives==0:
            sys.exit()
    for event in pygame.event.get():
       if event.type == pygame.QUIT:                                              
           pygame.quit()
           sys.exit()
           
       # Lines below process the events of the keyboard
       elif event.type == pygame.KEYDOWN:
           if event.key == pygame.K_RIGHT:
               move_right = True
           if event.key == pygame.K_LEFT:
               move_left = True
           if event.key == pygame.K_DOWN:
               move_down = True
           if event.key == pygame.K_UP:
               move_up = True
       elif event.type == pygame.KEYUP:
           if event.key == pygame.K_RIGHT:
               move_right = False
           if event.key == pygame.K_LEFT:
               move_left = False
           if event.key == pygame.K_DOWN:
               move_down = False
           if event.key == pygame.K_UP:
               move_up = False
           if  event.key ==pygame.K_SPACE:
                play()
    lives_left = str(lives)

   

    font = pygame.font.Font(None, 30)
    if lives>=50:
        text = font.render('Health Left:' + lives_left, True,white)
    if lives<=50:
        text = font.render('Health Left:' + lives_left, True,red)
    screen.blit(text, (500, 770))

    if lives == 0:
        screen.blit(text, (85, 70))
    
    pygame.display.update()     

    clock.tick(60)

