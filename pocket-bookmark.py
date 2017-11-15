import requests
# tutorial to obtain access tokens
# http://www.jamesfmackenzie.com/getting-started-with-the-pocket-developer-api/
url="https://getpocket.com/v3/add"

# obita
access_token = ''
consumer_key = ''

# place all the links from the csv to a text file(medium-bookmark-urls.txt)
for bookmarkUrl in open('medium-bookmark-urls.txt').readlines():
	bookmarkUrl = bookmarkUrl.strip()
	payload = {'access_token': access_token, 'consumer_key': consumer_key,'url' : bookmarkUrl}
	response = requests.post(url, data=payload)

	print(response.text) #TEXT/HTML
	print(response.status_code, response.reason) #HTTP

