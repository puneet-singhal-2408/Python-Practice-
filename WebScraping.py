from bs4 import BeautifulSoup

import requests

# createing a variable and storing URL 
r = requests.get("https://www.w3schools.com/python/python_classes.asp")

#converting site data into plain text and storing it into data variable

data = r.text

print(data)

link = BeautifulSoup(data)
print(link)





