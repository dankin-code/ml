# pg 427
#import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

import numpy as np

X_train = np.arange(10).reshare((10,1))
Y_train = np.array([1.0, 1.3, 3.1, 2.0, 5.0, 6.3, 6.6,7.4, 8.0, 9.0])

# train a linear regression model to predict the output

class TFLinreg(object):
    =000