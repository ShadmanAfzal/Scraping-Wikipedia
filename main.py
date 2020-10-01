import requests
from bs4 import BeautifulSoup


def scrape(year):
    movies = []
    date = year
    body = requests.get(f"https://en.wikipedia.org/wiki/List_of_American_films_of_{date}")
    soup = BeautifulSoup(body.content, 'html.parser')
    table = soup.find_all('table')
    for x in range(2, 6):
        for i in table[x].find_all('td'):
            for j in i.find_all('i'):
                for k in j.find_all('a'):
                    movies.append(k.get_text())
    return movies


def create_txt(year, movie):
    with open(f'movies_list_{year}.txt', 'w') as file:
        file.write(f"Movies of {year}:\n\n")
        count = 0
        for i in movie:
            count += 1
            file.write(f'{count}. {i} \n')
        print("Done...")
        print("Data has been store in the" + f"movies_list_{year}.txt")


if __name__ == '__main__':
    year = int(input("Please enter the year"))
    movies = scrape()
    choice = int(input("enter 1 to create txt file\n 2 for printing file\n 3 do nothing"))
    if choice == 1:
        create_txt(year, movies)
    elif choice == 2:
        print(movies)
    else:
        pass
