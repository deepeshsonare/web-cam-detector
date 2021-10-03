from plyer import notification
import cv2

cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if cap.isOpened():
        print("Webcam online.")
        notification.notify(title="Webcam",
                    message="PC using WebCam",
                    timeout=1000)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
