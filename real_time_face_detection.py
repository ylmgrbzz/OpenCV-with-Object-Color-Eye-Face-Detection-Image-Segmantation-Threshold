import cv2

cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    if ret==False:
        break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,3)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)

        cv2.imshow("Detected Faces", frame)

        if cv2.waitKey(30) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()