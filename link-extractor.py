from bs4 import BeautifulSoup
from urlparse import urlparse
import csv

# input to the medium bookmarks 
path = "medium-bookmarks.html"
content = open(path).read()
content = BeautifulSoup(content, 'html.parser')
content = content.findAll("div", { "class" : "postArticle-content"})

outputPath = "medium-bookmarks.csv"
output = open(outputPath,'a+')


with open(outputPath, 'w') as csvfile:
	fieldnames = ['title', 'link']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()

	for item in content:
		title = item.find("a").find("h3")
		hyperlink = item.find("a")
		
		# extract the text
		if(title is not None):
			title = title.get_text()
		else:
			title = ''

		# extract hyperlink
		if(hyperlink is not None):
			hyperlink = hyperlink.get('href')
			o = urlparse(hyperlink)
			hyperlink = o.scheme + "://" + o.netloc + o.path
		else:
			hyperlink = ''
		

		try:
			title = title.encode('utf-8')
			item = {'title' : title,'link' : hyperlink}
			writer.writerow(item)
		except Exception as e:
			pass
		