import random
import time
import math

u = []
#根據w的定義去計算1024x1024的矩陣
for i in range(1024):
    v = []
    for j in range(1024):
        v.append(complex(math.cos(2*math.pi*i*(j/1024)),math.sin(2*math.pi*i*(j/1024))))
    u.append(v)

t = 0
count = 0
while(t < 60):
    first = time.time()

    a = [random.uniform(0,1) for i in range(1024)] #從[0,1]區間中隨機選擇1024個IDFT input
    s = [] #用來存IDFT結果的list
    
    #根據原始的定義去計算，time complexity 為O(n^2)
    for i in range(1024):
        x = 0
        for j in range(1024):
            x  += u[i][j]*a[j]
        s.append(x)

    second = time.time()
    count += 1
    t += (second-first)

print(count)


