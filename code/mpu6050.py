import machine
import time

class MPU6050:
    def __init__(self, i2c, address=0x68):
        self.i2c = i2c
        self.address = address
        # Try to wake it up with a small delay
        time.sleep(0.1) 
        self.i2c.writeto_mem(self.address, 0x6B, b'\x00') 
        time.sleep(0.1)

    def read_raw_data(self, addr):
        # Using readfrom_mem directly (Pico-friendly)
        data = self.i2c.readfrom_mem(self.address, addr, 2)
        value = (data[0] << 8) | data[1]
        if value > 32768:
            value -= 65536
        return value

    def get_values(self):
        vals = {}
        vals["AcX"] = self.read_raw_data(0x3B)
        vals["AcY"] = self.read_raw_data(0x3D)
        vals["AcZ"] = self.read_raw_data(0x3F)
        vals["Tmp"] = self.read_raw_data(0x41) / 340.0 + 36.53
        vals["GyX"] = self.read_raw_data(0x43)
        vals["GyY"] = self.read_raw_data(0x45)
        vals["GyZ"] = self.read_raw_data(0x47)
        return vals

