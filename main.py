import PIL.ImageQt

import colours as cl
import file_manipulation as fm

cl.split_rgb(fm.read_image("./test_photos/corvids.jpg"), save=True)

