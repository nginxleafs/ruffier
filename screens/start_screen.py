from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.app import App

import instructions
from theme import *

class StartScreen(Screen):
    def __init__(self, **kw):
        super().__init__(name="StartScreen", **kw)
        greeting = Label(
            text=instructions.txt_instruction,
            size_hint_y=None,
            halign="center",
            valign="middle",
            color=text_color
        )
        greeting.bind(width=lambda inst, w: setattr(inst, "text_size", (w, None)))
        greeting.bind(texture_size=lambda inst, ts: setattr(inst, "height", ts[1]))
         

        form = BoxLayout(
            orientation="vertical",
            size_hint=(None, None),
            size=(300, 150),
            spacing=10,
            pos_hint={"center_x": 0.5},
        )

        self.name_input = TextInput(hint_text="Введите имя", multiline=False, background_color=input_color)
        self.age_input = TextInput(hint_text="Введите возраст", multiline=False, background_color=input_color)
        btn_start = Button(text="Начать", on_press=self.on_press, background_color=button_color)

        form.add_widget(self.name_input)
        form.add_widget(self.age_input)
        form.add_widget(btn_start)

        root = BoxLayout(orientation="vertical", padding=20, spacing=20)
        root.add_widget(greeting)
        root.add_widget(form)
        self.add_widget(root)

    def on_press(self, instance):
        try:
            self.user_age = int(self.age_input.text)
            if self.user_age > 6 and self.user_age < 18:
                App.get_running_app().data["age"] = self.user_age
                self.name_input.text = ""
                self.age_input.text = ""
                self.manager.current = "P1"
            else:
                self.age_input.text = ""
                self.age_input.hint_text = "Тест проходят с 7 по 17 лет"
        except ValueError:
            self.age_input.text = ""
            self.age_input.hint_text = "Введите чётное число"
            return
