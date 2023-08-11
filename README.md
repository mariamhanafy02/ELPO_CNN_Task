# Sign Language Detection for 10 Words using CNN and ResNet 🪧🖖


This GitHub project aims to demonstrate the implementation of a sign language detection system capable of recognizing 10 different words: hello, love, morning, drink, help, eat, okay, thank you, please, and stop. The system utilizes Convolutional Neural Networks (CNNs) and Residual Networks (ResNet) for accurate classification and has been integrated into a real-time detection application using OpenCV.

## Table of Contents 📄

- [Introduction](#introduction)
- [Approaches](#approaches)
  - [Edge Detection with CNN](#edge-detection-with-cnn)
  - [CNN](#cnn)
  - [ResNet](#resnet)
- [Real-time Detection with OpenCV](#real-time-detection-with-opencv)
- [Usage](#usage)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)

## Introduction ✨

Sign language is an essential form of communication for people with hearing impairments. This project tackles the challenge of developing a system that can recognize a set of 10 common sign language words. The system employs deep learning techniques and computer vision to achieve accurate classification and real-time detection.

## Approaches ✨

### Edge Detection with CNN 1️⃣

This initial approach used edge detection techniques in combination with a Convolutional Neural Network (CNN). However, the accuracy achieved was only 9%, indicating the limitations of this method in accurately distinguishing between the different signs.

### CNN 2️⃣

The second approach focused solely on using a CNN for classification. This approach led to a significant improvement in accuracy, reaching 64%. The CNN was able to learn relevant features from the raw image data, contributing to improved recognition.

### ResNet 3️⃣

The most successful approach utilized a Residual Network (ResNet). With its deeper architecture and skip connections, the ResNet achieved an impressive accuracy of 84%. This performance demonstrates the power of deeper networks in capturing intricate patterns in sign language gestures.

## Real-time Detection with OpenCV ✨

To make the sign language detection practical and user-friendly, the project integrates the trained ResNet model into a real-time detection application using OpenCV. This allows users to interact with the system in real-time through their device's camera, making it suitable for various applications, such as communication tools and educational resources.

## Usage ✨

1. Clone the repository: `git clone https://github.com/yourusername/sign-language-detection.git`
2. Navigate to the project file and run : `Sign_Language_CNN`
3. Run the real-time detection application: `main.py`

## Installation ✨

1. Install the required dependencies using pip:
   ```
   pip install tensorflow opencv-python
   ```

2. Make sure you have Python 3.x installed on your system.