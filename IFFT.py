import time
import random
import math

#回傳w^x(以n為底)
def w(x,n):
    return complex(math.cos(2*math.pi/n),math.sin(2*math.pi/n))**x

#根據divide and conquar計算，time complexity為O(n*log(n))
def ifft(a):
    if len(a) == 1:
        return a
    else:
        n = len(a)
        a_odd = []
        a_even = []
        for i in range(n):
            if (i+1)%2 == 1:
                a_odd.append(a[i])
            else:
                a_even.append(a[i])
        s_odd = ifft(a_odd)
        s_even= ifft(a_even)

        s = [0]*n
        for i in range(n//2):
            s[i] = s_odd[i]+s_even[i]*w(i,n)
            s[i+(n//2)] = s_odd[i]+s_even[i]*w(i+(n//2),n)
        return s

t = 0
count = 0
while(t < 60):

    first = time.time()

    #從[0,1]區間中隨機選擇1024個IFFT input
    a =  [random.uniform(0,1) for i in range(1024)]
    s = ifft(a) #s為做完ifft的結果

    second = time.time()

    count += 1
    t += second-first

print(count)

