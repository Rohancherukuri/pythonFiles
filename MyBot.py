# Building a simple responsive chat bot in python
from nltk.chat.util import Chat,reflections
try:
    pairs =  [[r"My name is (.*)",["Hello %1. How are you doing today"]], ]

    def chatbot():
        print("Hi I am your chat bot assistant built over nltk module")
        
        chatbot = Chat(pairs, reflections)
        chatbot.converse()
except Exception as e:
    print("There is error in your code. ")
if __name__ == "__main__":
    chatbot()
