import kivy 
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen



class ButtonApp(App):
     
    def build(self):
        # use a (r, g, b, a) tuple
        btn = Button(text ="Push Me !",
                   font_size ="20sp",
                   background_color =(1, 1, 1, 1),
                   color =(1, 1, 1, 1),
                   size =(32, 32),
                   size_hint =(.2, .2),
                   pos =(300, 250))
 
        # bind() use to bind the button to function callback
        btn.bind(on_press = self.callback)
        btn1 = Button(text ="Push Me !",
                   font_size ="20sp",
                   background_color =(1, 1, 1, 1),
                   color =(1, 1, 1, 1),
                   size =(32, 32),
                   size_hint =(.2, .2),
                   pos =(300, 250))

        
        return btn,btn1
 
    # callback function tells when button pressed
    def callback(self, event):
        print("button pressed")
        print('Yoooo !!!!!!!!!!!')
         
 

root = ButtonApp()
 

root.run()