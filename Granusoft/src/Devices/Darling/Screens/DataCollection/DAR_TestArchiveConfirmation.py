"""
This screen makes sure that the user will not accidentally archive stored tests on the device. It is quite simple
with only two buttons, archive and cancel. The position and type of button is intentionally different than the previous
set of buttons so it is very obvious there was a change in screen. 
"""

import os

from kivy.lang import Builder
from util.TestLog import TestLog
from util.BaseScreen import BaseScreen
from os import listdir
from os.path import isfile, join
from util.getKVPath import getKVPath
import os

Builder.load_file(getKVPath(os.getcwd(), __file__))

class DAR_TestArchiveConfirmation(BaseScreen):
    def on_pre_enter(self):
        self.test_filenames = [f for f in listdir("Tests") if (isfile(join("Tests", f)) and f != ".gitignore")]

    def on_enter(self):
        
        log=TestLog()
        log.connection("Entered DAR_TestArchiveConfirmation")

    def archive_all(self):
        for name in self.test_filenames:
            if name != '.gitignore':
                os.rename('Tests/' + name, 'TestArchive/' + name)
        super(DAR_TestArchiveConfirmation, self).back()

    def cancel(self):
        super(DAR_TestArchiveConfirmation, self).back()