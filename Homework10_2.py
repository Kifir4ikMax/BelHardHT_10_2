"""Задание (Лучше прогнать через PyCharm)

1. Создать файл json
2. Формат данных в файле
{
“id”: int,
“name”: str,
“age”: int,
“interests”: list, не обязательное поле, может быть null
“salary”: float
}
3. Создать минимум 5 объектов(вручную)
4. Написать pydantic модели
● Для добавления объекта(все поля)
● Для получения всех объектов(только id и name)
● Для получения определенного объекта(все поля)
5. Написать 3 метода(функции)
● Добавление объекта в файл
● Получения всех объектов
● Получение определенного объекта

"""


#Импортируем модули JSON, Typing и Pydantic
import json
from pydantic import BaseModel
from typing import List, Optional


#Создаём Pydantic модели (базовый для проверки id и имени)
class UserBase(BaseModel):
    id: int
    name: str


#Общий для создания объектов
class UserCreate(UserBase):
    age: int
    interests: Optional[List[str]] = []
    salary: float


#Наследуем классы для последующих методов
class UserGetName(UserBase):
    pass


class UserGetInfo(UserCreate):
    pass


#Метод для проверки данных через Pydantic класс
def add_user(id: int, name: str, age: int, interests: Optional[List[str]], salary: float):
    try:
        return dict(UserCreate(id=id, name=name, age=age, interests=interests, salary=salary))
    except Exception as exc:
        raise exc


#Метод проверки и вывода только ID и name
def get_users_name(id: int, name: str, age: int, interests: Optional[List[str]], salary: float):
    return UserGetName(id=id, name=name)


#Метод проверки и вывода всей информации об объекте
def get_user_info(id: int, name: str, age: int, interests: Optional[List[str]], salary: float):
    return UserGetInfo(id=id, name=name, age=age, interests=interests, salary=salary)


#Создаём объекты
data_1 = {
    "id": 100001,
    "name": "Alex",
    "age": 25,
    "interests": ["Camping", "Football"],
    "salary": 1.5
}


data_2 = {
    "id": 100002,
    "name": "Phill",
    "age": 30,
    "interests": ["Racing", "Fishing"],
    "salary": 2.5
}


data_3 = {
    "id": 100003,
    "name": "George",
    "age": 31,
    "interests": None,
    "salary": 3.6
}


data_4 = {
    "id": 100004,
    "name": "Max",
    "age": 32,
    "interests": ["Camping", "Racing"],
    "salary": 5.5
}


data_5 = {
    "id": 100005,
    "name": "Tatiana",
    "age": 32,
    "interests": ["Shopping", "Dancing"],
    "salary": 0.5
}


#Заливаем объекты в JSON файл через проверку методом add_user
with open("lesson_10.json", "w") as file:
    json.dump(
        (add_user(**data_1),
         add_user(**data_2),
         add_user(**data_3),
         add_user(**data_4),
         add_user(**data_5)
         ), file, indent=4, ensure_ascii=False
    )


#Теперь можем прочитать JSON и выведем только ID и name методом get_users_name
with open("lesson_10.json", "r") as file:
    loaded_data = json.load(file)
    for data in loaded_data:
        print(get_users_name(**data))


#Теперь можно вывести данные по конкретному объекту (Опционально добавил фильтр по имени)
with open("lesson_10.json", "r") as file:
    loaded_data = json.load(file)
choice = str(input("Enter name: "))
for data in loaded_data:
    if choice in data['name']:
        print(get_user_info(**data))
