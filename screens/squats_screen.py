from typing import override

from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

import instructions
from seconds import Timer
from theme import button_color, text_color


class SquatsScreen(Screen):
    def __init__(self, **kw):
        super().__init__(name="Squats", **kw)

        squats_button = Button(
            text="Продолжить",
            disabled=True,
            on_press=lambda x: setattr(self.manager, "current", "P2P3"),
            background_color=button_color
        )

        squats_label = Label(
            text=instructions.txt_sits,
            size_hint_y=None,
            valign="middle",
            halign="center",
            color=text_color
        )
        self.squats_timer = Timer(
            50,
            on_finish=lambda: setattr(squats_button, "disabled", False),
            size_hint_y=None,
            halign="center",
            valign="middle",
            color=text_color
        )

        squats_label.bind(width=lambda inst, w: setattr(inst, "text_size", (w, None)))
        self.squats_timer.bind(
            texture_size=lambda inst, ts: setattr(inst, "height", ts[1])
        )

        squats_form = BoxLayout(
            orientation="vertical",
            size_hint=(None, None),
            size=(300, 150),
            spacing=10,
            pos_hint={"center_x": 0.5},
        )
        squats_form.add_widget(squats_button)

        squats_root = BoxLayout(orientation="vertical", padding=20, spacing=20)
        squats_root.add_widget(squats_label)
        squats_root.add_widget(self.squats_timer)
        squats_root.add_widget(squats_form)

        self.add_widget(squats_root)

    def on_enter(self, *args):
        self.squats_timer.start()
