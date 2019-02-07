import PySimpleGUI as sg


def main():
    layout = [[sg.Text('Persistent Window')],
              [sg.Input(do_not_clear=True)],
              [sg.Button('Read'), sg.Exit()]]

    window = sg.Window('Window Title').Layout(layout)

    while True:
        event, values = window.Read()
        if event is None or event == 'Exit':
            break
        print(values[0])

    window.Close()


if __name__ == '__main__':
    main()
