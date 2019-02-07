import PySimpleGUI as sg
import image_handling


def main():
    layout = [[sg.Text('Change Look | Currently:'), sg.Text('', key='_OUTPUT_')],
              [sg.Input(do_not_clear=True, key='_IN_')],
              [sg.Button('Change'), sg.Exit()]]

    window = sg.Window('Window Title').Layout(layout)

    while True:
        event, values = window.Read()
        print(event, values)
        if event is None or event == 'Exit':
            break
        if event == 'Change':
            sg.ChangeLookAndFeel(values['_IN_'])
            window.FindElement('_OUTPUT_').Update(values['_IN_'])

    window.Close()


def get_image_gui():
    layout = [
        [sg.Text("Select image file:")],
        [sg.InputText(), sg.FileBrowse()],
        [sg.Submit(), sg.Exit()]
    ]

    return sg.Window("Open Image").Layout(layout).Read()


def test_image_display():
    event, (source_filename,) = get_image_gui()

    img_data = image_handling.processing(source_filename)
    layout = [
        [sg.Image(data=img_data, key="_IMG_")],
        [sg.Exit()]
    ]
    window = sg.Window("My Image Window").Layout(layout)

    while True:
        event, other = window.Read()
        if event is None or event == 'Exit':
            break
    window.Close()


if __name__ == '__main__':
    test_image_display()
