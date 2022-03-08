import pyautogui
import pyperclip
import time


pyautogui.click(x = 21, y = 765)
pyautogui.write("League of Legends")
pyautogui.press("enter")
time.sleep(30)

time.sleep(3)
#primeiro
pyautogui.click(x = 1116, y = 701)
texto = f""" Salve meu mano essa mensagem é automatizada por python sabia? Quer aprender a automatizar tarefas com python como eu acesse o link abaixo:
https://www.youtube.com/channel/UCafFexaRoRylOKdzGBU6Pgg
"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")


#segundo Point(x=628, y=462)
pyautogui.click(x = 628, y = 462)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")


#terceiro Point(x=592, y=502)
pyautogui.click(x = 592, y = 502)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")


#quarto Point(x=583, y=570)
pyautogui.click(x = 583, y = 570)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")


#quinto Point(x=619, y=616)
pyautogui.click(x = 619, y = 616)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")


#sexto Point(x=604, y=676)
pyautogui.click(x = 604, y = 676)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

#X Point(x=1306, y=20), Sair  x=593, y=415
pyautogui.click(x = 1306, y = 20)
pyautogui.click(x = 593, y = 415)