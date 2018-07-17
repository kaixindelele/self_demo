import cv2
import matplotlib.pyplot as plt 

img = cv2.imread("rgb.jpg")
cv2.circle(img,(100,100),22,(255,0,0),-1)
show_image = cv2.resize(img,(960,540))
plt.imshow(show_image)
plt.show(block = False)
plt.pause(3)
print("ok!")