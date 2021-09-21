import pyautogui
import random

pyautogui.moveTo(600, 1300, duration=1)
pyautogui.click()

pyautogui.moveTo(620, 50, duration=1)
pyautogui.click()

# Generate random letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# Generate random letters
print(random.choice(letters))

letrasrandom = ""
for i in range(0, 3):
    letrasrandom += random.choice(letters)

pyautogui.write("https://www.youtube.com/channel/UC8ORzy4p0vyZ2Nu5V_-rxKA", interval=0.1)
pyautogui.press('enter')

pyautogui.moveTo(900, 900, duration=1)

pyautogui.moveTo(600, 1000, duration=1)
pyautogui.click()

while True:
    pyautogui.moveTo(500, 500, duration=1)
    pyautogui.moveTo(500, 700, duration=1)
    pyautogui.moveTo(700, 700, duration=1)
    pyautogui.moveTo(700, 500, duration=1)