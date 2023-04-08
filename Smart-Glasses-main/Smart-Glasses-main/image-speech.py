import cv2 as cv
from cv2 import *
  
# initialize the camera
# If you have multiple camera connected with 
# current device, assign a value in cam_port 
# variable according to that
cam = cv.VideoCapture(0)
# reading the input using the camera
result, image = cam.read()
  
# If image will detected without any error, 
# show result
if result:
  
    # showing result, it take frame name and image 
    # output
    cv.imshow("Sample", image)
  
    # saving image in local storage
    cv.imwrite("Sample.png", image)
  
    # If keyboard interrupt occurs, destroy image 
    # window
    cv.waitKey(0)
    
  
# If captured image is corrupted, moving to else part
else:
    cv.print("No image detected. Please! try again")
    
    
import pytesseract

# adds image processing capabilities
from PIL import Image
# import library to speech conversion
from gtts import gTTS

# play the converted audio
import os


# opening an image from the source path
img = Image.open('Sample.png')

# describes image format in the output
print(img)
# path where the tesseract module is installed
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR/tesseract.exe'
# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)
# write text in a text file and save it to source path
with open('abc.txt', mode='w', encoding="utf-8") as file:
    file.write(result)
    print(result)

# Language in which you want to convert text
language = 'en'

# Passing the text and language to the engine,
#  module that the converted text into audio
myobj = gTTS(text=result, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
myobj.save("welcome.mp3")

# Playing the converted file
os.system("welcome.mp3")


