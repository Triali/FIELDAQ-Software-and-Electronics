"""
An input text box that, when selected, allows the user to type in the current Plot
setting via a touch screen number pad that will pop up. The value in the input text box
when you first visit this view is whatever value for the Plot setting is currently stored
in our settings file.
"""

from kivy.lang import Builder

import Devices.Arm.Settings.configurator as config
from util.BaseScreen import BaseScreen
from util.input.IntInput import IntInput
from util.getKVPath import getKVPath
import os

Builder.load_file(getKVPath(os.getcwd(), __file__))

class ARM_PlotScreen(BaseScreen):
    def on_pre_enter(self):
        """Before the Screen loads, read the configuration file to get the current
        plot number."""
        input = self.ids['plot_num']
        input.text = str(config.get('plot_num', 1))
        input.validate()

    def on_enter(self):
        """Once the Screen loads, focus the TextInput"""
        input = self.ids['plot_num']
        input.focus = True
        #input.select_all()

    def save(self):
        """Save button was pressed: save the new height in the configuration file.
        Returns True if save was successful.  False otherwise."""
        input = self.ids['plot_num']
        valid = input.validate()
        if valid:
            config.set('plot_num', int(input.text))
            config.set('curr_test_num', 0)
            return True
        else:
            input.focus = True
            return False
