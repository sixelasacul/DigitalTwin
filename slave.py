from pymodbus.server.asynchronous import StartTcpServer
from twisted.internet.task import LoopingCall

from dao import DAO
from modbus_params import ModbusParams
from config import config

modbus = config['modbus']


class Slave:
    def __init__(self):
        self.dao = DAO()
        self.modbus_params = ModbusParams()

    def start(self):
        print("Starting modbus_slave at %s:%s" % (modbus['host'], modbus['port']))
        to_loop = self.send_data_to_modbus
        context = self.modbus_params.init_modbus_context()

        loop = LoopingCall(to_loop)
        loop.start(modbus['interval'])
        StartTcpServer(context, address=(modbus['host'], modbus['port']))

    def send_data_to_modbus(self):
        try:
            values = self.dao.retrieve_temperatures()
            if len(values) < 0:
                raise Exception("No values found, allô")
            self.modbus_params.set_context_values(values)
        except Exception as e:
            print("Error : ", e)

