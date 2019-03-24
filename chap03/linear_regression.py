#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: linear_regression.py
#    Created:       <2019/03/23 19:19:20>
#    Last Modified: <2019/03/24 11:01:00>

import numpy as np

# === Create data and simulate results ===
x_data = np.random.randn(2000, 3)
w_real = [0.3, 0.5, 0.1]
b_real = -0.2

noise = np.random.randn(1, 2000) * 0.1
y_data = np.matmul(w_real, x_data.T) + b_real + noise

import tensorflow as tf

NUM_STEPS = 10

g = tf.Graph()
wb_ = []
with g.as_default():
    x = tf.placeholder(tf.float32, shape=[None, 3])
    y_true = tf.placeholder(tf.float32, shape=None)

    with tf.name_scope('inference') as scope:
        w = tf.Variable([[0, 0, 0]], dtype=tf.float32, name='weights')
        b = tf.Variable(0, dtype=tf.float32, name='bias')
        y_pred = tf.matmul(w, tf.transpose(x)) + b

    with tf.name_scope('loss') as scope:
        loss = tf.reduce_mean(tf.square(y_true - y_pred))

    with tf.name_scope('train') as scope:
        learning_rate = 0.5
        optimizer = tf.train.GradientDescentOptimizer(learning_rate)
        # minimize は第 3 引数に指定された Variable のリスト、
        # もしくはデフォルトで GraphKeys.TRAINABLE_VARIABLES に含まれる Variable
        # を第一引数の loss を最小化するように最適化する。
        # tf.Variable は第二引数に GraphKeys.TRAINABLE_VARIABLES に含むか否かの flag を取るが、デフォルトで真となる。
        train = optimizer.minimize(loss)

    # Before starting, initialize the variables. We will 'run' this first.
    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)
        for step in range(NUM_STEPS):
            sess.run(train, {x: x_data, y_true: y_data})
            if ( step % 5 == 0 ):
                print(step, sess.run([w, b]))
                wb_.append(sess.run([w, b]))

        print(10, sess.run([w, b]))
