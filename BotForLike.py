import pyautogui 
from time import sleep
#exbir informação 
pyautogui.alert('O Codigo Vai comerça !! Teamo Thially')
# 2 abrir o google
pyautogui.moveTo(x=34, y=197)
pyautogui.click(clicks=1)
sleep(3)
# 4 digitar o link do instagram
pyautogui.write('https://www.instagram.com/')
pyautogui.press('enter')
# 5 pegar a url de um link de uma # 
pyautogui.moveTo(x=366, y=84)
pyautogui.click(clicks=1)
# 6 entra na pag
pyautogui.write('https://www.instagram.com/explore/tags/fitness/')
pyautogui.press('enter')
sleep(3)
# 7 apertar em uma foto
pyautogui.moveTo(x=541, y=486)
pyautogui.click(clicks=1)
sleep(3)
# 8 deixar o like e proxima foto
for c in range(30):
    pyautogui.moveTo(x=668, y=597)
    sleep(1)
    pyautogui.click(clicks=2)
    pyautogui.moveTo(x=1364, y=592)
    pyautogui.click(clicks=1)
    sleep(3)
