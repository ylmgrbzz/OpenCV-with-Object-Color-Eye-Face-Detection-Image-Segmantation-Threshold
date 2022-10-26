import cv2
import imutils

img=cv2.imread("people.jpg")
img=imutils.resize(img,500)
hog=cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
(coordinate,_)=hog.detectMultiScale(img, winStride=(4,4),
                                    padding=(8,8),
                                    scale=1.05)
color=(0,255,0)
thickness=5
for (x,y,w,h) in coordinate:
    cv2.rectangle(img,(x,y),(x+w,y+h),color,thickness)

cv2.imshow("Original Image",img)
cv2.waitKey(0)
print(coordinate)