import cv2 as cv
from matplotlib import pyplot as plt

from Recognition import Recognition

def add_data(img, points):
    for pt in points:
        cv.rectangle(img, (pt.x, pt.y), (pt.x + pt.w, pt.y + pt.h), (0,0,0,255), 2)
        cv.putText(img, pt.code.value + pt.color.value ,(pt.x, pt.y), cv.FONT_HERSHEY_COMPLEX, 1, (0,0,0,255), 1)

def show_plot(img):
    plt.imshow(img, cmap = 'gray')
    plt.xticks([])
    plt.yticks([])
    plt.show()

def find():
    fen, res, img = Recognition.get_fen('examples/5.png')
    print(fen)
    add_data(img, res)
    show_plot(img)

find()