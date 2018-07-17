import tensorflow as tf 
import numpy as np 

x_data = np.float32(np.random.rand(2,100))

#x_data.shape is (2,100)
#np.dot() is the multiply of matrix
#and * is that figure multiply one by one
# original function is y = [0.1,0.2] * [[100个],[100个]]+0.3
# so y is just a figure
y_data = np.dot([0.100,0.200],x_data)+0.300

b = tf.Variable(tf.zeros([1]))
W = tf.Variable(tf.random_uniform([1,2],-1.0,1.0))
y = tf.matmul(W,x_data) + b

loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.1)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

with tf.Session() as sess:
	sess.run(init)
	for step in range(0,5001):
		sess.run(train)
		if step % 20 == 0:
			print(step,sess.run(W),sess.run(b))