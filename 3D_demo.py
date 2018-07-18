import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)
X,Y = np.meshgrid(X,Y)
# R只是将二者平方和，开方了
R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)
#绘制3D热图表面
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap("rainbow"))
#绘制等高线
ax.contourf(X,Y,Z,zdir="z",offset=-1.5,cmap=plt.get_cmap("rainbow"))
#在z轴方向压缩图的大小
ax.set_zlim(-2,2)

plt.show()