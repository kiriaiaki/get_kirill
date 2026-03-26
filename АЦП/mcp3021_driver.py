
import smbus
import time

class MCP3021:
    def __init__(self, dynamic_range, verbose = True):
        self.bus = smbus.SMBus(1)
        
        self.address = 0x4D
        self.wm = 0x00
        self.pds = 0x00
        
        self.verbose = verbose
        self.dynamic_range = dynamic_range

    def deinit(self):
        self.bus.close()

    def get_number(self):
        data = self.bus.read_word_data(self.address, 0)
        lower_data_byte = data >> 8
        upper_data_byte = data & 0xFF
        number = (upper_data_byte << 6) | (lower_data_byte >> 2)
        if self.verbose:
            print(f"Принятые данные: {data}, Upper_byte: {upper_data_byte:x}, Lower_byte: {lower_data_byte:x}, Num: {number}")

        return number

    def get_voltage(self):
        digital_value = self.get_number()
        voltage = digital_value * self.dynamic_range / 256
        return voltage

if __name__ == "__main__":
    try:
        mcp = MCP3021(dynamic_range = 3.0)
        
        while True:
            voltage = mcp.get_voltage()
            print(f"Voltage: {voltage:.3f}V")
            time.sleep(1.0)

    finally:
        mcp.deinit()