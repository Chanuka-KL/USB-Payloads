import cv2

def capture_webcam_image():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    cv2.imwrite("webcam_capture.jpg", frame)
    cam.release()
    print("Image captured and saved as webcam_capture.jpg")

if __name__ == "__main__":
    capture_webcam_image()