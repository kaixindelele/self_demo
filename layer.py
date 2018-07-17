import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

def add_layer(inputs,in_size,out_size,activation_function=None):
	Weights = tf.Variable(tf.random_normal([in_size,out_size]))
	biase = tf.Variable(tf.zeros([1,out_size])+0.1)
	Wx_plus_b = tf.matmul(inputs,Weights)+biase

	if activation_function is None:
		outputs = Wx_plus_b
	else:
		outputs = activation_function(Wx_plus_b)

	return outputs
#将行向量增加维度，原来的shape是(300,)，需要改成(300,1)
#同样的目标，通过shape也可以实现,大概是转置的效果
x_data = np.linspace(-1,1,300)[:,np.newaxis]

# x_data = np.linspace(-1,1,300)
# x_data.shape = (300,1)
# print(x_data.shape)

noise = np.random.normal(0,0.05,x_data.shape)
y_data = np.square(x_data) - 0.5 + noise

xs = tf.placeholder(tf.float32,[None,1])
ys = tf.placeholder(tf.float32,[None,1])


input_layer = add_layer(xs,1,10,activation_function = tf.nn.relu)
hidden_layer = add_layer(input_layer,10,1,activation_function = None )

loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - hidden_layer),reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()

with tf.Session() as sess:
	sess.run(init)
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1)
	ax.scatter(x_data,y_data)
	
	#在Python2中，可以用下面的方法，使函数子显示图片的时候也不会暂停，可以继续执行。
	#其实在Python3中也行
	# plt.show(block = False)
	plt.ion()
	plt.show()
	
	for i in range(2000):
		sess.run(train_step,feed_dict = {xs:x_data,ys:y_data})
		if i % 20 == 0:
			# print(sess.run(loss,feed_dict = {xs:x_data,ys:y_data}))
			try:
				ax.lines.remove(lines[0])
			except Exception:
				pass
			prediction_value = sess.run(hidden_layer,feed_dict={xs:x_data})

			lines = ax.plot(x_data,prediction_value,'r-',lw = 5)
			print(lines)
			plt.pause(0.1)
			# plt.show()