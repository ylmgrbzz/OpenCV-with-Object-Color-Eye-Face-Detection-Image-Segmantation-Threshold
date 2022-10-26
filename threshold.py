import cv2

img=cv2.imread("ylm.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

def nothing(x):
    pass

cv2.namedWindow("Threshold Trackbar")
cv2.createTrackbar("lower","Threshold Trackbar",0,255,nothing)
cv2.createTrackbar("upper","Threshold Trackbar",0,255,nothing)

while True:
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    lower=cv2.getTrackbarPos("lower","Threshold Trackbar")
    upper=cv2.getTrackbarPos("upper","Threshold Trackbar")

    ret,threshold=cv2.threshold(gray,lower,upper,cv2.THRESH_BINARY)

    cv2.imshow("Threshold Trackbar",threshold)
cv2.destroyAllWindows()