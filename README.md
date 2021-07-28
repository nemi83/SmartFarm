# SmartFarm

This project provides sensor data on air and soil that is displayed on an android device. It measures four parameters: air temperarure, air humidity, soil humidity and soil ph. The opening screen provides the last measurments, whereas the navigation menu gives access to a graphical display of mentioned measurments for a period of 24 hours, 1 week or 1 month. 

The second building block of the application gives the user access to the watering system. It gives 2 options, either watering for 1 hour interval or the option of manually starting and stopping the watering system. After data collection and analysis, the system will automatically start and stop the watering system which will be based on the measured parameters.

To digitalize this project one needs:
- Raspberry Pi,
- Arduino Uno,
- air sensor,
- soil humidity sensor,
- soil ph sensor,
- relay

To Do:
1. Implementing ssh connection into main.py to invoke relay scripts,
2. Wiering and measuring Soil Ph and implement into arduino_get_data.ino.
