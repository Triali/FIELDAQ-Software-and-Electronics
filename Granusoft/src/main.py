from kivy.config import Config as KivyConfig
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, FadeTransition, NoTransition
from kivy.logger import Logger,LOG_LEVELS



# Kivy Configuration

KivyConfig.set('kivy', 'desktop', 0) # Disable OS-specific features for testing
KivyConfig.set('kivy', 'keyboard_mode', 'systemanddock') # Allow barcode scanner and
                                                         # on screen keyboard
KivyConfig.set('graphics', 'height', 480) # Set window size to be the same as touchscreen
KivyConfig.set('graphics', 'width', 800)  # (not used when fullscreen enabled)
CLOCK_TYPE = "default"
KivyConfig.set('kivy', 'kivy_clock', CLOCK_TYPE)
KivyConfig.set('graphics', 'maxfps', 250)
KivyConfig.write()
Logger.setLevel(LOG_LEVELS["debug"])


class GranuScreenManager(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        sm = GranuScreenManager(transition=NoTransition())
        return sm

if __name__ == "__main__":
    import sys

    # Run the App
    try:
        MainApp().run()
    except KeyboardInterrupt:
        log.info("Closing Application...")
        sys.exit()

