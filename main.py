from turtle import delay
import pyautogui
import time
from mss import mss

x = 700
y = 775

box = (x, y, x + 408, y + 1)

coords_x = [0, 136, 272, 407]

# def time_test():

#     with mss() as sct: 
        
#         t1 = time.time()

#         for i in range(100):

#             img = sct.grab(box)

#             pyautogui.click(137, 965)

#         t2 = time.time()

#         print(t2-t1)
        
# time_test()

def start():

    with mss() as sct:

        while (True): 
            
            img = sct.grab(box)

            for cord in coords_x:

                if img.pixel(cord, 0)[0] < 100:

                    pyautogui.click(x + cord, y)

                    break

time.sleep(3)

start()

# def print_mouse_pos():

#     while (True):
#         pos=pyautogui.position()
#         print(pos)
#         time.sleep(1)

# print_mouse_pos()