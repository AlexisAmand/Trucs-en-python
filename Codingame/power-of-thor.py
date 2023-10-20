# puzzle : power-of-thor
# le code est compressé, ça faisait partie des consignes

import sys, math;lx,ly,tx,ty=[int(i) for i in input().split()];trX,trY=tx,ty;
while True:
    r = int(input());dX, dY = "",""
    if trX>lx:dX="W";trX-=1
    elif trX<lx:dX="E";trX+=1
    if trY>ly:dY="N";trY-=1
    elif trY<ly:dY="S";trY+=1      
    print(dY+dX)

