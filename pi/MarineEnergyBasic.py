#!/usr/bin/env python
#This is the control unit that runs the Raspberry PI DAQ

#from Encoder import Encoder, get_rpm
from Encoder import Encoder, get_rpm
from Sensor import run_Sensor
from gpiozero import LED
import pandas as pd
import threading
import time

# Constants
waterLED = LED(27) #What GPIO pin that the waterlight LED is on the raspberry pi
data_collection_interval = 2 # How many seconds to collect data
gearbox_ratio = 5 
start_time = time.time()
filename = "Output.csv" # Output file name
df = pd.DataFrame()

# Create a function to collect new data
def add_data():
    global df
    torque, temp1, temp2, voltage, current, water = run_Sensor()
    if water > 0.1:
        water()
    input_rpm = get_rpm()
    gen_rpm = input_rpm *gearbox_ratio
    # add rpm to concat call below here
    # add time as current_time - start time
    current_time = (time.time() - start_time)
    output_power = current * voltage
    if current <= 0: 
        resistance = 0
    else:
        resistance = voltage/current

    df = pd.concat([df, pd.DataFrame({'Voltage': [voltage], 'Current':[current], "Gen RPM": [gen_rpm], "Time (Seconds)": [current_time], "Output Power": [output_power], "Resistance":[resistance], "Generator Temp": [temp1], "Gearbox Temp": [temp2]})], ignore_index=True)
    print(df)
    write_dataframe_to_csv(df, 'data.csv')


def write_dataframe_to_csv(dataframe, filepath):
    dataframe.to_csv(filepath, index=False, header=True)

def water():
    waterLED.on()
    

try:
    
    thread1 = threading.Thread(target=Encoder) #Initializes Encoder 
    thread1.start()

    while True:
        add_data()    
        time.sleep(data_collection_interval)
   
    
except KeyboardInterrupt:
    exit()