
import numpy as np
import PIL
import file_manipulation as fm

image_path = "test_photos/corvids.jpg"


def split(path, save = False):
    image = fm.read_image(path)
    name = (image.filename).split("/")[-1]

    arr = np.array(image)
    shape = np.shape(arr)

    r, g, b = np.array(arr), np.array(arr), np.array(arr)

    for i in range(shape[0]):
        for j in range(shape[1]):
            r[i][j][1], r[i][j][2] = 0, 0
            g[i][j][0], g[i][j][2] = 0, 0
            b[i][j][0], b[i][j][1] = 0, 0

    PIL.Image.fromarray(r).show()
    PIL.Image.fromarray(g).show()
    PIL.Image.fromarray(b).show()

