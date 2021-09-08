def get_gaze_vec():
    from ax_gaze_estimation import ax_gaze_estimation_functionalize
    import judging_out

    gaze_vec = ax_gaze_estimation_functionalize.main("--video 0")


    # judging_out.judging_out(gaze_vec)