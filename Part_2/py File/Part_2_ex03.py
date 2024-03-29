#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf


# In[2]:


import numpy as np


# In[3]:


tf.set_random_seed(777)


# In[4]:


xy = np.loadtxt("C:\\Users\\Dreng\\Study_JupyterNotebook\\data-04-zoo.csv", delimiter=',', dtype=np.float32)
x_data = xy[:, 0:-1]
y_data = xy[:, [-1]]

print(x_data.shape, y_data.shape)


# In[5]:


nb_classes = 7

X = tf.placeholder(tf.float32, shape=[None, 16])
Y = tf.placeholder(tf.int32, shape=[None, 1])


# In[6]:


Y_one_hot = tf.one_hot(Y, nb_classes)
print("one_hot:", Y_one_hot)
Y_one_hot = tf.reshape(Y_one_hot, [-1, nb_classes])
print("reshape one_hot:", Y_one_hot)


# In[7]:


W = tf.Variable(tf.random_normal([16, nb_classes], name='weight'))
b = tf.Variable(tf.random_normal([nb_classes], name='bias'))


# In[8]:


logits = tf.matmul(X, W) + b
hypothesis = tf.nn.softmax(logits)


# In[9]:


cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=logits,
                                                                 labels=tf.stop_gradient([Y_one_hot])))


# In[10]:


optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)


# In[11]:


prediction = tf.argmax(hypothesis, 1)
correct_prediction = tf.equal(prediction, tf.argmax(Y_one_hot, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))


# In[12]:


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    for step in range(2001):
        _, cost_val, acc_val = sess.run([optimizer, cost, accuracy], feed_dict={X: x_data, Y: y_data})
        
        if step % 100 == 0:
            print("Step: {:5}\tCost: {:.3f}\tAcc: {:.2%}".format(step, cost_val, acc_val))
            
    # Let's see if we can predict
    pred = sess.run(prediction, feed_dict={X: x_data})
    # y_data: (N, 1) = flatten => (N, ) matches pred.shape
    for p, y in zip(pred, y_data.flatten()):
        print("[{}] Prediction: {} True Y: {}".format(p == int(y), p, int(y)))


# In[ ]:




