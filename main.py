import PySimpleGUI as sg
import image_handling


def main():
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


def get_image_gui():
    layout = [
        [sg.Text("Select image file:")],
        [sg.InputText(), sg.FileBrowse()],
        [sg.Submit(), sg.Exit()]
    ]

    return sg.Window("Open Image").Layout(layout).Read()


if __name__ == '__main__':
    main()
