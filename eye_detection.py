import cv2
import matplotlib.pyplot as plt

test_img=cv2.imread("ylm.jpg")
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")


gray=cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.3,3)

for (x,y,w,h) in faces:
    cv2.rectangle(test_img,(x,y),(x+w,y+h),(0,255,0),4)
    roi=gray[y:y+h,x:x+w]
    roi_color=gray[y:y+h,x:x+w]

    eyes=eye_cascade.detectMultiScale(roi,1.3,3)
    for (x1, y1, w1, h1) in faces:
        cv2.rectangle(roi_color, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 4)


cv2.imshow("Detected Faces", test_img)
cv2.waitKey(0)
cv2.destroyAllWindows()