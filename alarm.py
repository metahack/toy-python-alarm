#!/usr/bin/env python3.1 

# to make this program easier to use, consider running these two commands:
# ~/chmod +x alarm.py // lets the program run as an executable 
# ~/sudo ln alarm.py /usr/local/bin/alarm // puts a link into a $PATH folder
import sys
import time
import os

in_hour = sys.argv[1]
in_min = sys.argv[2]


not_executed = 1

while(not_executed):
	dt = list(time.localtime())
	hour = dt[3]
	minute = dt[4]
	second = dt[5]
	print(str(hour) + " " + str(minute) + " " + str(second))
	time.sleep(1)
	print("awaken at {0}  {1}".format(in_hour, in_min))

	if hour == int(in_hour) and minute == int(in_min):
		os.popen("open   /Volumes/Music/iTunes/iTunes\ Media/Music/Donald\ Fagen/The\ Nightfly/01\ I.G.Y..m4a")
		not_executed = 0
