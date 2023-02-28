import pygame
import random
score = 0
angle = 0
SIZE = 40
BACKGROUND = pygame.image.load('Background.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (500, 500))
class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("monkey.png").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(0,460)
        self.y = random.randint(0,460)

class Snake:
    
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.head_down_image = pygame.image.load('snake head down.png').convert()
        self.head_down_image = pygame.transform.scale(self.head_down_image, (50, 50))
        self.head_up_image = pygame.image.load('snake head up.png').convert()
        self.head_up_image = pygame.transform.scale(self.head_up_image, (50, 50))
        self.head_left_image = pygame.image.load('snake head left.png').convert()
        self.head_left_image = pygame.transform.scale(self.head_left_image, (50, 50))
        self.head_right_image = pygame.image.load('snake head right.png').convert()
        self.head_right_image = pygame.transform.scale(self.head_right_image, (50, 50))
        self.body_image = pygame.image.load("snake block.jpg").convert()
        self.body_image = pygame.transform.scale(self.body_image, (50, 50))
        self.direction = 'down'
        self.length = 1
        self.head_x = 40
        self.head_y = 40
        self.body_x = []
        self.body_y = []
        self.moveup = False
        self.movedown = False
        self.moveleft = False
        self.moveright = False
        self.angle = 0

    def move_left(self):
        if self.moveright == False:
            self.angle = 180
            self.moveleft = True
            self.direction = 'left'
            self.moveup = False
            self.movedown = False
            self.moveright = False
            self.head_image = self.parent_screen.blit(self.head_left_image, (self.head_x, self.head_y))
            print(self.angle)
            pygame.display.update()

    def move_right(self):
        if self.moveleft == False:
            self.angle = 90
            self.direction = 'right'
            self.moveright = True
            self.moveup = False
            self.moveleft = False
            self.movedown = False
            print(self.angle)
            self.head_right_image = self.parent_screen.blit(self.head_right_image, (self.head_x, self.head_y))
            pygame.display.update()

    def move_up(self):
        if self.movedown == False:
            self.angle = 180
            self.direction = 'up'
            self.moveup = True
            self.movedown = False
            self.moveleft = False
            self.moveright = False
            print(self.angle)
            self.head_up_image = self.parent_screen.blit(self.head_up_image, (self.head_x, self.head_y))
            pygame.display.update()

    def move_down(self):
        if self.moveup == False:
            self.angle = 0
            self.direction = 'down'
            self.movedown = True
            self.moveup = False
            self.moveleft = False
            self.moveright = False
            print(self.angle)
            self.head_down_image = self.parent_screen.blit(self.head_down_image, (self.head_x, self.head_y))
            pygame.display.update()

    def walk(self):
        # update body
        if self.length > 1:
            self.body_x.append(self.head_x)
            self.body_y.append(self.head_y)
            for i in range(self.length-2, -1, -1):
                self.body_x[i+1] = self.body_x[i]
                self.body_y[i+1] = self.body_y[i]
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

        if self.head_x < 0 or self.head_x >= 500 or self.head_y < 0 or self.head_y >= 500:
            pygame.quit()
    def check_collision(self):
            head_rect = pygame.Rect(self.head_x, self.head_y, SIZE, SIZE)
            for i in range(1, self.length):
                body_rect = pygame.Rect(self.body_x[i], self.body_y[i], SIZE, SIZE)
                if head_rect.colliderect(body_rect):
                    return True
            return False

    def draw(self):
        if angle == 0:
            self.parent_screen.blit(self.head_down_image, (self.head_x, self.head_y))
        if angle == 90:
            self.parent_screen.blit(self.head_right_image, (self.head_x, self.head_y))
        if angle == 270:
            self.parent_screen.blit(self.head_left_image, (self.head_x, self.head_y))
        if angle == 180:
            self.parent_screen.blit(self.head_up_image, (self.head_x, self.head_y))
        for i in range(self.length - 1):
            self.parent_screen.blit(self.body_image, (self.body_x[i], self.body_y[i]))
        pygame.display.update()
class Game:
    def __init__(self):
        self.surface = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('Snake Game')
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)

    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)

    def play(self, score):
        snake_rect = pygame.Rect(self.snake.head_x, self.snake.head_y, SIZE, SIZE)
        apple_rect = pygame.Rect(self.apple.x, self.apple.y, SIZE, SIZE)

        if snake_rect.colliderect(apple_rect):
            self.snake.length += 1
            score += 1
            self.snake.body_x.append(self.snake.head_x)
            self.snake.body_y.append(self.snake.head_y)
            self.apple.move()

        for i in range(self.snake.length - 1):
            body_rect = pygame.Rect(self.snake.body_x[i], self.snake.body_y[i], SIZE, SIZE)

        if self.snake.head_x < 0 or self.snake.head_x >= 500 or self.snake.head_y < 0 or self.snake.head_y >= 500:
            pygame.quit()

        self.snake.walk()
        self.surface.blit(BACKGROUND, (0, 0))
        self.snake.draw()
        self.apple.draw()
        pygame.display.flip()

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
                        
            if score == 5:
                if event.key == pygame.K_ESCAPE:
                        running = False
                elif event.key == pygame.K_LEFT:
                        self.snake.move_right()
                        self.snake.moveright = False
                elif event.key == pygame.K_RIGHT:
                        self.snake.move_left()
                        self.snake.moveleft = False
                elif event.key == pygame.K_UP:
                        self.snake.move_down()
                        self.snake.movedown = False
                elif event.key == pygame.K_DOWN:
                        self.snake.move_up()
                        self.snake.moveup = False
            self.play(score)
        pygame.quit()
def play_game():
        pygame.init()
        game = Game()
        game.run()
if __name__ == '__main__':
        play_game()
