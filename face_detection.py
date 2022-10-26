import cv2
import matplotlib.pyplot as plt

test_img=cv2.imread("ylm2.jpg")
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

gray=cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.3,3)

for (x,y,w,h) in faces:
    cv2.rectangle(test_img,(x,y),(x+w,y+h),(0,255,0),4)

    cv2.imshow("Detected Faces", test_img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()