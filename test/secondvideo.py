from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class DemoApp(MDApp):
    def build(self):
        label = MDLabel(text="HELLO SIR YOUR COMPUTER HAVE A VIRuuOS",
                        halign="center", theme_text_color="Custom", text_color=(0, 0, 1, 1), font_style="H1")
        return label


kek = DemoApp()
kek.run()
