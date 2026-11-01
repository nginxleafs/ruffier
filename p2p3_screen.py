from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

import instructions
from theme import *


class P2P3Screen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        p2p3_label = Label(text=instructions.txt_test3)
        self.p2_input = TextInput(
            hint_text="За первые 15 секунд", background_color=input_color
        )
        self.p3_input = TextInput(
            hint_text="За последние 15 секунд", background_color=input_color
        )
        p2p3_btn = Button(
            text="Продолжить",
            on_press=self.on_press,
            background_color=button_color,
            color=text_color,
        )

        p2p3_form = BoxLayout(
            orientation="vertical",
            size_hint=(None, None),
            size=(300, 150),
            spacing=10,
            pos_hint={"center_x": 0.5},
        )
        p2p3_form.add_widget(self.p2_input)
        p2p3_form.add_widget(self.p3_input)
        p2p3_form.add_widget(p2p3_btn)

        root = BoxLayout(orientation="vertical", padding=20, spacing=20)
        root.add_widget(p2p3_label)
        root.add_widget(p2p3_form)

        self.add_widget(root)

    def on_press(self, instance):
        try:
            App.get_running_app().data["p2"] = int(self.p2_input.text)
            App.get_running_app().data["p3"] = int(self.p3_input.text)
            self.manager.current = "Result"

        except ValueError:
            return
