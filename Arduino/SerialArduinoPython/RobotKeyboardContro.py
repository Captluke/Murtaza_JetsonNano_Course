import cv2
import SerialModule as sm
import keyboard
ser = sm.initConnection("COM5", 9600)

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    if not success:
        break
    cv2.imshow("Video", img)
    key = cv2.waitKey(1)
    if keyboard.is_pressed('w'):
        sm.sendData(ser, [30, 0], 4)
    elif keyboard.is_pressed('s'):
        sm.sendData(ser, [-30,0],4)
    elif keyboard.is_pressed('a'):
        sm.sendData(ser, [30, 15], 4)
    elif keyboard.is_pressed('d'):
        sm.sendData(ser, [30, -15], 4)
    elif key == ord('q'):
        sm.sendData(ser, [0, 0], 4)
        break
    else:
        sm.sendData(ser, [0, 0], 4)

   #if key == ord('w'):
   #     sm.sendData(ser, [30, 0], 4)
   # elif key == ord('s'):
   #     sm.sendData(ser, [-30, 0], 4)
   # elif key == ord('a'):
   #     sm.sendData(ser, [30, 15], 4)
   # elif key == ord('d'):
   #     sm.sendData(ser, [30, -15], 4)
   # elif key == ord('q'):
   #     sm.sendData(ser, [0, 0], 4)
   #     break
   # elif key == ord('z'):
   #     sm.sendData(ser, [0, 0], 4)
   # else:
   #     sm.sendData(ser, [0, 0], 4)

cap.release()
cv2.destroyAllWindows()
