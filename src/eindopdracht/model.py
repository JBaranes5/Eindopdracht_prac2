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

    def constantMeasurementStart(self):
        self._constant_thread = threading.Thread(
            target = self.constantMeasurement
        )

        self.terminate = False
        self._constant_thread.start()

    def constantMeasurement(self):
        self.measuring_busy = True
        self.U1 = digitalToAnalog(self.device.get_input_value(1))
        self.U2 = digitalToAnalog(self.device.get_input_value(2))
        self.U, self.I = calcUI(self.U1, self.U2)

    def runStart(self, amount, stepsize, start, stop):
        self._run_thread = threading.Thread(
            target = self.run, args=(amount, stepsize, start, stop)
        )
        self.terminate = False
        self._run_thread.start()

    def run(self, amount, stepsize, start, stop):
    
        self.U_list = []
        self.I_list = []
        self.P_list = []
        self.R_list = []

        self.U_error_list = []
        self.I_error_list = []
        self.P_error_list = []

        counter_U0 = start
        while counter_U0 <= stop and self.terminate == False:
            self.device.set_output_value(0, counter_U0)

            counter_runs = 0
            U_list_temp = []
            I_list_temp = []
            R_list_temp = []
            P_list_temp = []
            while counter_runs < amount:

                try: 
                    self.U1 = digitalToAnalog(self.device.get_input_value(1))
                    self.U2 = digitalToAnalog(self.device.get_input_value(2))
                    self.U, self.I = calcUI(self.U1, self.U2)
                    self.R = calcRVar(self.U, self.I)
                    self.P = self.U * self.I
                except:
                    pass

                U_list_temp.append(self.U)
                I_list_temp.append(self.I)
                P_list_temp.append(self.P)
                R_list_temp.append(self.R)

                counter_runs += 1

            self.U_list.append(np.average(U_list_temp))
            self.I_list.append(np.average(I_list_temp))
            self.P_list.append(np.average(P_list_temp))
            self.R_list.append(np.average(R_list_temp))

            self.U_error_list.append(np.std(U_list_temp))
            self.I_error_list.append(np.std(I_list_temp))
            self.P_error_list.append(np.std(P_list_temp))

            counter_U0 += stepsize

        self.device.set_output_value(0, 0)
        self.close_device()

        
    def close_device(self):
        self.device.closedevice()




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

# calculate the U total and I total
def calcUI(U1, U2):
    """calculate the total U and I that the solar cell produces

    Args:
        U1 (float): the voltage that is measured by channel 1 from the arduino
        U2 (float): the voltage that is measured by channel 2 from the arduino

    Returns:
        floats: the total U and I that the solar cell produces
    """    
    I = U2 / 4.7
    U = U1 * 3
    return U, I

# calculate the resistance of the MOSFET
def calcRVar(U, I):
    """calculate the resistance of the variable resistance

    Args:
        U (float): the total voltage that the solar cell produces
        I (float): the total amperage that the solar cell produces

    Returns:
        float: the resistance of the variable resistance
    """    
    R = U/ I
    RVartemp = (1 / R) - (1 / 3e9)
    RVar = (1 / RVartemp) - 4.7
    return RVar





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
