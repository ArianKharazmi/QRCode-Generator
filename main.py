# Python Libraries
import requests
import qrcode
from datetime import date
import sys
import numpy as np
import cv2
import selenium

import frame


Generate = qrcode
Reverse = cv2

today = date.today()
print("QRCode Generation completed on " + str(today) + ". Try it out!")

# Input link or text entry into qrcode.make section
qr = qrcode.QRCode(version = 1,
                   error_correction = qrcode.constants.ERROR_CORRECT_L,
                   box_size = 50,
                   border = 2)

# Edit your text entry/URL
qr.make(fit = True)
qr.add_data("www.google.com")
# Customization Options
img = qr.make_image(fill_color="black", back_color = "white")
img.save("QRCode.png")