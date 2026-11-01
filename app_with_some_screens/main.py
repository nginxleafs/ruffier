from typing import override

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class ScrButton(Button):
    def __init__(self, sm: ScreenManager, screen: str, **kwargs):
        super().__init__(on_press=lambda x: setattr(sm, "current", screen), **kwargs)
        self.text = screen


class Application(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        sm = ScreenManager()
        scr_list = []
        for s in range(4):
            scr_list.append(Screen(name=f"scr{s + 1}"))

        for s in scr_list:
            label_l = BoxLayout(orientation="vertical")
            label_b = BoxLayout(orientation="vertical")
            for b in range(3):
                label_b.add_widget(ScrButton(sm, f"scr{b + 1}"))
            label = Label(text="Выбери экран")
            label_l.add_widget(label)
            s.add_widget(label_b)
            s.add_widget(label_l)
            sm.add_widget(s)

        return sm


Application().run()
