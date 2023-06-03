import cv2
import numpy as np
from pyzbar.pyzbar import decode


img = cv2.imread('Untitled.png')

code = decode(image=img)

for i in code:
    result = i.data
    print(result)
    print(str(result)[2:-1])