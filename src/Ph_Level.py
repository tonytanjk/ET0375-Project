import time
from hal import hal_lcd as LCD
import hal.hal_keypad as keypad
from hal import hal_input_switch as input_switch
from threading import Thread
import queue
lcd = LCD.lcd()
lcd.lcd_clear()
global result
result = None

# Queue to store keypad presses
shared_keypad_queue = queue.Queue()

def key_pressed(key):
    shared_keypad_queue.put(key)

def init():
    input_switch.init()
    keypad.init(key_pressed)
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()

def get_keypad_value():
    if not shared_keypad_queue.empty():
        return shared_keypad_queue.get()
    return None

def process_key():
    global result
    sw_switch = input_switch.read_slide_switch()
    if sw_switch == 1:
        print("Call Detected")
        time.sleep(5)
        while(True):
            print("Press key NOW")
            time.sleep(3)
            keyvalue = shared_keypad_queue.get()
            print("key value ", keyvalue)
            time.sleep(2)
            key = int(keyvalue)
            if 1<= key <= 9:
                result = key
            return result
    elif result == None:
        return 0
    else:
        return result


def main():
    init()
    pH = process_key()
    return pH


if __name__ == "__main__":
    init()
