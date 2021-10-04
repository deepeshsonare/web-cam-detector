from plyer import notification
import keyboard
import cv2

cap = cv2.VideoCapture(0)
flag = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if flag:
        if not cap.isOpened():
            print("Webcam offline")
            notification.notify(title="Webcam",
                             message="WebCam turned off",
                             timeout=1000)
            flag = 0
    else:
        if cap.isOpened():
             print("Webcam online.")
             notification.notify(title="Webcam",
                                 message="PC using WebCam",
                                 timeout=1000)
            flag = 1
    if keyboard.is_pressed('q'):
        break
    

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
