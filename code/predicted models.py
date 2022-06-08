import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def logistic_increase_function(t, K, P0, r):
    t0 = 11
    # t:time   t0:initial time    P0:initial_value    K:capacity  r:increase_rate
    exp_value = np.exp(r * (t - t0))
    return (K * exp_value * P0) / (K + (exp_value - 1) * P0)


fast_r = 0.08
slow_r = 0.10


def faster_logistic_increase_function(t, K, P0, ):
    return logistic_increase_function(t, K, P0, r=fast_r)


def slower_logistic_increase_function(t, K, P0, ):
    return logistic_increase_function(t, K, P0, r=slow_r)


'''



'''
#
#  日期及感染人数
# t=[27,28,29 ,30, 31, 1, 2,  3,  4,  5,  6,  7  ,8| 8月]#14
t = [11,18,19,20 ,21, 22,   23, 24,  25,  26,  27,  28,  29  ,30 , 31]
t = np.array(t)
# P=[41,45,62,291,440,571,830,1287,1975,2744,4515,5974,7711,9692]
P = [3117946,3711413,3773260,3834677,3899211,3970121,4038816,4112531,4178970,4233923,4290037,4356206,4426982 , 4495105,4562107]
#↑美国（7月）
#巴西(现在--8月)：3359570,3717156,3761391,3804803；3908272，3950931，3997865，4041638，4091801，4123000，4137521，4147794，4162073
P = np.array(P)

# 用最小二乘法估计拟合
# popt, pcov = curve_fit(logistic_increase_function, t, P)
popt_fast, pcov_fast = curve_fit(faster_logistic_increase_function, t, P)
popt_slow, pcov_slow = curve_fit(slower_logistic_increase_function, t, P)
# 获取popt里面是拟合系数
print("K:capacity  P0:initial_value   r:increase_rate   t:time")
# print(popt)
# 拟合后预测的P值
# P_predict = logistic_increase_function(t,popt[0],popt[1],popt[2])
P_predict_fast = faster_logistic_increase_function(t, popt_fast[0], popt_fast[1])
P_predict_slow = slower_logistic_increase_function(t, popt_slow[0], popt_slow[1])
# 未来长期预测
# future=[11,18,19,20 ,21, 22, 23, 24,  25,  26,  27,28,29,30,31,41,51,61,71,81,91,101]
# future=np.array(future)
# future_predict=logistic_increase_function(future,popt[0],popt[1],popt[2])
# 近期情况预测
#16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29
tomorrow = [32,33,34,35,36,37,38,39,40,41,42,43,44,45]
tomorrow = np.array(tomorrow)
# tomorrow_predict=logistic_increase_function(tomorrow,popt[0],popt[1],popt[2])
tomorrow_predict_fast = logistic_increase_function(tomorrow, popt_fast[0], popt_fast[1], r=fast_r)
tomorrow_predict_slow = logistic_increase_function(tomorrow, popt_slow[0], popt_slow[1], r=slow_r)

# 绘图
plot1 = plt.plot(t, P, 's', label="confimed infected people number")
# plot2 = plt.plot(t, P_predict, 'r',label='predict infected people number')
# plot3 = plt.plot(tomorrow, tomorrow_predict, 's',label='predict infected people number')
plot2 = plt.plot(tomorrow, tomorrow_predict_fast, 's', label='predict infected people number fast')
plot3 = plt.plot(tomorrow, tomorrow_predict_fast, 'r')
plot4 = plt.plot(tomorrow, tomorrow_predict_slow, 's', label='predict infected people number slow')
plot5 = plt.plot(tomorrow, tomorrow_predict_slow, 'g')
plot6 = plt.plot(t, P_predict_fast, 'b', label='confirmed infected people number')

plt.xlabel('time')
plt.ylabel('confimed infected people number')

plt.legend(loc=0)  # 指定legend的位置右下角

print("32\n")
print(faster_logistic_increase_function(np.array(32), popt_fast[0], popt_fast[1]))
print(slower_logistic_increase_function(np.array(32), popt_slow[0], popt_slow[1]))

print("33\n")
print(faster_logistic_increase_function(np.array(33), popt_fast[0], popt_fast[1]))
print(slower_logistic_increase_function(np.array(33), popt_slow[0], popt_slow[1]))

plt.show()

print("Program done!")