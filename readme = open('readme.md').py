import re
readme = open('readme.md')
lines = readme.readlines()

with open("test.md","a") as f:
	for line in lines:
		if '- [' in line:
			title = line.split('[')[1].split(']')[0]
			print(title) 
			regex = r'[^\[\]]+(?=\])'
			line = re.sub(regex,'Question',line)
			link = 'https://github.com/emoanu/hackerRank/blob/master/'+title.replace(' ','%20')+'.py'
			line = '{0} - [Solution]({1})\n'.format(line,link)
		print(line)
