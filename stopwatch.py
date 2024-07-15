import time
import os

s=0
m=0
h=0

input("Press 'enter' to start stopwatch...")

while True:
    print(h, ":", m, ":", s)
    time.sleep(1)
    s = s+1
    if s == 60:
        s = 0
        m = m+1
        time.sleep(1)
        print(h, ":", m, ":", s)
    elif m == 60:
        m = 0
        h = h+1
        time.sleep(1)
        print(h, ":", m, ":", s)

    os.system("clear")    
                   
