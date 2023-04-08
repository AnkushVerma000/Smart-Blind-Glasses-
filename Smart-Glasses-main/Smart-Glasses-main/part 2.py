
# import library to speech conversion
from gtts import gTTS

# play the converted audio
import os

# The text that you want to convert to audio
mytext = 'Ready to develop smart glasses'

# Language in which you want to convert text
language = 'en'

# Passing the text and language to the engine,
#  module that the converted text into audio
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
myobj.save("welcome.mp3")

# Playing the converted file
os.system("welcome.mp3")
