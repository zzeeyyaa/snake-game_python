import pygame
from pygame.locals import *  # import certain global variable
import time


class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        # method loading the image, block or snake
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x, self.y = 100, 100
        self.direction = 'down'

    def draw(self):
        self.parent_screen.fill((110, 110, 5))  # clear the screen
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.update()

    def move_up(self):
        self.direction = 'up'
        # self.y -= 10
        # self.draw()

    def move_down(self):
        self.direction = 'down'
        # self.y += 10
        # self.draw()

    def move_left(self):
        self.direction = 'left'
        # self.x -= 10
        # self.draw()

    def move_right(self):
        self.direction = 'right'
        # self.x += 10
        # self.draw()

    def walk(self):
        # drawing the snake based on current direction
        if self.direction == 'up':
            self.y -= 10
        if self.direction == 'down':
            self.y += 10
        if self.direction == 'left':
            self.x -= 10
        if self.direction == 'right':
            self.x += 10

        self.draw()


class Game:
    def __init__(self):
        pygame.init()  # initiate pygame

        # initialize a window on screen for display
        self.surface = pygame.display.set_mode((500, 500))  # background
        self.surface.fill((255, 255, 255))
        # put the screen
        self.snake = Snake(self.surface)
        # draw the snake
        self.snake.draw()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                    if event.key == K_LEFT:
                        self.snake.move_left()

                elif event.type == QUIT:
                    running = False

            self.snake.walk()  # snake will keeping moving on and on, without press key
            time.sleep(0.2)


# main routine in python
if __name__ == "__main__":
    game = Game()
    game.run()
