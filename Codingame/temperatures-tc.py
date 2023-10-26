import sys, math;t,m,r=list(),6000,0;n=int(input())
for i in input().split():t.append(int(i))
if n==0:m=0
else:
    for i in t:
        if abs(i)<=m:
            if i==-m:continue
            else:r=i
            m=abs(i)
print(r)