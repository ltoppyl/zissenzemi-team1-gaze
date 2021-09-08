def get_gaze_vec():
    import ax_gaze_estimation_func
    import judging_out

    gaze_vec = ax_gaze_estimation_func.main()


    judging_out.judging_out(gaze_vec)