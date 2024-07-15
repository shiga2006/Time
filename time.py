import time
remainder=str(input("Enter a task to remind you at a particular time:"))
ti=float(input("Enter time:"))
ti*=60
time.sleep(ti)
print(remainder)
