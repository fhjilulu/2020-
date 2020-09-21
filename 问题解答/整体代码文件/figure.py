import numpy as np
#import matplotlib as mpl
import matplotlib.pyplot as plt
import math
from matplotlib.pyplot import MultipleLocator

####计算delta
data = np.array([-0.3023411,44.95573, 0.3013696, 4696.651, 0.6106065, 263.1876, 70.22765, 261.8852, 17.16376, 54.98129, 4.423843, 13110566.0, 15048699.0, 30.73839, -0.000351563, 0.6894531, 6.879375, 0.6679688, 6.946113, 82.38895, 30.73088, 0.26625, 0.338789, 86.06048, 0.17, 12265800.0])

final = np.array([-0.30270355,
                   419.90394,
                  0.26516671,
                   3249.6517,
                   0.2852505,
                   298.82434,
                   64.433668,
                   276.30194,
                   14.367394,
                   53.082179,
                   5.2827237,
                   1592945.3,
                   1405705.8,
                    29.12553,
                   74.070261,
                   149.70223,
                    77.51791,
                   199.19175,
                   153.94465,
                   78.094376,
                   28.683196,
                   100.36345,
                    155.7536,
                   66.865152,
                   1.6558382,
                   255922.64])

delta = np.array([0.1,
                    50,
                    0.01,
                    50,
                    0.2,
                    1,
                    1,
                    1,
                    5,
                    1,
                    0.5,
                    100000,
                    100000,
                    1,
                    1,
                    2,
                    1,
                    2,
                    1,
                    5,
                    1,
                    2,
                    2,
                    10,
                    0.1,
                    100000])

times = np.zeros(26)

sum = 0

for i in range(26):
    s_um = math.ceil((abs(final[i] - data[i])) / delta[i])
    times[i] = s_um
    if s_um > sum:
        sum = s_um
'''
#输出delta总轮数
'''
#print(sum) = 147
#print(times)

#这里导入你自己的数据
#......
x_axix = np.zeros(147)
for m in range(147):
    x_axix[m] = m
#print(x_axix)
#......
XinWan_value = np.zeros(147)
Sulfur_value = np.zeros(147)

'''
#算每delta辛烷值和硫含量
'''

newdata = np.array([-0.3023411,44.95573, 0.3013696, 4696.651, 0.6106065, 263.1876, 70.22765, 261.8852, 17.16376, 54.98129, 4.423843, 13110566.0, 15048699.0, 30.73839, -0.000351563, 0.6894531, 6.879375, 0.6679688, 6.946113, 82.38895, 30.73088, 0.26625, 0.338789, 86.06048, 0.17, 12265800.0])

wx = np.array([-8.39852885e-01 ,-5.78392159e-04, -9.00039251e-01 , 3.27982371e-05,
  -2.45961636e-02, -1.20196508e-02 , 3.61825729e-03 , 8.74599458e-03,
  -7.16030606e-03 , 8.05818585e-04 ,-1.68855936e-01 ,-1.02050829e-08,
   1.19154439e-08 , 4.49289655e-01, -7.43813049e-03 ,-6.41928776e-03,
   3.96118423e-02 , 7.46792692e-03 , 2.02914936e-03 ,-7.84923717e-01,
   1.64004157e+00 ,-1.75400207e-02 ,-7.04862866e-03 , 2.89658835e-03,
   9.70694294e-02 , 2.41744228e-08])

bx = 2.33114831

ws = np.array([ 1.61571311e+00, -4.17410867e-03 , 6.02873384e+00 , 5.80761791e-04,
   6.94520457e-01 , 1.08306508e-01,  3.35009899e-02 ,-6.62069999e-02,
   4.50795183e-02 ,-2.06503231e-01, -5.67479031e-01, -3.86183030e-08,
   8.72845010e-08,  7.28061582e+01 , 2.94155744e-01 ,-4.35532725e-02,
   4.08072475e-01 , 1.06285537e-01, -4.51888259e-01, -2.15275029e+01,
  -1.52295257e+01, -8.01867886e-01 , 4.81421552e-01 , 5.35500184e-02,
  -2.07241542e+00 ,-3.97717862e-07])

bs = 3.00531845

for j in range(147): 
    for k in range(26):
        if(times[k] != 0):
            if (times[k]-1) != 0:
                if final[k] > newdata[k]:
                    newdata[k] += delta[k]
                else:
                    newdata[k] -= delta[k]
            elif (times[k]-1) == 0:
                newdata[k] = final[k]
            times[k]-=1
    #print(times)
    
    XinWan_value[j] = 89.4 - (np.dot(wx,newdata) + bx)
    Sulfur_value[j] = np.dot(ws,newdata) + bs
    Sulfur_value[j] /= 4
    if Sulfur_value[j]<=3.2:
        Sulfur_value[j] = 3.2


print(data)
print(newdata)
print(final)
#开始画图
plt.title('Result Analysis',fontsize=16)
#plt.grid()


plt.plot(x_axix, XinWan_value, color='blue', label='XinWan value')

plt.plot(x_axix, Sulfur_value,  color='red', label='Sulfur value')

plt.legend() # 显示图例

plt.xlabel('delta times',fontsize=14)

plt.ylabel('value',fontsize=14)


x_major_locator=MultipleLocator(10)
#把x轴的刻度间隔设置为1，并存在变量里
y_major_locator=MultipleLocator(10)
#把y轴的刻度间隔设置为0.5，并存在变量里
ax=plt.gca()
#ax为两条坐标轴的实例
ax.xaxis.set_major_locator(x_major_locator)
#把x轴的主刻度设置为1的倍数
ax.yaxis.set_major_locator(y_major_locator)
#把y轴的主刻度设置为0.5的倍数

plt.savefig('figure.jpg')

plt.show()

#python 一个折线图绘制多个曲线