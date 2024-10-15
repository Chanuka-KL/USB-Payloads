import cv2
import numpy as np
import pyautogui
import time

def record_screen(output_filename, duration=10):
    screen_size = pyautogui.size()
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(output_filename, fourcc, 20.0, (screen_size))

    start_time = time.time()
    while time.time() - start_time < duration:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
    
    out.release()
    print(f"Recording saved as {output_filename}")

if __name__ == "__main__":
    record_screen("screen_recording.avi", duration=60)  # Record for 60 seconds