# kahs-nn
A Python, data analysis, neural network, and computer vision workshop for students at Kutztown Area High School

# Intro to Python

You can find resources for learning the syntax and basics of python in `intro_python`.

# Demos

## Data Analysis
Several demos can be found in `intro_python/demos` showing how Python is used in science for data analysis. We have a Jupyter notebook on performing text analysis in `intro_python/demos/text_analysis/moby_dick.ipynb`. Jordan provides some of his simulation code from his Physics senior thesis at Tufts University in `intro_python/demos/simulations`, along with a demonstration for using Python to work with Excel files in `intro_python/demos/excel_demo`.

## Computer Vision

Most of this work is based on [Connely Barnes'](http://www.cs.virginia.edu/~connelly/) course at the University of Virginia, [CS 4501 - Introduction to Computer Vision](http://www.cs.virginia.edu/~connelly/class/2017/intro_vision/).


### Filters and Image Processing
We have a Jupyter notebook explaining basic image processing with filters to make edge and face detectors in `cv_filters/computer_vision_filters.ipynb`.

### Neural Networks
We have a Jupyter notebook explaining how to train and use a neural network in Keras to classify handwritten digits from the MNIST dataset, found in `digits/digit_classifier.ipynb`.

We have a Jupyter notebook explaining how to use a Convolutional Neural Network to classify cat and dog images in `cats_or_dogs/cat_or_dog.ipynb`.

## Additional Resources
- **3Blue1Brown**, the YouTube channel, has produced an _**excellent**_ video series explaining neural networks ituitively. He also goes into some of the math behind why these neural networks work. [Part 1](https://www.youtube.com/watch?v=aircAruvnKk), [Part 2](https://www.youtube.com/watch?v=IHZwWFHWa-w), [Part 3](https://www.youtube.com/watch?v=Ilg3gGewQ5U), [Part 3.a](https://www.youtube.com/watch?v=tIeHLnjs5U8). 
- **Welch Labs**, another YouTube channel, produced a 15 part series on computer vision and machine learning called **Learning to See**: [Playlist](https://www.youtube.com/watch?v=i8D90DkCLhI&list=PLiaHhY2iBX9ihLasvE8BKnS2Xg8AhY6iV)


# Requirements
- [Python 3.6](https://www.python.org/downloads/)
- [Jupyter](http://jupyter.org/)

**Neural Networks**
- [Keras](https://keras.io/)
- [Tensorflow](https://www.tensorflow.org/)

**Computer Vision**
- [OpenCV](https://opencv.org/)
- [skimage](http://scikit-image.org/docs/dev/api/skimage.html)

# Installation

`pip install jupyter keras tensorflow opencv-python scikit-image`

