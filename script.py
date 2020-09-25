import glob
import os

listOfFiles = glob.glob("q*.py")

for file in listOfFiles:
	f = open(file,'r')
	lines = f.readlines()
	title = ''
	for line in lines:
		if "https://www.hackerrank.com/" in line:
			qlink = line.split()[1]
			# print(link)
			readme = open("readme.md","a")
			title = qlink.split('/')[4].replace('-',' ').capitalize()
			link = 'https://github.com/emoanu/hackerRank/blob/master/'+title.replace(' ','%20')+'.py'
			text = '\n{2}\n - [Question]({0})\n - [Solution]({1})\n\n'.format(qlink,link,title)
			readme.write(text)
	f.close()
	os.rename(file,title+".py")