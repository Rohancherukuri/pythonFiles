import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)
soup = BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify)
title = soup.title
# print(title)
# print(type(title))
paras = soup.find_all('p')
# print(paras)
anchors = soup.find_all('a')
# print(anchors)

# print(soup.find('p')['class'])
# print(soup.find_all("p",class_ = "lead"))
# print(soup.get_text())
all_links = set()
for links in anchors:
    if(links.get("href") != "#"):
        linksText = "https://codewithharry.com/"+ links.get("href")
        all_links.add(links)
        print(linksText)

markup = "<p> <!-- This is a comment --> </p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p))