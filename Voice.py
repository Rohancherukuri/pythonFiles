
# Using female voice in pyttsx3

import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)