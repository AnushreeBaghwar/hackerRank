import glob
import os

listOfFiles = glob.glob("q*.py")

for file in listOfFiles:
	f = open(file,'r')
	lines = f.readlines()
	title = ''
	for line in lines:
		if "https://www.hackerrank.com/" in line:
			link = line.split()[1]
			# print(link)
			readme = open("readme.md","a")
			title = link.split('/')[4].replace('-',' ').capitalize()
			text = '- [{0}]({1}) \n\n'.format(title,link)
			readme.write(text)
	f.close()
	os.rename(file,title+".py")