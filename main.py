import requests
from bs4 import BeautifulSoup

web = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(web.text, "html.parser")

titles_list = []

titles = soup.find_all("h3", class_="title")

for i in titles:
    titles_list.append(i.getText())

titles_list = titles_list[::-1]

with open("Movies.txt",'w') as file:
    for i in titles_list:
        file.write(i +"\n")


