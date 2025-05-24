# Script By Jackhammer Development (u/PreppyToast)

import pydirectinput as controller
import time

time_to_wait = 10
print(f"You have {time_to_wait} seconds to switch to game")
time.sleep(time_to_wait)
iterations = 100


for i in range (iterations):
    print (f" Start Iteration {i+1}")
    # Start Menu Interaction
    controller.press('e')
    time.sleep(3.3)
    controller.press('esc')
    time.sleep(2.6)

    # Start Walking To Target Position
    controller.keyDown('d')
    time.sleep(3)
    controller.keyUp("d")
    controller.keyDown("w")
    time.sleep(3)
    controller.keyUp("w")
    controller.keyDown("a")
    time.sleep(0.6)
    controller.keyUp("a")
    time.sleep(1)
    controller.keyDown("w")
    time.sleep(0.3)
    controller.keyUp("w")
    controller.press('2')
    time.sleep(1)
    controller.keyDown("w")
    time.sleep(1.5)
    controller.keyDown("a")
    time.sleep(3)
    controller.keyUp("w")
    controller.keyUp("a")
    time.sleep(0.5)

    # Initiate Attack
    controller.press("4")
    time.sleep(3)
    controller.press("4")
    time.sleep(6)

    #Reset
    controller.press('q')
    print (f" Completed Iteration {i+1} \n")
    time.sleep(17)
