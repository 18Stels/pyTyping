import time
import pyautogui
import keyboard as key 
import keyboard
speed_write = 0.145 # The speed of typing letters from text
text = 'Text' #Text from the ratatype site.
while True:
	if key.is_pressed("ctrl"): #Key Enabled code
		for alpha in text:
			keyboard.write(alpha)
			time.sleep(speed_write)
			if key.is_pressed('up'):#slowdown
				speed_write += 0.001
			elif key.is_pressed('down'):#speed up
				speed_write -= 0.001
			elif key.is_pressed('right'):#slowdown
				speed_write += 0.0005
			elif key.is_pressed('left'):#speed up
				speed_write -= 0.0005
			print(speed_write)#Output the typing speed to the console
