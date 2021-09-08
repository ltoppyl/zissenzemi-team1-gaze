# Zissen_team1_AGE

### ファイル構成のイメージ
- main.py
- get_gaze_vec.py
- judging_out.py
- ax_gaze_estimation_func.py  
- ax_gaze_estimation_utils_func.py

以上の5つのファイルを主に使う。

---

### 各ファイルの用途
【ax_gaze_estimation_func.py, ax_gaze_estimation_utils_func.py】  
> 主な機能はailia-SDKで提供されているものと同じ
> 視線のベクトルを取得する  

【get_gaze_vec.py】  
> ax_gaze_estimation_func.pyで取得した視線のベクトルの値を取得する  
> 取得した値をjudging_out.pyで、カンニングかどうかの判定を行う  

【judgin_out.py】
> 視線のベクトルから、アウトかどうかを判定する関数

【main.py】  
> 各要素を最終的に実行するためのファイル  
> main.pyを実行すると、カメラが立ち上がってカンニングの判定が始まる  

---

### 実行方法
```
python3 main.py
```