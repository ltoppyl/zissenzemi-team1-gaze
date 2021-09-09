def judging_out(x, y):
    import cv2
    import numpy as np

    if ((x < 0) and (y > 0)):
        judge = True

    else:
        judge = False

    print(judge)