from screens.start_screen import StartScreen
from screens.p1_screen import P1Screen
from screens.squats_screen import SquatsScreen
from screens.p2p3_screen import P2P3Screen
from screens.result_screen import ResultScreen
from kivy.core.window import Window

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from theme import window_color


class Application(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.data = {"p1": 0, "p2": 0, "p3": 0, "age": 0}
        Window.clearcolor = window_color
        self.sm = ScreenManager()
        self.sm.add_widget(StartScreen())
        self.sm.add_widget(P1Screen())
        self.sm.add_widget(SquatsScreen())
        self.sm.add_widget(P2P3Screen())
        self.sm.add_widget(ResultScreen())
        return self.sm


Application().run()
