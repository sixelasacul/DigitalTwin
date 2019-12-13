from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from config import config

modbus = config['modbus']


class ModbusParams:
    def __init__(self):
        self.context = None

    def init_modbus_context(self):
        block_address = [modbus['registers_starting_address']] * modbus['registers_number']
        store = ModbusSlaveContext(hr=ModbusSequentialDataBlock(0, block_address))
        self.context = ModbusServerContext(slaves=store, single=True)
        return self.context

    def set_context_values(self, values):
        try:
            self.context[modbus['slave_id']].setValues(
                modbus['function_code'],
                modbus['registers_starting_address'],
                values)
        except Exception as e:
            print("Error : ", e)
