Ans="""

1. What web server software issued by www.snopes.com?Analysis –
The domain name be found from host header so we will set host header column where we will see all domain name.
Select any HTTP request and expand the Hypertext Transfer Protocol then right click on Host header and then Apply as Column
Now we can see our host www.snopes.com in host column.Right click on the selected packet and then select Follow TCP stream.
Now we can see the webserver name in server header it is Microsoft IIS 5.0

2.  About what cell phone problem is the client concerned?
Analysis – Client talking about cell so we search for cell keyword in whole packets.
We will use regular express for searching the cell keyword.
Apply frame matches “(?!) cell”
After applying the filter now, we will start to check every HTTP request.
We noticed in the first HTTP request cell keyword is in URL and it was about cell phone charging issue.

3. According to Zillow, what instrument will Ryan learn to play?
Analysis – As we did in the last challenge, we will apply a regular express filter for the Zillow keyword.
Apply frame matched “(?!) zillow”
After applying the filter, we found only one packet with the Zillow keyword
Select the packet and expand the Hypertext Transfer Protocol
tab right click on it go to Protocol Preferences and check Allow subdissector to resemble TCP stream
Now go to file and select Export Objects > HTTP. It will save all objects from the packet.
Click on Save all
After saving all files in a directory and we found a swf file with name Zillow.
After opening the flash file, we saw that Zillow was trying to learn saxophone.
Answer is saxophone but file is swf so cant play

4.  How many web servers are running Apache?
Analysis – The web server name can be retrieved from HTTP response header.
So will apply filter http. response and we can see all http response packets
Now we will set the server header as column select any packet and right click on it then select Apply as Column
Now can see the server column where all server name is showing.
Now we have to check how many Apache packets are there we can’t count manually for each packet
so we will apply another filter http.server contains “Apache”
After applying filter go to Statistics > Endpoints
It will show all connections
Check the limit to display filter then it will show the actual Apache connections. Now there are showing 22 connections
but will exclude 192.168.1.71 because it is client’s IP not a server IP so there are actual 21 Apache servers.


"""
