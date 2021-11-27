from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder



username_helper="""
MDTextField:
    hint_text: "Username"
    helper_text: "Username must be at least 4 characters"
    helper_text_mode: "on_focus"
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    icon_right: "android"
    icon_right_color: app.theme_cls.primary_color
    size_hint_x: None
    width: 300
"""

password_helper="""
MDTextField:
    hint_text: "Password"
    helper_text: "Password must be at least 4 characters"
    helper_text_mode: "on_focus"

    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    icon_right: "android"
    icon_right_color: app.theme_cls.primary_color
    size_hint_x: None
    width: 300
    padding: 56, 56, 12, 16

"""

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_palette="Red"
        screen = Screen()
        username = Builder.load_string (username_helper) 
        password = Builder.load_string(password_helper)
        screen.add_widget(password)
        screen.add_widget(username)
        return screen


DemoApp().run()