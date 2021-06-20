import pyqrcode

def make_qr():
    text = pyqrcode.create('www.google.com')
    print(text.terminal())


make_qr()
