#test_main.py
from unittest.mock import patch
import Light_intensity as LI
import EC_level as EC
import pH_level as PH
import Relative_Humidity as RH
import Ambient_temperature as AT
import Server as Sys
import pytest

Sys.init() #Initialize Sensors before testing

#Temperature Pytest
def test_temp(): #Hardware Test
    result = AT.Ambi_Temp()
    if result == -100:
        assert None
    else:
        assert True

def test_temp_solution(): #Software Test
    test=31
    exp_result = 1
    result = AT.Temp_solution(test)

    assert exp_result == result

#Humidity Pytest 
def test_humi(): #Hardware Test
    result = RH.Ambi_Humi()
    if result == -100:
        assert None
    else:
        assert True

#Light Intensity Pytest
def test_amb_LI():
    # with patch(LI.read_light_intensity, return_value=600) as mock_get_adc_value: #mocking without hardware test
    #     light_intensity = LI.read_light_intensity()
    #     mock_get_adc_value.assert_called_once_with(0)
    light_intensity = LI.read_light_intensity()
    if light_intensity != 0:
        assert True
    else:
        assert False

def test_LI_solution():
    LI.hal_led.init()
    exp_result = 1
    result = LI.light_solution(200)

    assert result == exp_result

#EC Level Pytest
def test_read_adc():
    test_input = 512
    expected_output = 2.5

    result = EC.read_adc()
    if result is not None:
        assert True
    else:
        assert False
    

def test_open_solution_1():
    test_input = 1.5
    expected_output = 1

    result = EC.open_solution(test_input)

    assert result == expected_output

def test_open_solution_0():
    test_input = 3
    expected_output = 0

    result = EC.open_solution(test_input)

    assert result == expected_output

#pH level Pytest
@pytest.fixture  #reset input number before each test
def reset_input_number():
    global input_number
    input_number = ""

def test_process_key_digit(reset_input_number):  #verify digits
    PH.process_key('1')
    PH.process_key('2')
    assert input_number == '12'

def test_process_key_confirmation(reset_input_number, capsys):  #check cfm key
    PH.process_key('1')
    PH.process_key('3')
    PH.process_key('#')
    captured = capsys.readouterr()
    assert "pH Level entered: 13" in captured.out
    assert input_number == ""

def test_process_key_invalid_ph_level(reset_input_number, capsys):  #display invalid msg
    PH.process_key('0')
    PH.process_key('#')
    captured = capsys.readouterr()
    assert "Invalid pH Level. Please enter a value between 1 and 14." in captured.out
    assert input_number == ""

def test_process_key_non_digit(reset_input_number): #irrelevent keys
    PH.process_key('A')
    assert input_number == ""