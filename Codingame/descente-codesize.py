import sys,math;m=list()
while True:
    m.clear()
    for i in range(8):h=int(input());m.append(h)
    t=m[0];b=0
    for x in range(8):
        if m[x]>t:t=m[x];b=x
    print(b)