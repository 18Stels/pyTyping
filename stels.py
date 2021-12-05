import time
import pyautogui
import keyboard as key 
import keyboard
speed_write = 0.145 # мс/ нб текста
text = 'Текст'
while True:
	if key.is_pressed("ctrl"): #Клавиша вкл
		for alpha in text:
			keyboard.write(alpha)
			time.sleep(speed_write)
			if key.is_pressed('up'):#Замедлить
				speed_write += 0.001
			elif key.is_pressed('down'):#Ускорить
				speed_write -= 0.001
			elif key.is_pressed('right'):#Замедлить
				speed_write += 0.0005
			elif key.is_pressed('left'):#Ускорить 
				speed_write -= 0.0005
			print(speed_write)#вывод мс нб текста в консоль
