import subprocess as sp
import os
import sys
import time

SLEEP_VAL = 5
MUSIC_PLAYER_LOC = '/usr/bin/totem-audio-preview'
MUSIC_LOC = '~/Music/titanic_whistle.mp3'

def ping_check(ip):
	cmd_str = 'ping ' + ip.strip() + ' -c 1'
	
	x = os.popen(cmd_str)
	x = x.read()

	x = int(x.split('\n')[-3].split(',')[1].strip().split(' ')[0])

	if x == 1:
		return 1
	else:
		return 0

def main():
	while True:
		if ping_check(sys.argv[1]) is 1:
			print 'There is a glorious reply ^_^'
			os.system(MUSIC_PLAYER_LOC + ' ' +  MUSIC_LOC)
			break

		else:
			print 'No reply for you ;_;'
			time.sleep(SLEEP_VAL)

if __name__ == '__main__':
	main()

"""
What is happening while trying to parse the ping reply?
# Split the output according to newlines
# Went to the 3rd line from the last
# Split it according to ',' (commas)
# Went to the 2nd position of the array which contains how many replies received
# Striped whitespaces around it
# Split it according to spaces
# Went to the 1st position of the array which contains the exact number of repies in character format
"""
