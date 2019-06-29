import requests
from bs4 import BeautifulSoup
import json


def getKanji(URL):
    url = requests.get(URL).text
    soup = BeautifulSoup(url, features='html.parser')
    table = soup.findAll('table')[1]
    rows = table.find_all('tr')
    data = []
    i = 0
    for row in rows:
        if i == 0:
            i += 1
            continue
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        kanji = {
            "Kanji": cols[0],
            "Onyomi": cols[1].split(' '),
            "Kunyomi": cols[2].split(' '),
            "Meaning": cols[3].split(',')
        }
        data.append(kanji)
    return data


JPLT_URL = [
    'http://www.tanos.co.uk/jlpt/jlpt5/kanji/',
    'http://www.tanos.co.uk/jlpt/jlpt4/kanji/',
    'http://www.tanos.co.uk/jlpt/jlpt3/kanji/',
    'http://www.tanos.co.uk/jlpt/jlpt2/kanji/',
    'http://www.tanos.co.uk/jlpt/jlpt1/kanji/'
]

kanji = []

i = 5
for URL in JPLT_URL:
    kanji.append({
        "N"+str(i): getKanji(URL)
    })
    i -= 1

json.dump(kanji, open('kanji.json', 'w'))
