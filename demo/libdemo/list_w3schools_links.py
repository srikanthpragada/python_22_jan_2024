from bs4 import BeautifulSoup
import requests

WEBSITE = "https://www.w3schools.com"
resp = requests.get(WEBSITE)  # take HTML from home page
bs = BeautifulSoup(resp.text, 'html.parser')
links = bs.find_all("a")  # find all <a> elements


urls = set()
for link in links:
    href = link['href']
    if href.startswith("javascript:void"):
        continue

    if not href.startswith("http"):
        href = WEBSITE + href

    urls.add(href)

print("Links count : ", len(urls))
for url in urls:
    print(url)
