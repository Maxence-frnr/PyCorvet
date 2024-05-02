from machine import Pin
from gpio_lcd import GpioLcd
import utime
#les imports                        
                                                
lcd = GpioLcd(rs_pin = Pin(0),                  #♂♀♪
              enable_pin = Pin(1),              
              d4_pin = Pin(2),                  
              d5_pin = Pin(3),                  
              d6_pin = Pin(4),                  
              d7_pin = Pin(5),                  
              num_lines = 2, num_columns = 16)
#config l'écran

left = Pin(21, Pin.IN, Pin.PULL_UP)
up = Pin(20, Pin.IN, Pin.PULL_UP)
right = Pin(18, Pin.IN, Pin.PULL_UP)
down = Pin(19, Pin.IN, Pin.PULL_UP)

coordonne = [0, 0] #max : 5 * 12 ; 2 * 7
coordonne_force = [0, 0]

def draw(x, y, char_mem=None):
    if char_mem is None:
        char_mem = 0
    
    x_char = int(x / 5)
    x_pixel = 4 - (x - (5* x_char))
    #print("X : Complexe no: ", x_char)
    #print("    Pixel no   : ", x_pixel)
    
    y_char = int(y / 8)
    y_pixel = y - (8* y_char)
    #print("Y : Complexe no: ", y_char)
    #print("    Pixel no   : ", y_pixel)
    
    cstm_chr = [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
    
    cstm_chr[y_pixel] = int(hex(int(str(10**(x_pixel)), 2)))
    #print(cstm_chr)
    char = bytearray(cstm_chr)
    
    lcd.move_to(x_char, y_char)
    lcd.custom_char(char_mem, char)
    lcd.putchar(chr(char_mem))
    
def relachement(boutton):
    appuyer = True
    while appuyer == True:
        if boutton.value() == 1:
            appuyer = False
            
def check(x, y):
    if x < 0:
        coordonne[0] = 0
    if x > 60:
        coordonne[0] = 60
    if y < 0:
        coordonne[1] = 0
    if y > 14:
        coordonne[1] = 14
        
while True:
    if left.value() == 0:
        coordonne_force = [-1, 0]
        relachement(left)
        
    if right.value() == 0:
        coordonne_force = [1, 0]
        relachement(right)
        
    if up.value() == 0:
        coordonne_force = [0, 1]
        relachement(up)
        
    if down.value() == 0:
        coordonne_force = [0, -1]
        relachement(down)
    
    utime.sleep(0.3)
    lcd.clear()
    coordonne[0] = coordonne[0] + coordonne_force[0]
    coordonne[1] = coordonne[1] + coordonne_force[1]
    print(coordonne)
    check(coordonne[0], coordonne[1])
    draw(coordonne[0], coordonne[1])