import serial
import sys

def main():
    port = '/dev/ttyUSB1'
    baudrate = 115200
    timeout = 1

    ser = serial.Serial(port, baudrate=baudrate, timeout=timeout)

    while True:
        try:
            line = str(ser.readline())
            if line != "b''":
                print(line[2:-5])
        except KeyboardInterrupt:
            break
    
    ser.close()
    return True

if __name__ == "__main__":
    main()
    sys.exit()
