import cv2 as cv
import easyocr
import os
from PIL import Image

class TextReader:
        def __init__(self):
            self.reader = easyocr.Reader(['en'])
        def extract(self, img):
              textoutput = self.reader.readtext(img)
              totaltext = []

              for word in filter(lambda x: x[-1] > .45, textoutput):
                    text = word[1]
                    totaltext.append(text)    
              return totaltext

if __name__ == '__main__':
    img = cv.imread("documents/data2.jpg")
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    test = TextReader()
    result = test.extract(img)
    full = ' '.join(result)
    print(full)
