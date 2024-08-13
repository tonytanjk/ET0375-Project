import time
from hal import hal_adc as adc
from hal import hal_servo as servo
def init():
    adc.init()
    servo.init()

def read_adc():
    value = adc.get_adc_value(1)
    EC_value = float(value / 1024) * 5
    print(EC_value)
    return EC_value

def open_solution(EC_value):
    servo.init()
    if 1.0 < EC_value < 2.5:
        servo.set_servo_position(120)
        time.sleep(2)
        return 1
    else:
        EC_value < 1.0 or EC_value > 2.5    
        servo.set_servo_position(20)
        time.sleep(2)
        return 0

def main():
    while True:
        EC = read_adc()
        open_solution(EC)
        time.sleep(2)
        return EC

if __name__ == '__main__':
    main()
