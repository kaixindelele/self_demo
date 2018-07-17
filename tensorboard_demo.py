"""
Dependencies:
tensorflow: 1.6.0
python:3.5
numpy

"""

import tensorflow as tf 
import numpy as np 

tf.set_random_seed(1)
np.random.seed(1)

def add_layer(inputs,in_size,out_size,activation_function = None):
	Weights = tf.Variable(tf.random_normal([in_size,out_size]))
	baises = tf.Variable(tf.zeros([1,out_size])+0.1)
	Wx_plus_b = tf.matmul(inputs,Weights)+baises
	if activation_function is None:
		outputs = Wx_plus_b
	else:
		outputs = activation_function(Wx_plus_b)
	return outputs



x = np.linspace(-1,1,300)[:,np.newaxis]
noise = np.random.normal(0,0.1,size = x.shape)
#np.power()是求次方
y = np.power(x,2)+noise

with tf.variable_scope("Inputs"):
	tf_x = tf.placeholder(tf.float32,x.shape,name="x")
	tf_y = tf.placeholder(tf.float32,y.shape,name="y")

with tf.variable_scope("Net"):
	# l1 = tf.layers.dense(tf_x,10,tf.nn.relu,name = "hidden_layer")
	# output = tf.layers.dense(l1,1,name="output_layer")
	l1 = add_layer(tf_x,1,10,activation_function=tf.nn.relu)
	output = add_layer(l1,10,1,activation_function=None)

	tf.summary.histogram("h_out",l1)
	tf.summary.histogram("pred",output)

loss = tf.losses.mean_squared_error(tf_y,output,scope="loss")
train_op = tf.train.GradientDescentOptimizer(learning_rate=0.5).minimize(loss)
tf.summary.scalar("loss",loss)

sess = tf.Session()
merge_op = tf.summary.merge_all()

writer = tf.summary.FileWriter("./logs",sess.graph)
sess.run(tf.global_variables_initializer())

for step in range(100):
	__,result = sess.run([train_op,merge_op],feed_dict = {tf_x:x,tf_y:y})
	writer.add_summary(result,step)

