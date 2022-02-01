import machine
import math

class InternalThermistor:

        def __init__(self, channel):
            self.__channel = channel
            self.__temperature_in_C = 0
            self.__thermistor = machine.ADC(self.__channel)

        def get_temperature(self):          
            temperature_adc_value = self.__thermistor.read_u16()
            #print(temperature_adc_value)
            temperature_adc_voltage = 3.3 * float(temperature_adc_value) / 65535
            #print(temperature_adc_voltage)
            self.__temperature_in_C = 27 - (temperature_adc_voltage - 0.706)/0.001721
            #print(self.__temperature_in_C)
            return self.__temperature_in_C

        