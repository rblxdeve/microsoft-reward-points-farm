# If you are a script kiddie use this lol btw script kiddies is an insult
import webbrowser, time
import pyautogui

x = 0
while True:
    webbrowser.open_new(f'https://www.bing.com/search?q={x}')
    x += 1
    time.sleep(3)
    pyautogui.keyDown("ctrl") 
    pyautogui.press('w')
    pyautogui.keyUp("ctrl")
	#before running this code have 1 tab open in ur browser 
