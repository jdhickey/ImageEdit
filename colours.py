import numpy
import numpy as np
import PIL
import file_manipulation as fm


def split_rgb(path, show=False, save=False):
    image = fm.read_image(path)
    name = image.filename.split("/")[-1]

    arr = np.array(image)
    r_arr, g_arr, b_arr = np.array(arr), np.array(arr), np.array(arr)

    # Turns off the other two colour channels for the red, green and blue image
    r_arr[..., 1], r_arr[..., 2] = 0, 0
    g_arr[..., 0], g_arr[..., 2] = 0, 0
    b_arr[..., 0], b_arr[..., 1] = 0, 0

    # Converts the image arrays to image objects
    r_img = PIL.Image.fromarray(r_arr)
    g_img = PIL.Image.fromarray(g_arr)
    b_img = PIL.Image.fromarray(b_arr)

    if save:
        r_img.save("./out/rgb/r_" + name)
        g_img.save("./out/rgb/g_" + name)
        b_img.save("./out/rgb/b_" + name)
    elif show:
        r_img.show()
        g_img.show()
        b_img.show()
    else:
        return r_img, g_img, b_img


def split_cmyk(path, show=False, save=False):
    image = fm.read_image(path)
    name = image.filename.split("/")[-1]

    # Split the array into a red, green, and blue channel
    arr = np.array(image)
    r_arr = arr[..., 0]
    g_arr = arr[..., 1]
    b_arr = arr[..., 2]

    # Find the maximum colour value of each pixel
    mx = np.maximum(np.maximum(r_arr, g_arr), b_arr)

    # The key value of each pixel
    k_val = np.divide((255 - mx), 255)

    # Calculates: c, m, and y for each pixel
    c_val = np.divide((mx - r_arr), mx) * 255 * k_val
    m_val = np.divide((mx - g_arr), mx) * 255 * k_val
    y_val = np.divide((mx - b_arr), mx) * 255 * k_val

    # Creates a new image array for cyan, magenta and yellow
    c_arr, m_arr, y_arr, k_arr = [np.array(arr), np.array(arr),
                                  np.array(arr), np.array(arr)]
    c_arr[..., 0], c_arr[..., 1], c_arr[..., 2] = 0, c_val, c_val
    m_arr[..., 0], m_arr[..., 1], m_arr[..., 2] = m_val, 0, m_val
    y_arr[..., 0], y_arr[..., 1], y_arr[..., 2] = y_val, y_val, 0

    # Creates a new image array for black/white
    k_val = k_val * 255
    k_arr[..., 0], k_arr[..., 1], k_arr[..., 2] = k_val, k_val, k_val

    # Converts the image arrays to image objects
    c_img = PIL.Image.fromarray(c_arr)
    m_img = PIL.Image.fromarray(m_arr)
    y_img = PIL.Image.fromarray(y_arr)
    k_img = PIL.Image.fromarray(k_arr)

    if save:
        c_img.save("./out/cmyk/c_" + name)
        m_img.save("./out/cmyk/m_" + name)
        y_img.save("./out/cmyk/y_" + name)
        k_img.save("./out/cmyk/k_" + name)
    elif show:
        c_img.show()
        m_img.show()
        y_img.show()
        k_img.show()
    else:
        return c_img, m_img, y_img, k_img

