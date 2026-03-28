#cleaner data from the IMU
from machine import Pin, I2C
import mpu6050 
import time

# Hardware Setup - 400kHz
i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)
time.sleep(0.1) 
sensor = mpu6050.MPU6050(i2c)

def get_all_data():
    """Returns a dictionary with all cleaned sensor values"""
    try:
        raw = sensor.get_values()
        return {
            "ax": raw["AcX"] / 16384,
            "ay": raw["AcY"] / 16384,
            "az": raw["AcZ"] / 16384,
            "gx": raw["GyX"] / 131,
            "gy": raw["GyY"] / 131,
            "gz": raw["GyZ"] / 131,
            "temp": raw["Tmp"]
        }
    except OSError:
        return None

if __name__ == "__main__":
    print("Full 6-Axis Live Preview...")
    while True:
        data = get_all_data()
        if data:
            print("ACCEL: X:{:.2f} Y:{:.2f} Z:{:.2f} | GYRO: X:{:.2f} Y:{:.2f} Z:{:.2f}".format(
                data['ax'], data['ay'], data['az'], data['gx'], data['gy'], data['gz']))
        time.sleep(0.1)
