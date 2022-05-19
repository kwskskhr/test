#学生実験サンプルプログラム
import numpy as np
import matplotlib.pyplot as plt
from control.matlab import *
#パラメータ
N1,D1,D2,D3 = 1,1,1,100
#制御対象の定義
P_open = tf([N1],[D1,D2,D3])
#制御対象の極を計算
print(pole(P_open))