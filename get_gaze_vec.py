def get_gaze_vec():
    from ailia_models.face_recognition.ax_gaze_estimation import ax_gaze_estimation_functionalize

    gaze_vec = ax_gaze_estimation_functionalize.get_vec()
    print(gaze_vec)
