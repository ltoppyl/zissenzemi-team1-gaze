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

    if(len(datasetx) <= 100):
        print(len(datasetx))

    # ファイルへの書き込み用
    filex = open("x.txt", "a")
    filey = open("y.txt", "a")
    filexx =open("xx.txt", "a")


    second = 50
    if len(datasetx) > second:
        for vecx in range(len(datasetx)-(second + 1), len(datasetx)):
            judgeDatasetx.append(datasetx[vecx])
    
        for vecy in range(len(datasety)-(second + 1), len(datasety)-1):
            judgeDatasety.append(datasety[vecy])
        
        print("x diff: ", max(judgeDatasetx) - min(judgeDatasetx))       
        print("y diff: ", max(judgeDatasety) - min(judgeDatasety))
        filexx.write(str(x))
        filexx.write("\n")
        filex.write(str(max(judgeDatasetx) - min(judgeDatasetx)))
        filex.write("\n")
        filey.write(str(max(judgeDatasety) - min(judgeDatasety)))
        filey.write("\n")
        print("-----------------------------")
        if ((max(judgeDatasetx) - min(judgeDatasetx)) > 0.4) or ((max(judgeDatasety) -min(judgeDatasety)) > 0.5):
            global_judge = True
        else: global_judge = False
    
    else: global_judge = False

    filex.close()
    filey.close()
    filexx.close()


def output_judging_result(visual_img):
    import cv2
    if global_judge == True:
        cv2.putText(visual_img, 'WARNING!', (0, 50), cv2.FONT_HERSHEY_PLAIN, 
                    4, (0, 0, 255), 5, cv2.LINE_AA)
        cv2.imshow('frame', visual_img)

    else :
        cv2.imshow('frame', visual_img)