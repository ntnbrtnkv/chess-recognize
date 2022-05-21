import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
import imutils
import glob

from Figure import Color, FigureCode, Figure

METHOD = cv.TM_SQDIFF_NORMED

def treshhold(code: FigureCode, color: Color):
    if code == FigureCode.Space:
        return 0.999
    if color == Color.White:
        return 0.95
    return 0.87

COLLAPSE_PIXELS = 25

class Recognition:
    @staticmethod
    def get_glob(code, color):
        if code == FigureCode.Space:
            return f'templates/{code.value}/*.png'
        return f'templates/{code.value}/{color.value}/*.png'

    @staticmethod
    def distance(a, b):
        return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5

    @staticmethod
    def find_figures(img):
        result: list[Figure] = []
        global_scale = None
        for color in Color:
            for code in FigureCode:
                template_glob = Recognition.get_glob(code, color)
                loc_collector = []
                for path in glob.glob(template_glob):
                    template = cv.imread(path, cv.IMREAD_UNCHANGED)
                    loc = None
                    scalings = np.linspace(0.6, 1.4, 9)[::-1] if global_scale is None else (global_scale,)
                    for scale in scalings:
                        resized = imutils.resize(template, width = int(template.shape[1] * 1))

                        mask = np.array(cv.split(resized)[3])
                        res = cv.matchTemplate(img, resized, METHOD, mask=mask)
                        w, h = template.shape[:2]

                        if METHOD == 0 or METHOD == 1:
                            res = (2 - res) / 2
                        
                        loc = np.where( res >= treshhold(code, color) )
                        if loc is None:
                            continue
                        global_scale = scale
                        good_points = list(zip(*loc[::-1][:2]))
                        if len(good_points) > 0:
                            loc_collector.extend(good_points)
                            break
                for pt in loc_collector:
                    need_to_add = True
                    figure = Figure(code, color, pt[0], pt[1], w, h)
                    if len(result) == 0:
                        result.append(figure)
                    for existing_pt in result:
                        if Recognition.distance(figure, existing_pt) <= COLLAPSE_PIXELS:
                            need_to_add = False
                            break
                    if need_to_add:
                        result.append(figure)
        return result
        
