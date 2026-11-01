from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from kivy.core.window import Window

import instructions
import ruffier
from seconds import Timer

from kivy.animation import Animation

button_color = "#A53860"
input_color = "#DA627D"
window_color = "#450920"
text_color = "#F9DBBD"
button_anim = Animation(size=(200, 200), duration=0.1)


class Application(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.sm = ScreenManager()
        self.data = {"name": "", "p1": 0, "p2": 0, "p3": 0}
        self.window = Window.clearcolor = window_color

        screen1 = Screen()

        # ------------------------ SCREEN 1 -----------------------------------------
        screen1 = Screen(name="StartScreen")
        greeting = Label(
            text=instructions.txt_instruction,
            size_hint_y=None,
            halign="center",
            valign="middle",
            color=text_color,
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

        self.name_input = TextInput(
            hint_text="Введите имя",
            multiline=False,
            background_color=input_color,
        )
        self.age_input = TextInput(
            hint_text="Введите возраст",
            multiline=False,
            background_color=input_color,
        )
        self.btn_start = Button(
            text="Начать",
            on_press=self.on_startscreen_progress,
            background_color=button_color,
        )

        form.add_widget(self.name_input)
        form.add_widget(self.age_input)
        form.add_widget(self.btn_start)

        root = BoxLayout(orientation="vertical", padding=20, spacing=20)
        root.add_widget(greeting)
        root.add_widget(form)

        screen1.add_widget(root)
        self.sm.add_widget(screen1)

        # ------------------------ SCREEN 2 -----------------------------------------
        screen2 = Screen(name="P1")
        p1_label = Label(
            text=instructions.txt_test1,
            halign="center",
            valign="middle",
            size_hint_y=None,
            color=text_color,
        )

        p1_label.bind(width=lambda inst, w: setattr(inst, "text_size", (w, None)))
        p1_label.bind(texture_size=lambda inst, ts: setattr(inst, "height", ts[1]))
        self.p1_input = TextInput(
            hint_text="Введите пульс", multiline=False, background_color=input_color
        )

        p1_button = Button(
            text="Продолжить",
            on_press=self.on_p1_progress,
            background_color=button_color,
            color=text_color,
        )

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

        screen2.add_widget(p1_root)
        self.sm.add_widget(screen2)

        # ------------------------ SCREEN 3 -----------------------------------------

        screen3 = Screen(name="Squats")

        squats_button = Button(
            text="Продолжить",
            disabled=True,
            on_press=lambda x: setattr(self.sm, "current", "P2P3"),
            background_color=button_color,
            color=text_color,
        )

        squats_label = Label(
            text=instructions.txt_sits,
            size_hint_y=None,
            valign="middle",
            halign="center",
            color=text_color,
        )
        self.squats_timer = Timer(
            50,
            on_finish=lambda: setattr(squats_button, "disabled", False),
            size_hint_y=None,
            halign="center",
            valign="middle",
            color=text_color,
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

        screen3.add_widget(squats_root)
        self.sm.add_widget(screen3)

        # ------------------------ SCREEN 4 -----------------------------------------

        screen4 = Screen(name="P2P3")
        p2p3_label = Label(text=instructions.txt_test3)
        self.p2_input = TextInput(
            hint_text="За первые 15 секунд", background_color=input_color
        )
        self.p3_input = TextInput(
            hint_text="За последние 15 секунд", background_color=input_color
        )
        p2p3_btn = Button(
            text="Продолжить",
            on_press=self.on_p1p2_progress,
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

        screen4.add_widget(root)

        self.sm.add_widget(screen4)

        # ------------------------ SCREEN 5 -----------------------------------------

        screen5 = Screen(name="Result")
        result_form = BoxLayout(orientation="vertical", padding=20, spacing=20)
        self.result_label = Label(text="", color=text_color)
        result_form.add_widget(self.result_label)

        screen5.add_widget(result_form)
        self.sm.add_widget(screen5)

        return self.sm

    def on_startscreen_progress(self, instance):
        try:
            self.user_name = self.name_input.text
            self.user_age = int(self.age_input.text)
            button_anim.start(self.btn_start)
            if self.user_age > 6 and self.user_age < 18:
                # button_anim.start(self.window)
                setattr(self.sm, "current", "P1")
            else:
                self.age_input.text = ""
                self.age_input.hint_text = "Тест проходят с 7 по 17 лет"
        except ValueError:
            self.age_input.text = ""
            self.age_input.hint_text = "Введите чётное число"
            return

    def on_p1_progress(self, instance):
        try:
            self.p1 = int(self.p1_input.text)
            setattr(self.sm, "current", "Squats")
            self.squats_timer.start()
        except ValueError:
            return

    def on_p1p2_progress(self, instance):
        try:
            self.p2 = int(self.p1_input.text)
            self.p3 = int(self.p2_input.text)
            self.result_label.text = ruffier.test(
                self.p1, self.p2, self.p3, self.user_age
            )
            setattr(self.sm, "current", "Result")

        except ValueError:
            return


Application().run()
