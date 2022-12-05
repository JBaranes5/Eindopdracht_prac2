from eindopdracht.controller import ArduinoVISADevice, list_devices
import numpy as np
import os
import threading

# save the data provided to a csv file
def saveData(data, filename):
    """Save a Dataframe to a csv file

    Args:
        data (dataframe):  The dataframe with the data
        filename(str): the filename that will be given to the file
    """        

    # check what number file exists and create the next one
    condition = 0
    counter = 1
    while condition == 0:
        if os.path.isfile(f"Data\{filename}_{counter}.csv") == True:
            counter += 1
        else:
            condition = 1
    data.to_csv(f"Data\{filename}_{counter}.csv")

class ZonnecelExperiment():
    # set up the ardiuno
    def __init__(self, port):
        """Initialize the Arduino controller

        Args:
            resistor (int): The resistance of the resistor used
            port (string): The name of the port that the Arduino is plugged in
        """        
        self.device = ArduinoVISADevice(port=port)




# calculations

# calculate the digital signal from the analog signal
def analogToDigital(analog):
    """Convert the analog voltage to a digital signal

    Args:
        analog (float): The analog voltage that needs to be converted

    Returns:
        int: The converted digital signal
    """        
    # if analog is an integer or float
    if type(analog) == int or type(analog) == float:
        # the system does not measure above 3.30V
        if analog > 3.3:
            analog = 3.3
        digital = round((analog / 3.3) * 1024, 0)
        return int(digital)

    # if analog is an array
    else:
        digital = (analog / 3.3) * 1024
        return digital

# calculate the analog signal from the digital signal
def digitalToAnalog(digital):
    """Convert the digital signal to an analog voltage

    Args:
        digital (int): The digital signal that needs to be converted

    Returns:
        float: The converted analog voltage
    """    

    analog = (digital / 1024) * 3.3
    return analog




# communications with the device

# list the devices connected via USB
def list_devices_model():
    """list the devices connected via USB

    Returns:
        list: the list of all the connected devices
    """    
    return list_devices()

# identify a certain port
def identify_device(port):
    """identify a device on a certain port

    Args:
        port (str): the port of the device

    Returns:
        str: the identification of the port
    """    
   
    device = ArduinoVISADevice(port=port)
    return device.get_identification()