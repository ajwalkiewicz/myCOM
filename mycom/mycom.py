#!/usr/bin/env python3
import serial
from serial.tools import list_ports

class MyCOM():
    """[summary]
    """
    def __init__(self, port: str, baudrate: int):
        # super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.timeout = 1
        self.port_list = self.available_ports()

    def start_connection(self):
        self.ser = serial.Serial(
            port=self.port,
            baudrate=self.baudrate,
            timeout=self.timeout
        )
        return True

    def stop_connection(self):
        self.ser.close()
        return True

    def receive_data_from_serial(self):
        while True:
            if str(self.ser.readline())[2:-5] not in ("b''", ""):
                print(str(self.ser.readline())[2:-5])

    def send_data_to_serial(self, data: str):
        """
        Send data to serial
        """
        data = data + "\r\n"
        print(data)
        self.ser.write(bytes(data, "utf-8"))

    @staticmethod
    def available_ports():
        return [f"/dev/{port.name}" for port in list_ports.comports()]

    def change_port(self, port: str):
        self.stop_connection()
        self.port = port
        self.start_connection()
        return True

    def change_baudrate(self, baudrate: int):
        self.stop_connection()
        self.baudrate = baudrate
        self.start_connection()
        return True

if __name__ == "__main__":
    MyCOM("loop://", 9600)
    # MyCOM("/dev/ttyUSB1", 9600)
    print("done")