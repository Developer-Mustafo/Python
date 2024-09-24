import pyautogui

# while True:
#     print(pyautogui.position())
#     pyautogui.sleep(2)
# x=952, y=470
x, y = pyautogui.position()
print(pyautogui.onScreen(x, y))
pyautogui.sleep(5)
pyautogui.moveTo(952, 470, 1)
for i in range(9000):
    pyautogui.doubleClick()
