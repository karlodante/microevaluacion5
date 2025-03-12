from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.graphics import Triangle , Color

class TrianguloWidget(Widget):
    def __init__(self, **kwargs ):
        super().__init__(**kwargs)
        with self.canvas:

            Color(0,1,0,1)

            Triangle(points=[100,100,200,300,300,100])

class TrianguloApp(App):
    def build(self):

        return TrianguloWidget()
    
if __name__== "__main__":
    TrianguloApp().run()