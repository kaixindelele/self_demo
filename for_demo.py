# coding:utf-8
import tensorflow as tf 
import numpy as np 
BATCH_SIZE = 8
seed = 23455

rng = np.random.RandomState(seed)
X = rng.rand(8,2)
#这种for循环迭代只能在列表中使用
Y = [[int(x0+x1<1)] for x0,x1 in X]

print("Y:",Y)