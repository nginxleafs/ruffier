from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.app import App

import instructions
from theme import text_color, button_color, input_color


class P1Screen(Screen):
    def __init__(self, **kw):
        super().__init__(name="P1", **kw)

        p1_label = Label(
            text=instructions.txt_test1,
            halign="center",
            valign="middle",
            size_hint_y=None,
            color=text_color
        )
        p1_label.bind(width=lambda inst, w: setattr(inst, "text_size", (w, None)))
        p1_label.bind(texture_size=lambda inst, ts: setattr(inst, "height", ts[1]))
        self.p1_input = TextInput(hint_text="Введите пульс", multiline=False, background_color=input_color)
        p1_button = Button(text="Продолжить", on_press=self.on_press, background_color=button_color)

        p1_form = BoxLayout(
            orientation="vertical",
            size_hint=(None, None),
            size=(300, 150),
            spacing=10,
            pos_hint={"center_x": 0.5},
        )
        p1_form.add_widget(self.p1_input)
        p1_form.add_widget(p1_button)

        p1_root = BoxLayout(orientation="vertical", padding=20, spacing=20)
        p1_root.add_widget(p1_label)
        p1_root.add_widget(p1_form)

        self.add_widget(p1_root)

    def on_press(self, instance):
        try:
            App.get_running_app().data["p1"] = int(self.p1_input.text)
            self.p1_input.text = ""
            self.manager.current = "Squats"
        except ValueError:
            return
