import cv2 as cv
from matplotlib import pyplot as plt
from Board import Board

from Recognition import Recognition

img = cv.imread('examples/5.png', cv.IMREAD_UNCHANGED)

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
    res = Recognition.find_figures(img)
    b = Board()
    print(b.get_fen_by_figures(res))
    add_data(img, res)
    show_plot(img)

find()