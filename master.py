import time
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from mqtt import MQTT
from modbus_params import ModbusParams
from config import config

modbus = config['modbus']
publish = config['mqtt']['publish']


class Master:
    def __init__(self):
        self.client = ModbusClient(modbus['host'], modbus['port'])
        self.modbus_params = ModbusParams()
        self.mqtt_client = MQTT()

    def read_temperatures_registers(self):
        temperatures = self.client.read_holding_registers(
            modbus['registers_starting_address'],
            modbus['registers_number']
        )
        self.send_temperatures(temperatures.registers)
        return temperatures

    def send_temperatures(self, temperatures_registers):
        temperature_per_room = self.format_temperatures(temperatures_registers)
        self.pretty_print_temperatures(temperature_per_room)
        if publish:
            self.mqtt_client.publish_to_topic(temperature_per_room)

    def format_temperatures(self, temperatures):
        temperatures_dictionary = dict()
        for i in range(0, len(temperatures)):
            temp_i = i + 1
            key = "room_%d" % temp_i
            temperatures_dictionary[key] = temperatures[i] - 273
        return temperatures_dictionary

    def pretty_print_temperatures(self, temperatures):
        for room in temperatures:
            print("For %s, temperature is %s" % (room, temperatures[room]))

    def start_reading_loop(self):
        print("Starting reading loop")
        while True:
            self.read_temperatures_registers()
            time.sleep(modbus['interval'])
