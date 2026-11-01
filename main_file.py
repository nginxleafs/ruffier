from start_screen import StartScreen
from p1_screen import P1Screen
from squats_screen import SquatsScreen
from p2p3_screen import P2P3Screen
from result_screen import ResultScreen

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager


class Application(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.data = {"p1": 0, "p2": 0, "p3": 0, "age": 0}
        self.sm = ScreenManager()
        self.sm.add_widget(StartScreen(name="StartScreen"))
        self.sm.add_widget(P1Screen(name="P1"))
        self.sm.add_widget(SquatsScreen(name="Squats"))
        self.sm.add_widget(P2P3Screen(name="P2P3"))
        self.sm.add_widget(ResultScreen(name="Result"))
        return self.sm


Application().run()
