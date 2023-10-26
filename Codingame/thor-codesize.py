import sys,math;a,b,c,d=[int(i) for i in input().split()];e,f=c,d;
while True:
    r=int(input());r,h="",""
    if e>a:r="W";e-=1
    elif e<a:r="E";e+=1
    if f>b:h="N";f-=1
    elif f<b:h="S";f+=1      
    print(h+r)

