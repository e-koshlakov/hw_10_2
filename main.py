# Модуль 10 - 2 Упаковка/Распаковка, данных, json

# Задание 1
# Реализовать класс «Автомобиль» у которого будет минимум 3 атрибута и 2 метода, добавьте возможность упаковки и
# распаковки данных с использованием json и pickle, для json метод упаковки на ваш выбор.
import json
import pickle


class Pickler:
    @staticmethod
    def pickle_data(data):
        return pickle.dumps(data)

    @staticmethod
    def unpickle_data(data):
        return pickle.loads(data)


class Car:
    """Класс Автомобиль. 3 атрибута: модель, цвет, год выпуска. 2 метода: Ехать, Стоять"""

    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year
        self.car_dict = {self.model, self.color, self.year}
        self.json_encoder = MyCarEncoder
        self.pickler = Pickler

    def __str__(self):
        return f"Car: {self.model} {self.color} {self.year}"

    def drive(self):
        return f"{self.model} едет"

    def stop(self):
        return f"{self.model} стоит"

    def to_json(self):
        return json.dumps(self, cls=self.json_encoder, ensure_ascii=False, indent=2)

    @staticmethod
    def from_json(str_json):
        return json.loads(str_json)

    def pickle(self):
        return pickle.dumps(self.car_dict)

    def unpickle(self, data):
        self.car_dict = pickle.loads(data)
        return self.car_dict


class MyCarEncoder(json.JSONEncoder):
    def default(self, o):
        return {
            "model": o.model,
            "color": o.color,
            "year": o.year,
        }


my_car = Car("BMW", "Black", 2021)
print(f' Экземпляр класса Car: {my_car.__dict__}')

json_to_s = my_car.to_json()
print(f'Упакованный объект: {json_to_s}')

s_to_json = my_car.from_json(json_to_s)
print(f'Распакованный объект:', s_to_json)

pickled = my_car.pickle()
print(f'Замаринованный объект: {pickled}')
unpickled = my_car.unpickle(pickled)
print(f'Размаринованный объект:', unpickled)
print()


# Задание 2
# Реализовать класс «Книга» у которого будет минимум 3 атрибута и 2 метода добавьте возможность упаковки и распаковки
# данных с использованием json и pickle, для json метод упаковки через Encoder.

class Book:
    """ Класс Книга. 3 атрибута: название, автор, год выпуска. 2 метода: Читать, Закрыть """

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.book_dict = {self.title, self.author, self.year}
        self.json_encoder = MyBookEncoder
        self.pickler = Pickler

    def __str__(self):
        return f"Книга: {self.title} {self.author} {self.year}"

    def read(self):
        return f"{self.title} читается"

    def close(self):
        return f"{self.title}  закрыта"

    def to_json(self):
        return json.dumps(self, cls=self.json_encoder, ensure_ascii=False, indent=2)

    @staticmethod
    def from_json(str_json):
        return json.loads(str_json)

    def pickle(self):
        return pickle.dumps(self.book_dict)

    def unpickle(self, data):
        self.book_dict = pickle.loads(data)
        return self.book_dict


class MyBookEncoder(json.JSONEncoder):
    def default(self, o):
        return {
            "title": o.title,
            "author": o.author,
            "year": o.year,
        }


my_book = Book("Три мушкетера", "Александр Дюма", 1844)
print(f' Экземпляр класса Книга: {my_book.__dict__}')
my_book_json = my_book.to_json()
print(f'Упакованный объект: {my_book_json}')
my_book_from_json = my_book.from_json(my_book_json)
print(f'Распакованный объект:', my_book_from_json)
my_book_pickle = my_book.pickle()
print(f'Замаринованный объект: {my_book_pickle}')
my_book_unpickle = my_book.unpickle(my_book_pickle)
print(f'Размаринованный объект:', my_book_unpickle)
print()

# Задание 3
# Реализовать класс «Стадион» у которого будет минимум
# 3 атрибута и 2 метода добавьте возможность упаковки и распаковки данных с использованием json и pickle, для json метод
# упаковки через Adapter.


class Stadium:
    """ Класс Стадион. 3 атрибута: название, вместимость, город. 2 метода: Играть, Закрыть """

    def __init__(self, name, capacity, city):
        self.name = name
        self.capacity = capacity
        self.city = city
        self.stadium_dict = {self.name, self.capacity, self.city}
        self.json_adapter = JSONDataAdapter
        self.pickler = Pickler

    def __str__(self):
        return f"Стадион: {self.name} {self.capacity} {self.city}"

    def play(self):
        return f"{self.name} идет игра"

    def close(self):
        return f"{self.name} закрыт"

    def to_json(self):
        return self.json_adapter.to_json(self)

    @staticmethod
    def from_json(str_json):
        return JSONDataAdapter.from_json(str_json)

    def pickle(self):
        return pickle.dumps(self.stadium_dict)

    def unpickle(self, data):
        self.stadium_dict = pickle.loads(data)
        return self.stadium_dict


class JSONDataAdapter:
    @staticmethod
    def to_json(obj):
        if isinstance(obj, Stadium):
            return json.dumps({
                "name": obj.name,
                "capacity": obj.capacity,
                "city": obj.city
            }, ensure_ascii=False)

    @staticmethod
    def from_json(obj_json_str):
        obj_python_dict = json.loads(obj_json_str)
        try:
            return Stadium(obj_python_dict['name'], obj_python_dict['capacity'], obj_python_dict['city'])
        except KeyError:
            print("Неверная структура!")


my_stadium = Stadium("Лужники", 81000, "Москва")
print(f' Экземпляр класса Стадион: {my_stadium.__dict__}')
my_stadium_json = my_stadium.to_json()
print(f'Упакованный объект: {my_stadium_json}')
my_stadium_from_json = my_stadium.from_json(my_stadium_json)
print(f'Распакованный объект:', my_stadium_from_json)
my_stadium_pickle = my_stadium.pickle()
print(f'Замаринованный объект: {my_stadium_pickle}')
my_stadium_unpickle = my_stadium.unpickle(my_stadium_pickle)
print(f'Размаринованный объект:', my_stadium_unpickle)
