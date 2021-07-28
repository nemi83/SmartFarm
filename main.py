from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
import mysql.connector as connection
import pandas as pd
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

# Connect to database and get data (change database connection to fit your database
def get_data_air():
    mydb = connection.connect(host='localhost', port='XX', database='DATABASE_NAME', user='username', passwd='password')
    query_air = "Select * from temp;"
    result_dfAir = pd.read_sql(query_air, mydb)
    query_humid = "Select * from humid;"
    result_dfHumid = pd.read_sql(query_humid, mydb)
    query_ph = "Select * from ph;"
    result_dfPh = pd.read_sql(query_ph, mydb)
    mydb.close()
    return (result_dfAir, result_dfHumid, result_dfPh)

# Class related to displaying air temperature data in application
class MyGraphAirTemp(StackLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = data_air
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlabel('Date')
        self.ax.set_ylabel('Air temperature')
        self.ax.set_title('Smart Farm')
        self.ax.grid(True)
        self.data.plot(x='temp_date', y='temp_temp', ax=self.ax, label='Temperature')
        self.ax.legend()
        self.widget = FigureCanvasKivyAgg(self.fig)
        self.add_widget(self.widget)

    def update_day(self):
        self.remove_widget(self.widget)
        if len(data_air) <= 48:
            self.data_day = data_air
        elif len(data_air) > 48:
            self.data_day = data_air.tail(48)
        self.fig, self.ax = plt.subplots()
        self.data_day.plot(x='temp_date', y='temp_temp', ax=self.ax, label='Temperature')
        self.widget = FigureCanvasKivyAgg(self.fig)
        self.add_widget(self.widget)

    def update_week(self):
        self.remove_widget(self.widget)
        if len(data_air) <= 336:
            self.data_day = data_air
        elif len(data_air) > 336:
            self.data_day = data_air.tail(336)
        self.fig, self.ax = plt.subplots()
        self.data_day.plot(x='temp_date', y='temp_temp', ax=self.ax, label='Temperature')
        self.widget = FigureCanvasKivyAgg(self.fig)
        self.add_widget(self.widget)

    def update_month(self):
        self.remove_widget(self.widget)
        if len(data_air) <= 1440:
            self.data_day = data_air
        elif len(data_air) > 1440:
            self.data_day = data_air.tail(1440)
        self.fig, self.ax = plt.subplots()
        self.data_day.plot(x='temp_date', y='temp_temp', ax=self.ax, label='Temperature')
        self.widget = FigureCanvasKivyAgg(self.fig)
        self.add_widget(self.widget)

# Class related to displaying air humidity data in application
class MyGraphAirHumid(StackLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = data_air
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlabel('Date')
        self.ax.set_ylabel('Air humidity')
        self.ax.set_title('Smart Farm')
        self.ax.grid(True)
        self.data.plot(x='temp_date', y='temp_humid', ax=self.ax, label='Humidity')
        self.ax.legend()
        self.widget = FigureCanvasKivyAgg(self.fig)
        self.add_widget(self.widget)

    def update_day(self):
        self.remove_widget(self.widget)
        if len(data_air) <= 48:
            self.data_day = data_air
        elif len(data_air) > 48:
            self.data_day = data_air.tail(48)
        self.fig, self.ax = plt.subplots()
        self.data_day.plot(x='temp_date', y='temp_humid', ax=self.ax, label='Humidity')
        self.widget = FigureCanvasKivyAgg(self.fig)
        self.add_widget(self.widget)

    def update_week(self):
        self.remove_widget(self.widget)
        if len(data_air) <= 336:
            self.data_day = data_air
        elif len(data_air) > 336:
            self.data_day = data_air.tail(336)
        self.fig, self.ax = plt.subplots()
        self.data_day.plot(x='temp_date', y='temp_humid', ax=self.ax, label='Humidity')
        self.widget = FigureCanvasKivyAgg(self.fig)
        self.add_widget(self.widget)

    def update_month(self):
        self.remove_widget(self.widget)
        if len(data_air) <= 1440:
            self.data_day = data_air
        elif len(data_air) > 1440:
            self.data_day = data_air.tail(1440)
        self.fig, self.ax = plt.subplots()
        self.data_day.plot(x='temp_date', y='temp_humid', ax=self.ax, label='Humidity')
        self.widget = FigureCanvasKivyAgg(self.fig)
        self.add_widget(self.widget)

# Class related to displaying soil humidity data in application
class MyGraphSoilHumid(StackLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = data_soilHumid
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlabel('Date')
        self.ax.set_ylabel('Soil humidity')
        self.ax.set_title('Smart Farm')
        self.ax.grid(True)
        self.data.plot(x='humid_date', y='humid_humid', ax=self.ax, label='Humidity')
        self.ax.legend()
        self.widget = FigureCanvasKivyAgg(self.fig)
        self.add_widget(self.widget)

    def update_day(self):
        self.remove_widget(self.widget)
        if len(data_soilHumid) <= 48:
            self.data_day = data_soilHumid
        elif len(data_soilHumid) > 48:
            self.data_day = data_soilHumid.tail(48)
        self.fig, self.ax = plt.subplots()
        self.data_day.plot(x='humid_date', y='humid_humid', ax=self.ax, label='Humidity')
        self.widget = FigureCanvasKivyAgg(self.fig)
        self.add_widget(self.widget)

    def update_week(self):
        self.remove_widget(self.widget)
        if len(data_soilHumid) <= 336:
            self.data_day = data_soilHumid
        elif len(data_soilHumid) > 336:
            self.data_day = data_soilHumid.tail(336)
        self.fig, self.ax = plt.subplots()
        self.data_day.plot(x='humid_date', y='humid_humid', ax=self.ax, label='Humidity')
        self.widget = FigureCanvasKivyAgg(self.fig)
        self.add_widget(self.widget)

    def update_month(self):
        self.remove_widget(self.widget)
        if len(data_soilHumid) <= 1440:
            self.data_day = data_soilHumid
        elif len(data_soilHumid) > 1440:
            self.data_day = data_soilHumid.tail(1440)
        self.fig, self.ax = plt.subplots()
        self.data_day.plot(x='humid_date', y='humid_humid', ax=self.ax, label='Humidity')
        self.widget = FigureCanvasKivyAgg(self.fig)
        self.add_widget(self.widget)

# Class related to displaying soil PH data in application
class MyGraphSoilPh(StackLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = data_soilPh
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlabel('Date')
        self.ax.set_ylabel('Soil Ph')
        self.ax.set_title('Smart Farm')
        self.ax.grid(True)
        self.data.plot(x='ph_date', y='ph_ph', ax=self.ax, label='Ph')
        self.ax.legend()
        self.widget = FigureCanvasKivyAgg(self.fig)
        self.add_widget(self.widget)

    def update_day(self):
        self.remove_widget(self.widget)
        if len(data_soilPh) <= 48:
            self.data_day = data_soilPh
        elif len(data_soilPh) > 48:
            self.data_day = data_soilPh.tail(48)
        self.fig, self.ax = plt.subplots()
        self.data_day.plot(x='ph_date', y='ph_ph', ax=self.ax, label='Ph')
        self.widget = FigureCanvasKivyAgg(self.fig)
        self.add_widget(self.widget)

    def update_week(self):
        self.remove_widget(self.widget)
        if len(data_soilPh) <= 336:
            self.data_day = data_soilPh
        elif len(data_soilPh) > 336:
            self.data_day = data_soilPh.tail(336)
        self.fig, self.ax = plt.subplots()
        self.data_day.plot(x='ph_date', y='ph_ph', ax=self.ax, label='Ph')
        self.widget = FigureCanvasKivyAgg(self.fig)
        self.add_widget(self.widget)

    def update_month(self):
        self.remove_widget(self.widget)
        if len(data_soilPh) <= 1440:
            self.data_day = data_soilPh
        elif len(data_soilPh) > 1440:
            self.data_day = data_soilPh.tail(1440)
        self.fig, self.ax = plt.subplots()
        self.data_day.plot(x='ph_date', y='ph_ph', ax=self.ax, label='Ph')
        self.widget = FigureCanvasKivyAgg(self.fig)
        self.add_widget(self.widget)

class Content(BoxLayout):
    pass

class SmartFarm(MDApp):
    dialog = None
    global data_air
    global data_soilHumid
    global data_soilPh
    data_air, data_soilHumid, data_soilPh = get_data_air()

    zalivam = "No watering"
    temp = str(data_air['temp_temp'].iloc[-1])
    humid = str(data_air['temp_humid'].iloc[-1])
    date = str(data_air['temp_date'].iloc[-1])
    soilHumid = str(data_soilHumid['humid_humid'].iloc[-1])
    soilPh = str(data_soilPh['ph_ph'].iloc[-1])

    def action(self):
        # action script invoked for zalivam
        if not self.dialog:
            self.dialog = MDDialog(
                title="Watering:",
                type="custom",
                content_cls=Content(),
                buttons= [MDFlatButton(text="STOP", text_color=self.theme_cls.primary_color, on_release=self.grabText),
                ],
            )
        self.dialog.set_normal_height()
        self.dialog.open()

    def grabText(self, inst):
        for obj in self.dialog.content_cls.children:
            if isinstance(obj, MDTextField):
                print(obj.text)
        self.dialog.dismiss()

    def closeDialog(self, inst):
        self.dialog.dismiss()

    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file('smartFarm.kv')

if __name__ == '__main__':
    SmartFarm().run()

