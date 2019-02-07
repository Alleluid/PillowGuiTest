import PySimpleGUI as sg


def main():
    layout = [[sg.Text('my one-shot window')],
              [sg.InputText()],
              [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Window Title').Layout(layout)

    event, values = window.Read()
    window.Close()

    print(values[0])


if __name__ == '__main__':
    main()
