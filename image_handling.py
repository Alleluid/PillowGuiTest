from PIL import Image
from PIL.ImageTk import BitmapImage


def processing(filename: str):
    img: Image.Image = Image.open(filename)
    return BitmapImage(img)


if __name__ == '__main__':
    filename = r"D:\Users\milot\Pictures\alleluid_leaf_badass.png"
    print(processing(filename))
