global_judge = False

def judging_out(x, y):
    import numpy as np

    if ((x < 0) and (y > 0)):
        global_judge = True
    else:
        global_judge = False

    print(global_judge)


def output_judging_result(visual_img):
    import cv2
    if global_judge == True:
        output_img = cv2.putText(visual_img, "OUT!", (50, 50), cv2.FONT_HERSHEY_PLAIN, 100, (0, 0, 255), 4, cv2.LINE_AA)
        return output_img
    else :
        return visual_img