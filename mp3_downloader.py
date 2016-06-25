import subprocess as sp
import sys
import os
import time

def download_mp3s():
	if len(sys.argv) < 2:
		print "File not found!"
		return 1
	
	file_links = open(sys.argv[1], 'r')

	for line in file_links:
		cmd = [
		'youtube-dl',			# primary command 
		'-x',				# extract audio
		'--audio-quality', '0',		# selecting best audio quality
		'--audio-format', 'mp3',	# setting audio format as mp3
		line]				# selecting each youtube link from the file
		
		sp.call(cmd)

	file_links.close()

	r = int(time.time())
	folder_name = "youtube_mp3_" + str(r)
	os.makedirs(folder_name)

	cmd = 'mv *.mp3 %s' % folder_name

	sp.call(cmd, shell = True)

	return 0

if __name__ == '__main__':
	download_mp3s()
