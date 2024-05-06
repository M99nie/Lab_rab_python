from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests
def parse():
    url = 'https://auto.drom.ru/'  # передаем необходимы URL адрес
    page = requests.get(url)  # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code)  # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser")  # передаем страницу в bs4

    block = soup.findAll('a', class_='css-4zflqt e1huvdhj1')  # находим  контейнер с нужным классом
    file = open("cars.txt", 'a')
    for car in block:  # проходим циклом по содержимому контейнера
        name = car.find('div', class_='css-16kqa8y e3f4v4l2')
        nameCar = name.text
        print(nameCar)
        price = car.find('div', class_='css-1dv8s3l eyvqki91')
        priceCar = str(price.text)
        print(priceCar)
        file.write(nameCar+'\n')
        file.write(priceCar+ "\n")

    file.close()

parse()