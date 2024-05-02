# Example file showing a basic pygame "game loop"
import pygame as py
import random

#Constants
WIDTH = 800
HEIGHT = 800
GAME_SPEED = 9
NUMBER_OF_CASES = 20
PIX_PER_UNIT = WIDTH // NUMBER_OF_CASES
BACKGROUND = (0, 26, 0)
SNAKE = (0, 150, 0)
APPLE = (204, 0, 0)

#pygame setup
py.init()
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Snake")
clock = py.time.Clock()
running = True

class Player:
    def __init__(self) -> None:
        self.direction = "RIGHT"
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.has_moved = False
        self.score = 0

    def move(self):
        head = self.body[0]
        x, y = head

        if self.direction == 'UP':
            y -= PIX_PER_UNIT
        elif self.direction == 'DOWN':
            y += PIX_PER_UNIT
        elif self.direction == 'LEFT':
            x -= PIX_PER_UNIT
        elif self.direction == 'RIGHT':
            x += PIX_PER_UNIT
        self.body.pop()
        self.body.insert(0, (x, y))

    def change_direction(self, direction):
        if direction == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        elif direction == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        elif direction == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        elif direction == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

    def grow(self):
        tail = self.body[-1]
        x, y = tail

        if self.direction == 'UP':
            y += PIX_PER_UNIT
        elif self.direction == 'DOWN':
            y -= PIX_PER_UNIT
        elif self.direction == 'LEFT':
            x += PIX_PER_UNIT
        elif self.direction == 'RIGHT':
            x -= PIX_PER_UNIT

        self.body.append((x, y))
        self.score += 1

    def draw(self):
        for segment in self.body:
            py.draw.rect(screen, SNAKE, (segment[0], segment[1], PIX_PER_UNIT-1, PIX_PER_UNIT-1))
        snake.has_moved = True

    def check_collision(self):
        head = self.body[0]
        for segment in self.body[1:]:
            if head[0] == segment[0] and head[1] == segment[1]:
                return True
        return False
    def check_out_of_bounds(self):
        head = self.body[0]
        if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
            return True
        else:
            return False

class Target:
    def __init__(self) -> None:
        self.position = self.generate_new_target_position()

    def generate_new_target_position(self):
        x = random.randint(0, (WIDTH - PIX_PER_UNIT) // PIX_PER_UNIT) * PIX_PER_UNIT
        y = random.randint(0, (HEIGHT - PIX_PER_UNIT) // PIX_PER_UNIT) * PIX_PER_UNIT
        return x, y
    def draw(self):
        py.draw.rect(screen, APPLE, (self.position[0], self.position[1], PIX_PER_UNIT, PIX_PER_UNIT))
def clear_display():
    screen.fill("black")

snake = Player()
apple = Target()
def reset():
    global snake, apple
    print("SCORE: ", snake.score)
    del snake, apple
    snake = Player()
    apple = Target()
while running:

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.KEYDOWN:
                if event.key == py.K_w and snake.has_moved == True:
                    snake.has_moved = False
                    snake.change_direction('UP')
                elif event.key == py.K_s and snake.has_moved == True:
                    snake.has_moved = False
                    snake.change_direction('DOWN')
                elif event.key == py.K_a and snake.has_moved == True:
                    snake.has_moved = False
                    snake.change_direction('LEFT')
                elif event.key == py.K_d and snake.has_moved == True:
                    snake.has_moved = False
                    snake.change_direction('RIGHT') 
    
    clear_display()  
    snake.move() 
    snake.draw()
    apple.draw()
      
    if snake.body[0] == apple.position:
            snake.grow()
            apple.position = apple.generate_new_target_position()
    
    if snake.check_out_of_bounds()== True:
        reset()
    if snake.check_collision()== True:
        reset()

    py.display.update()
    clock.tick(GAME_SPEED)

py.quit()