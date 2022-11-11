import requests
from bs4 import BeautifulSoup


def random_quote():
    url = "http://www.bashorg.org/casual"

    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')
    result = soup.find('div', {"class" : 'q'}).find_all("div")
    return result[-1].text

