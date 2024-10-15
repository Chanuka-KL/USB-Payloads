import pyautogui
import time

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    print("Screenshot taken and saved as screenshot.png")

if __name__ == "__main__":
    time.sleep(5)  # Give 5 seconds before taking the screenshot
    take_screenshot()