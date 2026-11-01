from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

from theme import button_color, text_color
from ruffier import test


class ResultScreen(Screen):
    def __init__(self, **kwargs) -> None:
        super().__init__(name="Result", **kwargs)
        result_form = BoxLayout(orientation="vertical", padding=20, spacing=20)
        self.result_label = Label(text="", color=text_color)
        btn = Button(text="Пройти заново", color=text_color, background_color=button_color, on_press=self.on_press)
        result_form.add_widget(self.result_label)
        result_form.add_widget(btn)
        self.add_widget(result_form)

    def on_enter(self, *args):
        p1 = App.get_running_app().data["p1"]
        p2 = App.get_running_app().data["p2"]
        p3 = App.get_running_app().data["p3"]
        age = App.get_running_app().data["age"]

        self.result_label.text = test(p1, p2, p3, age)

    def on_press(self, instance):
        data = App.get_running_app().data
        data["p1"] = 0
        data["p2"] = 0
        data["p3"] = 0
        data["age"] = 0
        self.manager.current = "StartScreen"


