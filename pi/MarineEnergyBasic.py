#!/usr/bin/env python
#This is the control unit that runs the Raspberry PI DAQ

#from Encoder import Encoder, get_rpm
from Encoder import Encoder, get_rpm
from Sensor import run_Sensor
from gpiozero import LED
import pandas as pd
import threading
import time
import sys

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
    if water > 1:
        waterON()
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

    
    df = pd.concat([df, pd.DataFrame({'Voltage (V)': [voltage], 'Current (A)':[current], "Gen RPM": [gen_rpm], "Time (Seconds)": [current_time], "Output Power (W)": [output_power], "Resistance (Ohms)":[resistance], "Generator Temp (C)": [temp1], "Gearbox Temp (C)": [temp2], "Water Sensor Voltage": [water]})], ignore_index=True)
    i=1
    while i < len(df):
        sys.stdout.write('\033[F')  # Move cursor up one line
        sys.stdout.write('\033[K') 
        i+=1 # Clear the line
    print(df, end ="\r")
    write_dataframe_to_csv(df, 'data.csv')


def write_dataframe_to_csv(dataframe, filepath):
    dataframe.to_csv(filepath, index=False, header=True)

def waterON():
    waterLED.on()
    

try:
    
    thread1 = threading.Thread(target=Encoder) #Initializes Encoder 
    thread1.start()

    while True:
        add_data()    
        time.sleep(data_collection_interval)
   
    
except KeyboardInterrupt:
    exit()