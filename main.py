import requests
from bs4 import BeautifulSoup


url = "https://news.ycombinator.com/"
response = requests.get(url)

if response.status_code == 200 :

    soup = BeautifulSoup(response.text, 'html.parser')

    titles = soup.select('.titleline > a')

    for i, title in enumerate(titles[:10], start=1):
        print(f"{i}. {title.get_text()}")


