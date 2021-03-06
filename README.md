# mnist-number-classification

[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://opensource.org/licenses/MIT)

This is a Convolutional Neural Network model trained with the [MNIST Dataset](https://en.wikipedia.org/wiki/MNIST_database) of handwritten digits and 
this model was implemented to support the [CoreML-MNIST](https://github.com/LucianoPAlmeida/CoreML-MNIST) Demo Application.

## Tools
* [Tensorflow 1.8](https://www.tensorflow.org/)
* [tf-coreml](https://github.com/tf-coreml/tf-coreml) 
* [coremltools](https://github.com/apple/coremltools)
* [Jupyter Notebook](http://jupyter.org/)
* [Python 3.6](https://www.python.org/)
* [matplotlib](https://matplotlib.org/)

## The Model 
The model was trainned with 70 epochs with a batch size of 512. Achieving 0.984400 of validation accuracy and 0.9861225328947368 of test accuracy.
The [AdamOptimizer](https://www.tensorflow.org/api_docs/python/tf/train/AdamOptimizer) was used to train this network with a learning rate of 0.00001.

### Architecture 
 * conv2d with filter size 32, strides 5, padding same and relu activation
 * max_pooling2d with pool size of 2 and strides 2
 * conv2d with filter size 64, strides 5, padding same and relu activation
 * max_pooling2d with pool size of 2 and strides 2
 * fully_connected with number of outputs 1024 and relu activation
 * fully_connected with number of outputs 10 and no activation function
 * softmax activation layer

## The CoreML Model

With a trained model and saved .pb file, tf-coreml was used generate a CoreML model. 
The code is available on [coreml_converter.py](https://github.com/LucianoPAlmeida/mnist-number-classification/blob/master/coreml_converter.py)

## Credits and Thanks

- [Udacity](https://www.udacity.com) for their awesome [Deep Learning Nanodegree Foundation](https://www.udacity.com/course/deep-learning-nanodegree--nd101) course.


## Licence 

mnist-number-classification is released under the [MIT License](https://opensource.org/licenses/MIT).
