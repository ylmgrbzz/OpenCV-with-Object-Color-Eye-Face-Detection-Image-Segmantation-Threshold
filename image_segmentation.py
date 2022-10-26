import cv2
import numpy as np
import matplotlib.pyplot as plt
from graph3d import Visualize3D_RGB as vis3d_rgb
from graph3d import Visualize3D_HSV as vis3d_hsv
from graph3d import hsvDisplayer as hsv_disp

img=cv2.imread("bird.jpg")
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#vis3d_rgb(img_rgb)
#vis3d_hsv(img_hsv)

lower_blue=(55,0,0)
upper_blue=(118,255,255)
mask=cv2.inRange(img_hsv,lower_blue,upper_blue)
result=cv2.bitwise_and(img_rgb,img_rgb,mask)

plt.subplot(1,2,1)
plt.imshow(mask,cmap="gray")
cv2.imshow("mask",mask)
cv2.imshow("result",result)
cv2.waitKey(0)
