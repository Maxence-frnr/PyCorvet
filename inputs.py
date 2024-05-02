import picoSnake








from machine import Pin

import time

button_up = Pin(1, Pin.IN, Pin.PULL_UP)
button_down = Pin(2, Pin.IN, Pin.PULL_UP)
button_right = Pin(3, Pin.IN, Pin.PULL_UP)
button_left = Pin(4, Pin.IN, Pin.PULL_UP)

while True:
    if button_up.value() == 1:
        picoSnake.snake.direction = 'UP'
    if button_down.value() == 1:
        picoSnake.snake.direction = 'DOWN'
    if button_right.value() == 1:
        picoSnake.snake.direction = 'RIGHT'
    if button_left.value() == 1:
        picoSnake.snake.direction = 'LEFT'
    time.sleep(0.1)
    print(picoSnake.snake.direction)

