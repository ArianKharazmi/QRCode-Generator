# Python Libraries
import requests
import qrcode
from datetime import date
import sys
import numpy as np
import cv2
import selenium

Generate = qrcode
Reverse = cv2


print("Welcome to the QRCode Tool! Which option will you choose?")
answer = input(
    "Generate QR Code or use Reverse QR Code Search? **Type of the two choices:** (Generate/Reverse) ").lower()
if answer == Generate:
    today = date.today()
    print("QRCode Generation completed on " + str(today) + ". Try it out!")

    # Input link or text entry into qrcode.make section
    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=50,
                       border=2)

    # Edit your text entry/URL
    qr.make(fit=True)
    qr.add_data("Your QR Code")
    # Customization Options
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("QRCodeIMG.PNG")

if answer == Reverse:
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()



#today = date.today()
#print("QRCode Generation completed on " + str(today) + ". Try it out!")

# Input link or text entry into qrcode.make section
#qr = qrcode.QRCode(version = 1,
                   #error_correction = qrcode.constants.ERROR_CORRECT_L,
                   #box_size = 50,
                   #border = 2)

# Edit your text entry/URL
#qr.make(fit = True)
#qr.add_data("Your QR Code")
# Customization Options
#img = qr.make_image(fill_color="black", back_color = "white")
#img.save("QRCodeIMG.PNG")
