import serial
from vpython import *
print("hello world")

import time

for i in range(10):
    print(f"Progress: {i * 10}%", end='\r')
    time.sleep(1)