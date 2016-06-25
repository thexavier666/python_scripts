"""
MULTITHREADED FILE DOWNLOADER
"""

import subprocess as sp
import sys
import threading

def download_file(file_name, i, ext):
	cmd_str = ['wget', file_name.strip(), '-O', ('file_%d.' + ext) % i]
	sp.call(cmd_str)

def main():
	dl = open(sys.argv[1], 'r')

	i = 1

	ext = 'pdf'

	for line in dl:		
		t = threading.Thread(target=download_file, args=(line, i, ext,))
		t.start()
		i = i + 1

if __name__ == '__main__':
	main()
