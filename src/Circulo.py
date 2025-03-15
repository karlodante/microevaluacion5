from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class CircleWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(0, 1, 0, 1)  # Color verde (RGBA)
            self.circle = Ellipse(pos=self.center, size=(200, 200))
        self.bind(pos=self.update_circle, size=self.update_circle)
    
    def update_circle(self, *args):
        self.circle.pos = (self.center_x - 100, self.center_y - 100)  # Centrar el círculo

class CircleApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        widget = CircleWidget()
        label = Label(text='Hasta luego Ing\nGracias por todo\nBuen módulo\nSe cuida', 
                      color=(1, 1, 1, 1), font_size='20sp', bold=True)
        layout.add_widget(widget)
        layout.add_widget(label)
        return layout

if __name__ == "__main__":
    CircleApp().run()
