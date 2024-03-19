"""
Shows all data: Temperature, Humidity, Location, Time, and all Sensor data
"""

from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.clock import Clock
from Devices.Rodney.Sensors import Sensor
import datetime

from util.BaseScreen import BaseScreen
from util.elements import *
import os
from util.getKVPath import getKVPath
Builder.load_file(getKVPath(os.getcwd(), __file__))

INTERVAL = .5
SECOND_CAP = 1/INTERVAL

# FIXME: This has not been updated to show strain values, or whisker angles yet, and just has old code in it

class ROD_LiveFeedScreen(BaseScreen):
    sensor = Sensor()

    run_count = 0
    transition_to_state = StringProperty("Pause")

    time_label = StringProperty("Time")
    strainAx_label = StringProperty("Strain Ax, volts")
    strainAy_label = StringProperty("Strain Ay, volts")
    strainBx_label = StringProperty("Strain Bx, volts")
    strainBy_label = StringProperty("Strain By, volts")
    whisker_front_angle_label = StringProperty("Whisker Front \nAngle")
    whisker_back_angle_label = StringProperty("Whisker Back \nAngle")
    data_rate_label = StringProperty("Data Rate")
    current_date_label = StringProperty("Date")

    #temperature = StringProperty("0")
    time = StringProperty("00:00:00 AM")
    strainAx = StringProperty("0.00")
    strainAy = StringProperty("0.00")
    strainBx = StringProperty("0.00")
    strainBy = StringProperty("0.00")
    whisker_front_angle = StringProperty("0")
    whisker_back_angle = StringProperty("0")
    data_rate = StringProperty("0")
    current_date = StringProperty("01/01/2000")


    old_time = 0
    xUnits = " lbs"
    potUnits = u'\N{DEGREE SIGN}'
    imuUnits = u'\N{DEGREE SIGN}'
    loadCellHeightUnits = 'cm'


    def on_pre_enter(self):
        self.event = Clock.schedule_interval(self.update_values, INTERVAL)
        self.transition_to_state = "Pause"
        self.sensor.clear_gps_memory()
        self.ids['adc_button_text'].text = 'ADC\nValues'
        self.adc_out = 0

    def update_values(self, obj):

        if self.run_count >= SECOND_CAP:
            self.sensor.get_header_data()
            sensor_data = self.sensor.get_sensor_data(self.adc_out)
            self.time = datetime.datetime.now().strftime("%H:%M:%S %p")
            self.current_date = datetime.date.today().strftime("%d/%m/%Y")
            self.whsiker_front_angle = str("%.3f" % sensor_data["IMU Angle"])
            # Calculate Data Acquisition Rate
            now = datetime.datetime.now()
            new_time = (int(now.strftime("%M")) * 60) + int(now.strftime("%S")) + (int(now.strftime("%f"))/1000000)
            time_dif = new_time - self.old_time
            self.data_rate = str("%.0f" % round(SECOND_CAP/time_dif,2))
            self.old_time = new_time
            # Reset run_count
            self.run_count = 0
        else:
            sensor_data = self.sensor.get_sensor_data()
            self.run_count = self.run_count + 1

    def adc_button_press(self):
        adcButton = self.ids['adc_button_text']
        if self.adc_out == 0:
            self.adc_out = 1
            adcButton.text = 'Real\nUnits'
            self.xUnits = ""
            self.potUnits = ""
            self.imuUnits = u'\N{DEGREE SIGN}'
        else:
            self.adc_out = 0
            adcButton.text = 'ADC\nValues'
            self.xUnits = " lbs"
            self.potUnits = u'\N{DEGREE SIGN}'
            self.imuUnits = u'\N{DEGREE SIGN}'

    def on_leave(self):
        self.event.cancel()

    def transition(self):
        if(self.transition_to_state == "Pause"):
            self.event.cancel()
            self.transition_to_state = "Resume"
        else:
            self.event = Clock.schedule_interval(self.update_values, INTERVAL)
            self.transition_to_state = "Pause"
