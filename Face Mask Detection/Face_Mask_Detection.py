import cv2
import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.models import load_model

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load the pre-trained face mask detection model
model = load_model('maskDetectionModel.h5')

# Initialize the video capture
cap = cv2.VideoCapture(0)


# Function to perform mask detection on a frame
def detect_mask(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        face = frame[y:y + h, x:x + w]
        face = cv2.resize(face, (224, 224))
        face = preprocess_input(face)

        # Predict whether the person is wearing a mask or not
        predictions = model.predict(np.expand_dims(face, axis=0))
        mask, without_mask = predictions[0]

        # Determine the label and color based on the prediction
        label = "Mask" if mask > without_mask else "Not Mask"
        color = (0, 255, 0) if label == "Mask" else (0, 0, 255)

        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

    return frame


while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Perform mask detection
    output_frame = detect_mask(frame)

    # Display the output frame
    cv2.imshow('Face Mask Detection', output_frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()
