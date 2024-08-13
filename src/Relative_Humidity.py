from hal import hal_lcd as LCD
from hal import hal_temp_humidity_sensor as Temp
import time  # Ensure time is imported for the sleep function
from Ambient_temperature import var1
lcd = LCD.lcd()
lcd.lcd_clear()

#Initialize Sensor
def init():
    global var1
    if var1 == False: #Cross checks if init has run before since DHT11 sensor is combination of both temp and humid
        Temp.init()
        var1 = True
    else:
        return None

def Ambi_Humi():
    result = Temp.read_temp_humidity()
    # Check for valid humidity value
    if result[1] != -100:
        print(result[1])
        return result[1]
    else:
        print("Failed to read humidity.")
        return None

def main():
    init()  # Initialize the sensor
    while True:
        humidity = Ambi_Humi()
        if humidity is not None:
            return humidity
        else:
            lcd.lcd_clear()
            print("Humidity Error")
           #lcd.lcd_display_string("Humidity: Error", 1)
        return humidity

if __name__ == "__main__":
    main()
