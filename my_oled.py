from machine import Pin, SoftI2C
import ssd1306
import gfx

# Initialize I2C and OLED
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
graphics = gfx.GFX(oled_width, oled_height, oled.pixel)

def print_text(msg, x=0, y=0):
    print('I am printing text')
    oled.fill(0)
    oled.text(msg, x, y)
    oled.show()

def plot_line(*args, **kwargs):
    print('I am plotting a line')