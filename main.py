from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class DemoApp(MDApp):
    def build(self):
        first_lable= MDLabel(text='UserName',halign='center',theme_Text_color='Error')
        return first_lable

DemoApp().run()
