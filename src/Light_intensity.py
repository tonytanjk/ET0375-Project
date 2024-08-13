import time
import hal.hal_adc as hal_adc
import hal.hal_led as hal_led

def init():
    hal_adc.init()
    hal_led.init()

def read_light_intensity():
    light_intensity = hal_adc.get_adc_value(0) # Read light intensity from ADC channel 0 (connected to LDR)
    return light_intensity

def light_solution(light_intensity):
    if light_intensity < 500:  # Adjust the threshold
        hal_led.set_output(1, 1)
        return 1
    else:
        hal_led.set_output(1, 0) 
        return 0

def main():
    hal_led.init()
    while True:
        light_intensity = read_light_intensity()

        print(f"Light Intensity: {light_intensity}")  # Display light intensity on console
        # Control LED based on light intensity

        light_solution(light_intensity)
        
        # Wait before the next reading

        return light_intensity

if __name__ == "__main__":
    main()
