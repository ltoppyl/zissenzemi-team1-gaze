# Zissen_team1_AGE

###ファイル構成のイメージ
- main.py
- get_gaze_vec.py
- judging_out.py
- ax_gaze_estimation_functionalize.py  
  (ailia-models/face_recognition/ax_gaze_estimation/)

以上の3つのファイルを使う。

---


###各ファイルの用途
【ax_gaze_estimation_functionalize.py】  
- ax_gaze_estimation.pyを使用しやすいように関数化したもの
- 視線のベクトルを取得する
- 取得した値は、get_gaze_vec.pyに送って使う 

【get_gaze_vec.py】  
- ax_gaze_estimation_functionalize.pyファイルから視線のベクトルの値を取得する
- 取得した値をjudging_out.pyに送って、アウトかどうかの判定を行う

【judgin_out.py】
- 視線のベクトルから、アウトかどうかを判定する関数

【main.py】  
- 各要素を最終的に実行するためのファイル 
- イメージとしては、main.pyを実行すると、カメラが立ち上がってカンニングの判定が始まる
