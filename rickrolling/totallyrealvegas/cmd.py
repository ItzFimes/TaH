import time
import keyboard
import mouse
mouse_stuck = True


keyboard.send("windows+r")
time.sleep(2)
mouse.move(100, 100, absolute=False, duration=2)
keyboard.send("backspace")
mouse.move(100, 100, absolute=False, duration=2)
keyboard.write("msedge")
mouse.move(100, 100, absolute=False, duration=2)

time.sleep(1)
keyboard.send("enter")
mouse.move(100, 100, absolute=False, duration=2)
time.sleep(3)
keyboard.write("https://www.")
mouse.move(10, 10, absolute=False, duration=1)
keyboard.write("youtube.com")
mouse.move(10, 10, absolute=False, duration=1)
keyboard.write("/embed/")
mouse.move(10, 10, absolute=False, duration=1)
keyboard.write("iik25wqIu")
mouse.move(10, 10, absolute=False, duration=1)
keyboard.write("Fo?auto")
mouse.move(10, 10, absolute=False, duration=1)
keyboard.write("play=1")
mouse.move(10, 10, absolute=False, duration=1)
keyboard.send("enter")
mouse.move(10, 10, absolute=False, duration=7)
