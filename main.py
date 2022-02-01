import time
from internal_thermistor import InternalThermistor
from data_logger import DataLogger

internal_thermistor = InternalThermistor(4)
data_logger = DataLogger("logger.csv")

while True:
    print(internal_thermistor.get_temperature())
    data_logger.write_to_logger(internal_thermistor.get_temperature())
    time.sleep_ms(1000)

