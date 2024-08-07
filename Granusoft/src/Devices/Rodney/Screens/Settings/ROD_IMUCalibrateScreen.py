from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty, NumericProperty
from util.TestLog import TestLog
from Devices.Rodney.Sensors import Sensor
from util.BaseScreen import BaseScreen
from util.elements import *

from Devices.Rodney.Settings.configurator import SettingsSingleton as settings
from util.getKVPath import getKVPath
import os

Builder.load_file(getKVPath(os.getcwd(), __file__))

ONE_SEC = 1

class ROD_IMUCalibrateScreen(BaseScreen):
    offset = NumericProperty()
    real_angle = NumericProperty()
    adc_angle = NumericProperty()

    def on_pre_enter(self):
        self.event = Clock.schedule_interval(self.update_data, ONE_SEC / 2)
        self.sensor = Sensor()
        self.config = settings()
        self.config_data = self.config.get('sensors', {})
        if 'IMU Angle' in self.config_data:
            self.offset = self.config_data['IMU Angle']['offset']
        else:
            self.offset = 0

    def on_enter(self):
        
        log = TestLog()
        log.connection("Entering ROD_IMUCalibrateScreen")

    def set_to_zero(self):
        sensor_data = self.sensor.get_sensor_data(1)
        self.offset = sensor_data['IMU Angle']

    def update_data(self, obj):
        sensor_data = self.sensor.get_sensor_data(1)
        self.adc_angle = sensor_data['IMU Angle']
        self.real_angle = sensor_data['IMU Angle'] - self.offset

    def save(self):
        self.config_data['IMU Angle'] = {
            'offset': self.offset
        }
        self.config.set('sensors', self.config_data)
        self.event.cancel()
        return True
