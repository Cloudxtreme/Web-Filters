# Web-Filters
The purpose of this project is to collect various malware and ad blocking tools used by the ad blocking software in Tomato USB routers. 

Merging of multiple fitlers with the addition of my own for usage in host files and routers to filter unwanted sites (malware and ads)

Merged files are updated daily. 
The files are merged information from the following sites:
http://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&mimetype=plaintext
http://winhelp2002.mvps.org/hosts.txt
http://hostsfile.mine.nu/Hosts
http://adaway.org/hosts.txt
http://hosts-file.net/ad_servers.txt
http://www.malwaredomainlist.com/hostslist/hosts.txt
http://adblock.mahakala.is
http://adblock.gjtech.net/?format=unix-hosts

I also add in the following to blacklist:
WinXBlockList - This is a listing of the now built in windows malware/tracking sites
AdBlock - My own listing of in app ads I find. 

If you know of any other good block lists - specially for iOS and Android in app adds, please let me know. 

The merged files are
hostsblocklist - Block list in host file format
blocklist - Just the listing of addresses to block
sources - Listing of sources used to get data to merge

ToDo: 
Add my own Tomato adBlock script with my own updates.
Add my pythin script used to merge the files.
Add a windows, Linux, OSX script that will download the proper host file and update block listing with instruction on how to set it up to kick off on a timed basis. 
