import pyqrcode
import random

def make_qr():
    back = random.randint(1, 200)
    module = random.randint(1, 200)
    text = pyqrcode.create('www.google.com')
    print(text.terminal(module_color = module, background = back, quiet_zone = 1))

make_qr()
