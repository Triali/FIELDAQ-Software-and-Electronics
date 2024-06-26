"""
This screen makes sure that the user will not accidentally archive stored tests on the device. It is quite simple
with only two buttons, archive and cancel. The position and type of button is intentionally different than the previous
set of buttons so it is very obvious there was a change in screen. 
"""

import os

from kivy.lang import Builder

from util.BaseScreen import BaseScreen
from os import listdir
from os.path import isfile, join
from util.getKVPath import getKVPath

Builder.load_file(getKVPath(os.getcwd(), __file__))

class ARM_TestArchiveConfirmation(BaseScreen):
    def on_pre_enter(self):
        self.test_filenames = [f for f in listdir("Tests") if (isfile(join("Tests", f)) and f != ".gitignore")]

    def archive_all(self):
        for name in self.test_filenames:
            if name != '.gitignore':
                os.rename('Tests/' + name, 'TestArchive/' + name)
        super(ARM_TestArchiveConfirmation, self).back()

    def cancel(self):
        super(ARM_TestArchiveConfirmation, self).back()