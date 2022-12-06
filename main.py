import PIL.ImageQt

import colours as cl
import file_manipulation as fm



cl.soften(fm.read_image("./test_photos/corvids.jpg"), 10, show=True)