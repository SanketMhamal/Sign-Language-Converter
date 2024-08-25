# Sign Language Conversion App

Welcome to the Sign Language Conversion App! This project enables real-time sign language to text conversion and vice versa using advanced machine learning models and computer vision techniques.

## Project Overview

The Sign Language Conversion App is designed to:
- Convert sign language gestures into text in real time.
- Convert text into animated sign language gestures.

This application utilizes deep learning models built with Keras and TensorFlow, along with computer vision tools provided by OpenCV and MediaPipe.

## Features

- **Sign Language to Text Conversion**: Recognizes hand gestures and translates them into corresponding text.
- **Text to Sign Language Conversion**: Converts input text into sign language animations.
- **Real-Time Detection**: Uses a webcam for live sign language recognition.

## Installation

To get started with this project, you'll need to install the necessary dependencies. Create a virtual environment and install the required packages using the following commands:

# Install dependencies
pip install -r requirements.txt

## Dependencies
# The required Python packages are listed in requirements.txt. Here is a summary of the main dependencies:

- numpy: For numerical operations.
- opencv-python: For computer vision tasks.
- mediapipe: For hand gesture recognition.
- keras: For building and training the deep learning model.
- tensorflow: Backend for Keras.
- scikit-learn: For data preprocessing and model evaluation.
- nltk: For text processing.


## Run the GUI application:

python gui1.py

## Training the Model
To train a new model, follow these steps:

Prepare your dataset of sign language gestures. 
Run the training script:

python train_model.py
The model will be saved as model.h5
