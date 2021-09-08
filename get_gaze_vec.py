def get_gaze_vec():
    import ax_gaze_estimation_functionalize
    import judging_out

    gaze_vec = ax_gaze_estimation_functionalize.main()


    # judging_out.judging_out(gaze_vec)