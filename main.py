from kivymd.app import MDApp

from kivy.lang import Builder
#from kivy.properties import ObjectProperty

from kivy.uix.boxlayout import BoxLayout

class ContentNavigationDrawer(BoxLayout):
    pass


class TestNavigationDrawer(MDApp):
    def build(self):
        return Builder.load_file('TestNavigationDrawer.kv')


TestNavigationDrawer().run()