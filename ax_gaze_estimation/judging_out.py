global_judge = False
datasetx = []
datasety = []


def judging_out(x, y):
    global global_judge
    global datasetx 
    global datasety
    judgeDatasetx = []
    judgeDatasety = []

    datasetx.append(x)
    datasety.append(y)

    print(len(datasetx))

    if len(datasetx) > 10:
        for vecx in range(len(datasetx)-11, len(datasetx)):
            print("vecx = " + str(vecx))
            judgeDatasetx.append(datasetx[vecx])
    
        for vecy in range(len(datasety)-11, len(datasety)-1):
            judgeDatasety.append(datasety[vecy])
    
        print("x diff: ", max(judgeDatasetx) - min(judgeDatasetx))
        print("y diff: ", max(judgeDatasety) - min(judgeDatasety))
        if ((max(judgeDatasetx) - min(judgeDatasetx)) > 0.3 ) or ((max(judgeDatasety) -min(judgeDatasety)) > 0.3):
            global_judge = True
        else: global_judge = False
    
    else: global_judge = False


def output_judging_result(visual_img):
    import cv2
    if global_judge == True:
        cv2.putText(visual_img, 'WARNING!', (0, 50), cv2.FONT_HERSHEY_PLAIN, 
                    4, (0, 0, 255), 5, cv2.LINE_AA)
        cv2.imshow('frame', visual_img)

    else :
        cv2.imshow('frame', visual_img)