from ImageToText import TextReader
from GPTapp import GPT4
import cv2 as cv

if __name__ == '__main__':
    gpt = GPT4()
    img = cv.imread("documents/data1.jpg")
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    test = TextReader()
    result = test.extract(img)
    full = ' '.join(result)
    result = gpt.predict(full)
    print("Full Text:\n",full)
    print("\n")
    print("Classification:\n",result)