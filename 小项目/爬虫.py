import requests
>>> from bs4 import BeautifulSoup

>>> url = 'https://www.bilibili.com/anime/index/#season_version=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&pub_date=-1&style_id=-1&order=3&st=1&sort=0&page=1'
>>> res = requests.get(url)
>>> res.encoding = 'UTF-8'
>>> soup = BeautifulSoup(res.text, 'html.parser')
>>> for news in soup.select('.bangumi-tittle'):
	h2 = news.select('h2')
	if len(h2) > 0:
		title = h2[0].text
		print(title)