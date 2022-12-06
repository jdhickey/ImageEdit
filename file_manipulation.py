
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
        img.save("./out/random_" + filename + ".jpg")
    else:
        return img


def circle(x, y, centre, radius, show=False, save=False):
    filename = str(uuid.uuid4())
    arr = np.zeros((x, y, 3))

    for i in range(x):
        for j in range(y):
            if ((i - centre[0])**2 + (j - centre[1])**2 - radius**2) in range(radius*2):
                arr[i][j] = [255, 255, 255]

    img = PIL.Image.fromarray(arr.astype(np.uint8))

    if show:
        img.show()
    elif save:
        img.save("./out/circle_" + filename + ".jpg")
    else:
        return img


def sin_2D(x, show=False, save=False):
    filename = str(uuid.uuid4())
    arr = np.zeros((x, x, 3))

    for i in range(x):
        for j in range(x):
            arr[i][j] = (
            256 * np.sin(i * j * 2 * np.pi / x),
            256 * np.sin(i * j * 2 * np.pi / x),
            256 * np.sin(i * j * 2 * np.pi / x))

    img = PIL.Image.fromarray(arr.astype(np.uint8))

    if show:
        img.show()
    elif save:
        img.save("./out/sin_2D_" + filename + ".jpg")
    else:
        return img



