import serial
from serial.tools import list_ports
import threading 
import time
import sys
import PySimpleGUI as sg

cp = sg.cprint

port = '/dev/ttyUSB1'
baudrate = 115200
timeout = 1
ser = serial.Serial(port, baudrate=baudrate, timeout=timeout)


def receive():
    while True:
        # cp(str(ser.readline()))
        if str(ser.readline())[2:-5] not in ("b''", ""):
            cp(str(ser.readline())[2:-5])

def send(arg):
    cp(arg)
    arg = arg + "\r\n"
    ser.write(bytes(arg, "utf-8"))

def ports():
    return [port.name for port in list_ports.comports()]

def main():
    global port
    global baudrate
    global ser

    layout = [  
                [sg.Input(key='-IN-', size=(90,5)), sg.Button('Send', focus=True, bind_return_key=True)],
                [sg.Multiline(size=(100,50), key='-ML-', autoscroll=True, reroute_stdout=True, write_only=True, reroute_cprint=True)],
                [sg.Text(text="Ports: "), sg.Combo(ports(), key="-PORT-", enable_events=True), sg.Text(text="baudrate: "), sg.Combo([115200, 9600], key="-BAUD-", enable_events=True), sg.Button('Exit')]
    ]

    window = sg.Window('Mycom', layout, finalize=True)

    threading.Thread(target=receive, daemon=True).start()
    time.sleep(2)
    send("\r\n")

    while True:
        event, values = window.read()
        # print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == "Send" and values.get("-IN-"):
            send(values["-IN-"])

        if event == "-PORT-":
            ser.close()
            ser = serial.Serial(f"/dev/{values['-PORT-']}", baudrate=baudrate, timeout=timeout)

        if event == "-BAUD-":
            ser.close()
            ser = serial.Serial(port=port, baudrate=values['-BAUD-'], timeout=timeout)


    window.close()
    sys.exit()


if __name__ == "__main__":
    main()
    
