
import numpy as np
import PIL
import uuid


def split_rgb(image, name="", show=False, save=False):
    try:
        name = image.filename.split("/")[-1]
    except Exception as e:
        name = name if not name == "" else str(uuid.uuid4())

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


def split_cmyk(image, name="", show=False, save=False):
    try:
        name = image.filename.split("/")[-1]
    except Exception as e:
        name = name if not name == "" else str(uuid.uuid4())

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
    k_val = 255 - k_val * 255
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


def soften(image, p, name="", show=False, save=False):
    try:
        name = image.filename.split("/")[-1]
    except Exception as e:
        name = name if not name == "" else str(uuid.uuid4())

    arr_in = np.array(image)
    shape = np.shape(arr_in)
    arr_out_min = np.zeros(shape)
    arr_out_max = np.zeros(shape)

    for i in range(shape[0]):
        for j in range(shape[1]):
            row = arr_in[i, :, :]
            row = [np.average(row[:, 0]), np.average(row[:, 1]),
                   np.average(row[:, 2])]
            row = np.array(row)  # average colour of row

            col = arr_in[:, j, :]
            col = [np.average(col[:, 0]), np.average(col[:, 1]),
                   np.average(col[:, 2])]
            col = np.array(col)  # average colour of column

            av = np.divide(row + col, 2)

            arr_out_min[i][j] = np.minimum((1 - p) * arr_in[i][j] + p * av,
                                           arr_in[i][j])
            arr_out_max[i][j] = np.maximum((1 - p) * arr_in[i][j] + p * av,
                                           arr_in[i][j])

    img_min = PIL.Image.fromarray(arr_out_min.astype(np.uint8))
    img_max = PIL.Image.fromarray(arr_out_max.astype(np.uint8))

    if show:
        img_min.show()
        img_max.show()
    elif save:
        img_min.save("./out/min_soft_" + name + ".jpg")
        img_max.save("./out/max_soft_" + name + ".jpg")

    else:
        return img_min, img_max
