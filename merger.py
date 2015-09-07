# -*- coding: utf-8 -*-
__version__ = "0.0.0.0.1b Pre Alpha Alpha"
__author__ = "Tony Martin"

# Creating a host file for blocking ads
# Based on the idea of various adblocking sw running on TomatoUSB
# The goal is to simplify the adblocking sw by having a central point
# that merges and hosts the host file - this will allow the SW
# to simply download the file and with a quick sanitization (alway sanitize - never trust)
# get the most updated host list to block
#
# This program will grab the host files from the sources file in the github project,
# download and merge them into a single file. 

import sys
import urllib2
import subprocess
import hashlib
                
# location of sources of host file data
sourcelist = "https://raw.githubusercontent.com/0xTony/Web-Filters/master/sources"
# a few of the sources need use agent headers or the close the connection
headers = { 'User-Agent' : 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.6) Gecko/20070802 SeaMonkey/1.1.4' }

# Trash old file and overwrite with new contents
def writeToFile(filename, data):
	target = open(filename, 'w')
	target.truncate() 
	target.write(data)  
	target.close()

#download list of sources from github 
def getSources():
	response = urllib2.urlopen(sourcelist)
	return response.read()
	
# With the list of source host files, download each and save
# if the file doesnt download - it will use the old file so not data lost on the latest. 
# will download contents into a file sources-xyz
def downloadSources(sources):
	data = ""
	print sources
	for line in sources.splitlines():
		if not line.startswith("#"):
			sourcehash = "source-" + hashlib.md5(line).hexdigest()[:8] # for file name
			# get data. if it exists, overwrite source file - else if error it wil use old
			try:
				req = urllib2.Request(line, None, headers)
				data = urllib2.urlopen(req).read()
				data = data.replace('127.0.0.1', '0.0.0.0')
				data = data.replace("\r", "\n")
				data = data.replace("  ", " ")
				print "writing to " + sourcehash + " for line " + line
				writeToFile(sourcehash, data)
			except urllib2.URLError, e:
				print "An error %s " %e
				print line
			except:
				print "Bad Source for line " + line

# Take all source-* files, merge and remove duplicates and remove unwanted data
def mergeSources():	
	# Merge the files and filter out unwanted data 
	print "Merging"
	process = subprocess.Popen('sort -u source-* | grep -v "#" | grep -v "localhost" | grep -v "broadcasthost" | grep "0.0.0.0" > hosts',
                             shell=True,stdout=subprocess.PIPE)
    #force a wait for Popen to finish
	process.communicate()

# Main program entry here
def main(argv):
	sources = getSources()
	downloadSources(sources)
	mergeSources()    


if __name__ == "__main__":
  main(sys.argv[1:])
  print("Done")




