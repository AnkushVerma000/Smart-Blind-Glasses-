import cv2
import numpy as np
import tensorflow as tf
import cv2
import urllib.request

# Download the Haar Cascade classifier file
url = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"
urllib.request.urlretrieve(url, "haarcascade_frontalface_default.xml")


# Load the Haar Cascade classifier file
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")




# Load the pre-trained gender classification model
gender_model = tf.keras.models.load_model('D:\Downloads\Smart-Glasses-main\Smart-Glasses-main\model.h5')


# Define a function to predict the gender of a face
def predict_gender(face_image):
    # Resize the face image to 64x64 pixels
    face_image = cv2.resize(face_image, (64, 64))
    # Convert the face image to a grayscale image
    face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
    # Normalize the pixel values to be between 0 and 1
    face_image = face_image / 255.0
    # Reshape the image to a 4D tensor with a single channel
    face_image = np.reshape(face_image, (1, 64, 64, 1))
    # Predict the gender using the pre-trained model
    gender_prediction = gender_model.predict(face_image)[0]
    # Convert the prediction to a string ("Male" or "Female")
    gender = "Male" if gender_prediction < 0.5 else "Female"
    return gender

# Open the video capture device
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the video stream
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # For each detected face, predict the gender and print the result
    for (x, y, w, h) in faces:
        # Extract the face region from the frame
        face_image = frame[y:y+h, x:x+w]
        # Predict the gender of the face
        gender = predict_gender(face_image)
        # Draw a rectangle around the face and print the gender result
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, gender, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the frame with the detected faces and gender results
    cv2.imshow('frame', frame)

    # Wait for a key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture device and close all windows
cap.release()
cv2.destroyAllWindows()
