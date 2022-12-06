import PIL.ImageQt

import colours as cl
import file_manipulation as fm


cl.pixelate(fm.read_image("./test_photos/corvids.jpg"), 300, show=True)
