from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class MyLayout(BoxLayout):
    ti_fp = ObjectProperty(None)
    ti_cp = ObjectProperty(None)
    ti_cper = ObjectProperty(None)

    def click(self):
        self.ti_cper.text = str(int(self.ti_fp.text) + int(self.ti_cp.text))
        self.ti_fp.text = ""
        self.ti_cp.text = ""


class MyKivy(App):
    def build(self):
        return MyLayout()


MyKivy().run()
