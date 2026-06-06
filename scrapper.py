from bs4 import BeautifulSoup
import requests

source=requests.get("https://indianexpress.com/").text

soup=BeautifulSoup(source,"lxml")

headline=[]

for match in soup.find_all("h2", class_="topblockNews__sidebarTitle"):
    headline.append(match.get_text(strip=True))
for match in soup.find_all("h3",class_=["o-express-premium__title","o-commonTopnews__txt mts-3","o-latest-news__title"]):
    headline.append(match.get_text(strip=True))
for match in soup.find_all("h4",class_="o-commonList__txt"):
    headline.append(match.get_text(strip=True))

headline=list(set(headline))

with open("headlines.txt","w",encoding="utf-8") as head_file:

    for i in headline:
        head_file.write(i+"\n")

