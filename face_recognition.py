# Import necessary libraries
import cv2
from fer import FER

# Initialize the FER model
emotion_detector = FER()

# Start video capture from webcam
cam = cv2.VideoCapture(0)

# Define font style for displaying text on the screen
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    # Capture frame-by-frame
    ret, frame = cam.read()

    # Convert the captured frame to RGB (FER requires RGB images)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect emotions in the current frame
    result = emotion_detector.detect_emotions(rgb_frame)

    # Loop through detected faces and their emotions
    for face in result:
        # Get the bounding box for the detected face
        (x, y, w, h) = face["box"]

        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Get the most dominant emotion and its confidence score
        emotion, confidence = max(face["emotions"].items(), key=lambda item: item[1])

        # Display the emotion and confidence on the frame
        text = f"{emotion}: {confidence*100:.2f}%"
        cv2.putText(frame, text, (x, y-10), font, 0.9, (255, 255, 255), 2)

    # Display the resulting frame
    cv2.imshow('Emotion Detector', frame)

    # Press 'q' to exit the video window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close windows
cam.release()
cv2.destroyAllWindows()
