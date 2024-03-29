#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf


# In[2]:


import numpy as np


# In[3]:


tf.set_random_seed(777)


# In[4]:


x_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)
y_data = np.array([[0], [1], [1], [0]], dtype=np.float32)


# In[5]:


X = tf.placeholder(tf.float32, [None, 2])
Y = tf.placeholder(tf.float32, [None, 1])


# In[6]:


W1 = tf.Variable(tf.random_normal([2, 10], name='weight1'))
b1 = tf.Variable(tf.random_normal([10], name='bias1'))
layer1 = tf.sigmoid(tf.matmul(X, W1) + b1)

W2 = tf.Variable(tf.random_normal([10, 10], name='weight2'))
b2 = tf.Variable(tf.random_normal([10], name='bias2'))
layer2 = tf.sigmoid(tf.matmul(layer1, W2) + b2)

W3 = tf.Variable(tf.random_normal([10, 10], name='weight3'))
b3 = tf.Variable(tf.random_normal([10], name='bias3'))
layer3 = tf.sigmoid(tf.matmul(layer2, W3) + b3)

W4 = tf.Variable(tf.random_normal([10, 1], name='weight4'))
b4 = tf.Variable(tf.random_normal([1], name='bias4'))
hypothesis = tf.sigmoid(tf.matmul(layer3, W4) + b4)


# In[7]:


cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1 - hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)


# In[8]:


predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))


# In[9]:


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    for step in range(10001):
        _, cost_val = sess.run([train, cost], feed_dict={X: x_data, Y: y_data})
        
        if step % 100 == 0:
            print(step, cost_val)
            
    h, p, a = sess.run(
        [hypothesis, predicted, accuracy], feed_dict={X: x_data, Y: y_data}
    )
    
    print("\nHypothesis:\n", h, "\nPredicted:\n", p, "\nAccuracy:\n", a)


# In[ ]:




