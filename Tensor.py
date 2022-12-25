import tensorflow as tf
# with tf.device('/gpu:0'):
x1 = tf.constant([1,2,3,4,5])
x2  = tf.constant([6,7,8,9,10])
result = tf.add(x1,x2)
print(result)
print(type(result))
print(tf.__version__)