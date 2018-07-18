import matplotlib.pyplot as plt 

import numpy as np 

x = np.linspace(-3,3,50)
y1 = 2 * x + 1
y2 = x ** 2 + 1

#创建图片，并且为图片命名
plt.figure(num = 1)
plt.ion()

#给xy限定范围
plt.xlim((-4,4))
plt.ylim((-8,8))

#给每个轴加上标注
plt.xlabel('i am x')
plt.ylabel('i am y')

#为轴上的坐标点分布限定内容
new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2,-1.5,-1,0,1,1.5],
			["too low",r"$low\ \alpha$","$little\ low$","ok","little high","high"])

#plt.gca()获取当前坐标轴
#将xy坐标轴和上下左右轴对应起来
#然后将平移xy的中心值
ax = plt.gca()
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
ax.spines["bottom"].set_position(("data",0))
ax.spines["left"].set_position(("data",0))

#为每条线加上一个标签，然后给标签加上图例
plt.plot(x,y2,label = "up")
plt.plot(x,y1,color = 'red',linewidth=1.0, linestyle = '--',label = "down")
plt.legend(loc = "best")


#标注单个散点
x0 = 2
y0 = x0 ** 2 + 1
plt.scatter(x0,y0,s = 50,color = "b")
plt.scatter(x0,x0,s = 50,color = "k")
plt.scatter(0,y0,s = 100,color = "k")
plt.scatter(0,0,s = 50,color = "r")
#画出虚线，第一个框中第一个数对应第二个框第一个数，形成一个坐标
plt.plot([x0,x0,],[0,y0,],'k--',lw = 3)

#给曲线加标注,如果位置偏移的话，需要将xycoords,xytext,textcoords都加上才行。
#后面的是字体大小，箭头类型和箭头线的弯曲程度
plt.annotate(r"$2x+1=%s$"%y0,xy=(x0,y0),xycoords = "data",xytext = (+30,-30),textcoords = "offset points",
	fontsize = 16,arrowprops = dict(arrowstyle="->",connectionstyle='arc3,rad=.3'))

#第二种方法直接在图中显示出文本信息
plt.text(x0-2,y0-2,r"$this is the line $",fontdict = {'size':16,'color':'r'})
# plt.show()

plt.pause(2)  #显示秒数
# 可见程序确实是暂定在这儿了
print("continue run?")
plt.close()