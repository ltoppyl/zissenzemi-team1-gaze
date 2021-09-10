def judging_out(x, y):
    global global_judge
    import numpy as np

    if ((x < 0) and (y > 0)):
        global_judge = True
    else:
        global_judge = False

    # print(global_judge)


def output_judging_result(visual_img):
    print(global_judge)
    import cv2
    if global_judge == True:
        cv2.putText(visual_img, 'OUT!', (0, 50), cv2.FONT_HERSHEY_PLAIN, 
                    4, (0, 0, 255), 5, cv2.LINE_AA)
        cv2.imshow('frame', visual_img)

    else :
        cv2.imshow('frame', visual_img)