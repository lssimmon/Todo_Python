import kivy
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.textinput import TextInput


class todoApp(App):
    def build(self):
        TextInput(text='Hello world', multiline=False)
        return Label(text ="Hello World !") 

todoApp().run()