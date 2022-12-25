# Automating a WhatsApp Message system using pywhatkit in python

import pywhatkit as pw
# Sending message through whatsapp in python
try:
    #pw.sendwhatmsg('+919948931020','This is my message used for automating so dont mind me.',16,18)
    pw.info("python pytorch module")
    pw.search("julia programming language")
    pw.playonyt("Ramraju for Bheem ")
except Exception as e:
    print("Sorry there was an error in your code: "+str(e))