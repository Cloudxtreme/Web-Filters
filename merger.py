# -*- coding: utf-8 -*-
__version__ = "0.0.0.0.1 Pre Alpha Alpha"
__author__ = "Tony Martin"

import sys
import urllib2
import subprocess
import hashlib
                
sourcelist = "https://raw.githubusercontent.com/0xTony/Web-Filters/master/sources"
headers = { 'User-Agent' : 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.6) Gecko/20070802 SeaMonkey/1.1.4' }

def writeToFile(filename, data):
	target = open(filename, 'w')
	target.truncate() 
	target.write(data)  
	target.close()

def getSources():
	response = urllib2.urlopen(sourcelist)
	return response.read()
	
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
	
	process = subprocess.Popen('sort -u source-* | grep -v "#" | grep -v "localhost" | grep -v "broadcasthost" > hosts',
                             shell=True,
                            stdout=subprocess.PIPE,
                           )

def downloadSources2(sources):
	data = ""
	print sources
	for line in sources.splitlines():
		if not line.startswith("#"):
			try:
				req = urllib2.Request(line, None, headers)
				data += urllib2.urlopen(req).read()
			except urllib2.URLError, e:
				print "An error %s " %e
				print line
			except:
				print "Bad Source for line " + line
	
			data = data.replace('127.0.0.1', '0.0.0.0')
			data = data.replace("\r", "\n")
			data = data.replace("  ", " ")
	
			writeToFile("temp", data)
			process = subprocess.Popen('grep -v "#" temp | sort -u > hosts',
                             shell=True,
                             stdout=subprocess.PIPE,
                           )




def main(argv):
	sources = getSources()
	downloadSources(sources)    

  
if __name__ == "__main__":
  main(sys.argv[1:])
  print("Done")




