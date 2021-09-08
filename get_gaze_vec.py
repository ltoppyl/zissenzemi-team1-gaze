def get_gaze_vec():
    from ax_gaze_estimation import ax_gaze_estimation
    import judging_out

    gaze_vec = ax_gaze_estimation.main()


    judging_out.judging_out(gaze_vec)