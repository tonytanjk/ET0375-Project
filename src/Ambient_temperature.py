from hal import hal_temp_humidity_sensor as Temp
from hal import hal_lcd as LCD
from hal import hal_dc_motor as DC
lcd = LCD.lcd()
var1 = False
def init(): #Initialize Temp sensor and fan
   global var1
   if var1 == False: #Prevent from re-running init if Relative_Humidity.py file has run it //  Basically idiot proofing something an idiot will overlook
      Temp.init()
      var1 = True
      DC.init()

#Read Temperature Values   
def Ambi_Temp():
   result = Temp.read_temp_humidity()
   if result != 100:
      #lcd.lcd_display_string("Temperature "  +str(result) + "*C", 2)
      temperature = result[0]
      print(result[0])
   else:
      print("Failed to read temperature.")
   return temperature

def Temp_solution(temperature):
   if temperature > 25:
      DC.set_motor_speed(100)
      return 1
   else:
      DC.set_motor_speed(0)
      return 0

#REQ04 
def main(): 
   temperature = Ambi_Temp()
   if temperature is not None:
      lcd.lcd_clear()
      #lcd.lcd_display_string("Temperature "  +str(temperature) + "*C", 2)

      
      Temp_solution(temperature)

   else:
      lcd.lcd_clear()
      lcd.lcd_display_string("Temperature: Error" )
   return temperature

if __name__ == "_main_":
    main()