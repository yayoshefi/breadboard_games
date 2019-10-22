"""
Based on 
https://max7219.readthedocs.io/en/0.2.3/
"""
def set_serial():
    from luma.core.interface.serial import spi, noop
    # start the led matrix 8Xx device 
    serial = spi(port=0, device=0, gpio=noop())
    return serial

def set_single_device(serial=None):
    if serial is None:
        serial = set_serial()
    from luma.led_matrix.device import max7219
    device = max7219(serial, rotate=2)
    return device

def set_long_device(serial=None):
    if serial is None:
        serial = set_serial()
    from luma.led_matrix.device import max7219
    device = max7219(serial, cascaded=4, rotate=2, block_orientation=-90)
    return device
