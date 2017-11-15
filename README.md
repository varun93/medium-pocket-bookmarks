# Save medium bookmarks to pocket!

I have had a habit of bookmarking more articles than I read. But when I want to look up a particular post its hard to find on Medium, they do not allow to search by tags. And ofcourse you ever need to access your bookmarks offline its not possible.(Now I think you can opt for a subscription plan which enables this).


## How to Use?

1. Go to this [link](medium.com/browse/bookmarks) keep scrolling until you hit the bottom of the page. Copy the HTML in the developer console. Remember this is a client side rendered app so HTML can't be grabbed from the page source!
1. Now run the `link-extractor.py` which collects all the urls to a CSV file.
1. Finally run the `pocket-boomark.py`. Make sure you have a Pocket API key, [here](http://www.jamesfmackenzie.com/getting-started-with-the-pocket-developer-api/) is a link to the tutorial which guides you to obtain an access token.


## TODO

The step 1 can be automated by using a Selenium Web Driver.



