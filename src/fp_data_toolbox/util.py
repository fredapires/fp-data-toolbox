# %%
import pyautogui
import random
import time


# %%
def sleep_prevention():
    while True:
        center_x, center_y = pyautogui.size()  # get the screen size
        center_x //= 2
        center_y //= 2
        # generate a random x coordinate within 100 pixels of the center
        rand_x = random.randint(center_x - 100, center_x + 100)
        # generate a random y coordinate within 100 pixels of the center
        rand_y = random.randint(center_y - 100, center_y + 100)
        # move the mouse to the random pixel
        pyautogui.moveTo(rand_x, rand_y, duration=0.25)
        time.sleep(10)  # wait for 10 seconds before repeating the process
        if random.random() < 0.5:  # 50% chance of right clicking
            pyautogui.rightClick()  # perform a right click
            time.sleep(1)  # wait for the context menu to appear
        if time.time() % 30 == 0:  # check if 30 seconds have elapsed
            pyautogui.rightClick()  # perform a random right click
            time.sleep(1)  # wait for the context menu to appear
# %%


sleep_prevention()
# %%
