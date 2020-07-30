import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.musicList200730

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200730', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

music_rank_200730 = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for music_info in music_rank_200730:
    rank = music_info.select_one('td.number').text[0:2].strip()
    title = music_info.select_one('a.title').text.strip()
    artist = music_info.select_one('a.artist').text

    db.musicList200730.insert_one({'rank': rank, 'title': title, 'artist': artist})
