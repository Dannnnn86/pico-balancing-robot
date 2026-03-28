import mpudata
import time

print("Robot Brain Starting... Reading X-Axis data.")

while True:
    # Get all the data from your provider file
    data = mpudata.get_all_data()
    
    if data:
        # Pull out only the X values
        accel_x = data['ax']
        gyro_x = data['gx']
        
        print("X-Tilt: {:.2f} G | X-Rotation: {:.2f} dps".format(accel_x, gyro_x))
    else:
        print("Sensor error! Check connections.")
        
    # Fast loop for balancing (10ms)
    time.sleep(0.01)
