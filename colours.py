import numpy
import numpy as np
import PIL
import file_manipulation as fm


def split(path, show = False, save = False):
    image = fm.read_image(path)
    name = image.filename.split("/")[-1]

    arr = np.array(image)
    r_arr, g_arr, b_arr = np.array(arr), np.array(arr), np.array(arr)

    r_arr[..., 1], r_arr[..., 2] = 0, 0
    g_arr[..., 0], g_arr[..., 2] = 0, 0
    b_arr[..., 0], b_arr[..., 1] = 0, 0

    r_img = PIL.Image.fromarray(r_arr)
    g_img = PIL.Image.fromarray(g_arr)
    b_img = PIL.Image.fromarray(b_arr)

    if save:
        r_img.save("./out/r_" + name)
        g_img.save("./out/g_" + name)
        b_img.save("./out/b_" + name)

    if show:
        r_img.show()
        g_img.show()
        b_img.show()


def split_cmyk(path, show = False, save = False):
    image = fm.read_image(path)
    name = image.filename.split("/")[-1]

    arr = np.array(image)



