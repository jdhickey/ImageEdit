
import numpy as np
import PIL
import uuid


def read_image(path):
    try:
        image = PIL.Image.open(path)
        return image
    except Exception as e:
        print(e)


def rand_img(x, y, show=False, save=False):
    filename = str(uuid.uuid4())
    arr = np.random.randint(0, 255, (x, y, 3)).astype(np.uint8)
    img = PIL.Image.fromarray(arr)

    if show:
        img.show()
    elif save:
        img.save("./out/" + filename + ".jpg")
    else:
        return img

