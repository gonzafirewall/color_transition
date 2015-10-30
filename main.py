from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.animation import Animation

from kivy.uix.scatter import Scatter
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout


class BabyScreen(Screen):
    def __init__(self, *args, **kwargs):
        super(BabyScreen, self).__init__(*args, **kwargs)
        self.change_event = None
        self.index = 0
        self.delay = 5
        # https://simple.wikipedia.org/wiki/Rainbow
        self.rainbow_colors = [
            {'r': 1, 'g': 0, 'b': 0}, #red
            {'r': 1, 'g': 127/255., 'b': 0}, # orange
            {'r': 1, 'g': 1, 'b': 0}, # yellow
            {'r': 0, 'g': 1, 'b': 0}, # green
            {'r': 0, 'g': 0, 'b': 1}, # blue
            {'r': 75/255., 'g': 0, 'b': 130/255.}, # indigo
            {'r': 139/255., 'g': 0, 'b': 1}, # violet
        ]
        Clock.schedule_once(self.change_color, 0)
        self.change_event = Clock.schedule_interval(self.change_color, self.delay)


    def change_color(self, ev=None):
        if not hasattr(self, 'color'):
            with self.canvas.before:
                self.color = Color(**self.rainbow_colors[self.index])
                self.rect = Rectangle(size=self.size,
                                      pos=self.pos)
        self.index += 1
        if self.index > len(self.rainbow_colors) - 1:
            self.index = 0
        anim = Animation(d=self.delay, **self.rainbow_colors[self.index])
        anim.start(self.color)

class MiApp(App):
    def build(self):
        root = ScreenManager()
        root.add_widget(BabyScreen(name="Baby"))
        return root

if __name__ == "__main__":
    MiApp().run()
