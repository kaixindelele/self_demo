import numpy as np
import matplotlib.pyplot as plt
import cv2

for i in range(10):
    img = np.random.randint(0,(i+1)*20,(300,400,3))
    # fig = plt.gcf()
    # print(fig)
    # plt.close(2)
    
    # plt.figure(num = i)
    # plt.title('num:')
    # plt.imshow(img)
    # plt.pause(1)
    # plt.figure()
    # plt.title('ggdt')
    # plt.imshow(img)

    # plt.show(block=False)
    cv2.imshow("img:"+str(i),img)
    print("continue run ?",str(i))
