from machine import Pin
import time

direction = 'RIGHT'

button_up = Pin(2, Pin.IN, Pin.PULL_UP)
button_down = Pin(1, Pin.IN, Pin.PULL_UP)
button_right = Pin(0, Pin.IN, Pin.PULL_UP)
button_left = Pin(3, Pin.IN, Pin.PULL_UP)

def check_for_inputs():
    t = time.time()
    while time.time()-t < 0.1:
        if button_up.value() == 0:
            direction = 'UP'
        
        if button_down.value() == 0:
            direction = 'DOWN'
        
        if button_right.value() == 0:
            direction = 'RIGHT'

        if button_left.value() == 0:
            direction = 'LEFT'
        print(direction)
        time.sleep(0.004)
            
# while True:
#         if button_up.value() == 0:
#             direction = 'UP'
#         
#         if button_down.value() == 0:
#             direction = 'DOWN'
#         
#         if button_right.value() == 0:
#             direction = 'RIGHT'
# 
#         if button_left.value() == 0:
#             direction = 'LEFT'
#         time.sleep(0.004)
#         print(direction)