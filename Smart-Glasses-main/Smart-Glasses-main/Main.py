import cv2
import pytesseract
from PIL import Image
import pyttsx3
from gtts import gTTS

# Initialize the pytesseract OCR engine
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR/tesseract.exe'

# Initialize the pyttsx3 text-to-speech engine
engine = pyttsx3.init()

# Open the video capture device
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the video stream
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply a threshold to the grayscale image to binarize it
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Convert the binary image to a Pillow Image object
    img = Image.fromarray(thresh)

    # Use OCR to extract text from the image
    text = pytesseract.image_to_string(img)

    # Print the extracted text
    print(text)

    # Speak the extracted text
    language = 'en'
    myobj = gTTS(text=text, lang=language, slow=False)
    engine.runAndWait()

    # Display the frame with the detected text
    cv2.imshow('frame', thresh)

    # Wait for a key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture device and close all windows
cap.release()
cv2.destroyAllWindows()
