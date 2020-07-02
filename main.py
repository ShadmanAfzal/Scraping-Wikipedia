from bs4 import BeautifulSoup
import requests

movies = []
date = input("Enter the Year: ")
print("Finding...")
body = requests.get(f"https://en.wikipedia.org/wiki/List_of_American_films_of_{date}")
soup = BeautifulSoup(body.content, 'html.parser')
table = soup.find_all('table')
for x in range(2, 6):
    for i in table[x].find_all('td'):
        for j in i.find_all('i'):
            for k in j.find_all('a'):
                movies.append(k.get_text())
with open(f'movies_list_{date}.txt', 'w') as file:
    file.write(f"Movies of {date}:\n\n")
    count = 0
    for i in movies:
        count += 1
        file.write(f'{count}. {i} \n')
    print("Done...")
    print("Data has been store in " + f"movies_list_{date}.txt")
