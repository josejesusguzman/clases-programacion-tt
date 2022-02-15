import os
import mouse
import time
from random import randrange

# direccion = r"C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE"
# os.system(direccion)


mouse.move(x = 500, y = 100, absolute=True , duration=2)
#mouse.click(button='left')

#mouse.drag(start_x= 200, start_y=250, end_x=250, end_y= 260, absolute=True , duration=2)

while True :
    mouse.move(x = randrange(1000), y = randrange(1000), absolute=True , duration=0.5)
    time.sleep(5)
    mouse.click(button='left')
    mouse.move(x = randrange(1000), y = randrange(1000), absolute=True , duration=0.5)
    time.sleep(5)
    mouse.click(button='left')

