

import sys
import time
averageactive = 30
activetime = [5,10,15,20,25,30]
sys.stdout.write("Enter name:")
name = sys.stdin.readline().strip()
sys.stdout.write ("Hello" + " "+name+ "! What was the total minutes you spent active today?")
totalactivetime = int(sys.stdin.readline().strip())

while averageactive < totalactivetime:
    sys.stdout.write("You need to increase that.\n")
    
