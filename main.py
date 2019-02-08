import PySimpleGUI as sg
import image_handling


def main():
    event, (source_filename,) = get_image_gui()

    img_data = image_handling.processing(source_filename)
    layout = [
        [sg.Image(data=img_data, key="_IMG_")],
        [sg.Button("Open"), sg.Exit()]
    ]
    window = sg.Window("My Image Window").Layout(layout)

    while True:
        event, other = window.Read()
        if event is None or event == 'Exit':
            break
        elif event == 'Open':
            event, (source_filename,) = get_image_gui()
            img_data = image_handling.processing(source_filename)
            window.FindElement("_IMG_").Update(data=img_data)
    window.Close()


def get_image_gui():
    layout = [
        [sg.Text("Select image file:")],
        [sg.InputText(), sg.FileBrowse()],
        [sg.Submit(), sg.Exit()]
    ]

    window = sg.Window("Open Image")
    read = window.Layout(layout).Read()
    window.Close()
    return read



if __name__ == '__main__':
    main()
