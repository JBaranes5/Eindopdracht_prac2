try:

 from nsp2visasim import sim_pyvisa as pyvisa

except ModuleNotFoundError:

 import pyvisa

# class for using the arduino
class ArduinoVISADevice():
    # initialize the device
    def __init__(self, port):
        """Initialize the Arduino

        Args:
            port (string): The port that the Arduino is attached to
        """        
        rm = pyvisa.ResourceManager("@py")
        self.device = rm.open_resource(
            port, read_termination="\r\n", write_termination="\n"
        )
    
    def get_identification(self):
        """Get the identification of the Arduino

        Returns:
            string: The identification of the Ardiuno
        """        
        return self.device.query("*IDN?")

    def set_output_value(self, channel, value):
        """Set the output of a certain channel of the Arduino

        Args:
            value (int): The output value that will be set from 0 until 1023
            channel (int): The channel where the voltage will be outputted
        """        
        self.device.query(f"OUT:CH{channel} {value}")

    def get_output_value(self, channel):
        """Get the output of a certain channel of the Arduino

        Args:
            channel (int): The outputting channel where the output value will be taken from

        Returns:
            int: The output value that has been set
        """        
        return int(self.device.query(f"OUT:CH{channel}?"))
    
    def get_input_value(self, channel):
        """Get the intput value of a certain channel

        Args:
            channel (int): Set the channel that will be measured

        Returns:
            int: The input value that has been measured
        """        
        return int(self.device.query(f"MEAS:CH{channel}?"))
    
    def get_input_voltage(self, channel):
        """Get the input voltage of a certain channel

        Args:
            channel (int): Set the channel that will be measured

        Returns:
            float: The input voltage that has been measured
        """        
        return (self.get_input_value(channel) / 1024) * 3.3

    def closedevice(self):
        self.device.close()

# list the available devices to pyvisa
def list_devices():
    rm = pyvisa.ResourceManager()
    ports = rm.list_resources()
    return ports
