import requests
import googletrans
from bs4 import BeautifulSoup
from pprint import pprint
# sahifa = "https://kun.uz/news/main"
# r = requests.get(sahifa)
# pprint(r.text)


# url = "https://api.adviceslip.com/advice"
# r = requests.get(url)
# advice = r.json()['slip']['advice']
# print(advice)

# translator = googletrans.Translator()
# tarjima = translator.translate(advice, dest='uz')
# print(tarjima.text)







sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
news = soup.find_all(class_="news-title")
print(news[0].text)