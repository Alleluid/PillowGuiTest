import io

from PIL import Image, ImageDraw


def processing(filename: str):
    _MIN_SIZE = 512

    img: Image.Image = Image.open(filename)
    bio = io.BytesIO()
    img_modded = img.copy()

    ix, iy = img_modded.size
    if min(ix, iy) < _MIN_SIZE:
        multi = 2
        new_x, new_y = ix, iy
        while min(new_x, new_y) < _MIN_SIZE:
            new_x = ix * multi
            new_y = iy * multi
            multi += 1
        print(f"multi was {multi}")
        print(f"image size is now {new_x}, {new_y}")
        img_modded = img_modded.resize((new_x, new_y), Image.NEAREST)

    draw = ImageDraw.Draw(img_modded)
    ix, iy = img_modded.size
    draw.ellipse(
        (ix // 2, iy // 2),
        width=1
    )

    img_modded.save(bio, format="PNG")
    return bio.getvalue()

def img_obj_to_bytes(image: Image) -> bytes:
    bio = io.BytesIO()
    image.save(bio, format="PNG")
    return bio.getvalue()


if __name__ == '__main__':
    filename = r"D:\Users\milot\Pictures\alleluid_leaf_badass.png"
    print(type(processing(filename)))
