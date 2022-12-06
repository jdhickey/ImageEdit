import PIL.ImageQt

import colours as cl
import file_manipulation as fm


cl.transparent(fm.read_image("./out/cmyk/y_corvids.jpg"), 300, show=True)
