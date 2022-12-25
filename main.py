# Building a basic gui app in python
from time import time
import warnings
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
warnings.simplefilter("ignore")

class MyApp(App):
    """This is a MyApp class which builds the gui for an app"""
    def build(self):
        """The build method builds the gui components of an app"""
        layout = FloatLayout()
        img =  Image(source = '/home/rohanoxob/My2DGame/opp_promo_traveler.png',size_hint = (1,5),pos_hint = {'center_x': 0.5, 'center_y': 0.7})
        label = Label(text = "Welocme to my App Rohan",size_hint = (1,1),pos_hint = {'center_x': 0.5, 'center_y': 0.3})
        layout.add_widget(img)
        layout.add_widget(label)
        return layout

def main():
    """This is a main method"""
    try:
       app = MyApp()
       app.run()
    except Exception as e:
        print("Failed to open the app: "+str(e))

        
if __name__ == "__main__":
    try:
        t1 = time()
        main()
    
    except (KeyboardInterrupt,Exception) as e:
        print("Sorry there was an error in your code: "+str(e))
    
    finally:
        t2 = time() - t1
        print("[Finished in: "+str(round(t2,3))+" sec]")