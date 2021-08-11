#!/usr/bin/python3

import unittest
import mycom.mycom as mc
from os import path
from unittest.mock import patch

PORT = "/dev/ttyUSB0"


class TestCharacterClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.port = PORT
        cls.baudrate = 9600

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.mycom = mc.MyCOM(self.port, self.baudrate)
        self.mycom.start_connection()

    def tearDown(self):
        self.mycom.stop_connection()

    def test_start_connection(self):
        result = self.mycom.start_connection() 
        self.assertTrue(result)

    def test_stop_connection(self):
        result = self.mycom.stop_connection() 
        self.assertTrue(result)

    def test_receive_data_from_serial(self):
        # data = "test"
        # result = self.mycom.send_data_to_serial(data=data)
        pass

    def test_send_data_to_serial(self):
        pass
    
    @patch('mycom.mycom.serial.tools.list_ports')
    def test_available_ports(self, mocked_list_ports):
        mocked_list_ports.side_effect = ["/dev/ttyUSB0", "/dev/ttyUSB1"]
        compare = ["/dev/ttyUSB1", "/dev/ttyUSB0"]
        result = self.mycom.available_ports()
        self.assertListEqual(result, compare)

    def test_change_port(self):
        port = "/dev/ttyUSB1"
        result = self.mycom.change_port(port=port)
        self.assertTrue(result)

    def test_change_baudrate(self):
        baudrate = 115200
        result = self.mycom.change_baudrate(baudrate=baudrate)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()