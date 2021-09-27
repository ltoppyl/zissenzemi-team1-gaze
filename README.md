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

【judgin_out.py】
> 視線のベクトルから、アウトかどうかを判定するファイル  
> アウトと判定された時に、アウトの表示を画面に乗せる

【main.py】  
> 各要素を最終的に実行するためのファイル  
> main.pyを実行すると、カメラが立ち上がってカンニングの判定が始まる  

---
### 実行環境の構築
- https://github.com/axinc-ai/ailia-models
- https://github.com/axinc-ai/ailia-models/blob/master/TUTORIAL.md  

２つ目のリンクのTUTORIAL.mdを参考に、ailia SDKをinstallする。  
途中libailia.dllのファイルの置き場所には気をつける(OSによって異なる) 。  
TUTOIRAL.mdが完了した後、以下の方法で実行すれば動くはずです。 


---

### 実行方法
```
python3 main.py
```

---
### 注意事項
- 現状では、視線の値がNoneになった時、カメラが落ちるというバグがあるため、常にカメラの前にいる必要がある。