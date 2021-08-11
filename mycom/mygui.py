#!/usr/bin/env python3
from mycom import MyCOM
import threading
import sys
import PySimpleGUI as sg

def main():

    init_data = {
        "port": MyCOM.available_ports()[0],
        "baudrate": 9600,
    }

    baudrates = [1200, 2400, 4800, 19200, 38400, 57600, 115200]

    available_ports  = MyCOM.available_ports()

    mycom = MyCOM(**init_data)
    mycom.start_connection()
    threading.Thread(target=mycom.receive_data_from_serial, daemon=True).start()
    # threading.Thread(target=mycom, args=(init_data["port"], init_data["baudrate"]), daemon=True).start()
    
    row_1 = [
        sg.Input(key='-IN-',size=(90,5)),
        sg.Button('Send', focus=True, bind_return_key=True)]
    row_2 = [
        sg.Multiline(
            size=(100,50),
            key='-ML-',
            autoscroll=True,
            reroute_stdout=True,
            write_only=True,
            reroute_cprint=True)]
    row_3 = [
        sg.Text(text="Ports: "),
        sg.Combo(
            available_ports,
            default_value=init_data["port"],
            key="-PORT-",
            enable_events=True),
        sg.Text(text="baudrate: "),
        sg.Combo(
            baudrates,
            default_value=9600,
            key="-BR-",
            enable_events=True),
            # sg.Text(text=" "*80),
            # sg.Button('Exit')
            ]

    layout = [row_1, row_2, row_3]
    window = sg.Window('MyCOM', layout, finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED: # or event == 'Exit':
            break

        if event == "Send" and values.get("-IN-"):
            mycom.send_data_to_serial(data=values.get("-IN-"))

        if event == "-PORT-":
            mycom.change_port(port=values['-PORT-'])

        if event == "-BR-":
            mycom.change_baudrate(baudrate=values['-BR-'])

    window.close()
    sys.exit()

if __name__ == "__main__":
    main()