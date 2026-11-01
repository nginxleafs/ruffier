from typing import override

from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

from theme import text_color
from ruffier import test


class ResultScreen(Screen):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        screen5 = Screen(name="Result")
        result_form = BoxLayout(orientation="vertical", padding=20, spacing=20)
        self.result_label = Label(text="", color=text_color)
        result_form.add_widget(self.result_label)
        self.add_widget(result_form)

    @override
    def on_enter(self, *args):
        p1 = App.get_running_app().data["p1"]
        p2 = App.get_running_app().data["p2"]
        p3 = App.get_running_app().data["p3"]
        age = App.get_running_app().data["age"]

        self.result_label.text = test(p1, p2, p3, age)
