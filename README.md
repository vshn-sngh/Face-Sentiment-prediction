# Real-Time Emotion Detection System

This project is a real-time emotion detection system built using Python's OpenCV library and the `fer` package for facial emotion recognition. The system captures video from a webcam, detects faces in the video feed, and analyzes their emotions in real time.

## Overview

The emotion detection system uses a deep learning-based model from the `fer` package to recognize facial expressions. The emotions detected are displayed in real time with the corresponding confidence score. This project is suitable for demonstrating basic computer vision applications, facial recognition, and emotion analysis.

## Features

- **Real-time Emotion Detection**: Detects emotions like happiness, anger, sadness, etc., from live webcam feed.
- **Facial Recognition**: Automatically identifies and highlights faces in the video.
- **Confidence Scores**: Displays the confidence percentage of the detected emotions for each face.
- **Real-time Video Feed**: The detected emotions are superimposed on the live video feed with bounding boxes around faces.

## Technologies Used

- **Python**: Core language for implementing the system.
- **OpenCV**: For video capture and image processing.
- **FER (Facial Expression Recognition)**: Deep learning model to detect emotions from facial expressions.
- **cv2 (OpenCV)**: For handling webcam input, face detection, and drawing bounding boxes.

## Prerequisites

Ensure you have the following installed on your system:

- **Python 3.x**
- **OpenCV (`cv2`)**
- **FER library**

You can install the required dependencies by running the following commands:

```bash
pip install opencv-python
pip install fer
