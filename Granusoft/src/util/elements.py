from kivy.lang import Builder

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from util.getKVPath import getKVPath
import os

Builder.load_file(getKVPath(os.getcwd(), __file__))
class GranuContainer(BoxLayout):
    pass

class GranuSideArea(GridLayout):
    pass

class SettingsButton(Button):
	pass

class GranuSideButton(SettingsButton):
	pass

class GranuNoteButton(Button):
	pass

class GranuNone(Widget):
    pass

class GranuContent(BoxLayout):
    pass

class GranuTitle(Label):
    pass

class GranuSideAreaTest(GridLayout):
    pass