import requests
from bs4 import BeautifulSoup

try:
    url = "https://www.flipkart.com/"
    r = requests.get(url)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent,'html.parser')

    name  = soup.title.string
    body = soup.find('p').get_text()
    print(name)
    print(body)
except Exception as e:
    print("There is an error: "+str(e))