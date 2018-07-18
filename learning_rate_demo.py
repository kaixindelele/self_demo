# coding:utf-8

import tensorflow as tf 
import matplotlib.pyplot as plt 
import numpy as np

W = tf.Variable(tf.constant(5,dtype = tf.float32))
loss = tf.square(W + 1)
train_step = tf.train.GradientDescentOptimizer(0.8).minimize(loss)

with tf.Session() as sess:
	init_op = tf.global_variables_initializer()
	sess.run(init_op)
	w_val = []
	loss_val = []

	for i in range(400):
		sess.run(train_step)
		w_val.append(sess.run(W))
		loss_val.append(sess.run(loss))
		# print("After %s steps: W is %f,\t loss is %f ." % (i,w_val,loss_val))
	print("len(w_val):",len(w_val))
	length = 40
	plt.plot(range(length),w_val[:length],linestyle = '--', color = "b",label = "w_val")
	plt.scatter(range(length),w_val[:length],s = 50,color = "b")
	plt.plot(range(length),loss_val[:length],color = "r",label = "loss_val")
	plt.scatter(range(length),loss_val[:length],s = 50,color = "r")
	plt.legend(loc = "best")
	plt.show()
