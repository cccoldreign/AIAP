# Алгоритмические языки программирования 


```python


```

# Практика №1

1. Сгенерировать, используя модуль псевдослучайных чисел `random`, или ввести с клавиатуры список целых чисел. Вывести в консоль, затем перевернуть его и снова вывести в консоль.

Создаю список вывожу его и после вывожу реверсивный список

```python

list = np.random.randint(-10, 10, 7).tolist()

print(list)

list.reverse()

print(list)

```

2. Сгенерировать, используя модуль псевдослучайных чисел `random`, или ввести с клавиатуры два списка целых чисел. Вывести их в консоль. Создать новый пустой список. Добавить в него все четные (по индексу) элементы первого списка и все нечетные (по индексу) элементы второго списка. Вывести третий список в консоль.

Создаю два списка и заполняю третий из четных первого и нечетных второго

```python

firstList = np.random.randint(-10, 10, 7).tolist()
secondList = np.random.randint(-10, 10, 7).tolist()
thirdList = []

print("", firstList,'\n', secondList)

for i in range(len(firstList)):
    if i % 2 == 0:
        thirdList.append(firstList[i])
    else:
        thirdList.append(secondList[i])

print("", thirdList)

```


3. Сгенерировать, используя модуль псевдослучайных чисел `random`, или ввести с клавиатуры список произвольных элементов (целые числа, числа с плавающей точкой, строки). Вывести в консоль. Убрать из него все дубликаты через приведение типов. Вывести в консоль.

Создаю список из трех произвольных типов и убираю из него дубликаты циклом 

```python

list = [12.3, "1", 1, "12.3", 13, 13, 13]

for i in range(len(list)):
    list[i] = str(list[i])

list = sorted(set(list))

print(list)

```

4. Сгенерировать, используя модуль псевдослучайных чисел `random`, или ввести с клавиатуры словарь, где ключом является строка, значением — целое число или число с плавающей точкой. Вывести в консоль. Для всех уникальных значений создать кортеж, где первым элементом будет значение, вторым — список связанных с ним ключей. Собрать эти кортежи в список, вывести его в консоль.

Создаю пустой список и два словаря, где создаю для уникальных значений второй словарь и вывожу его

```python

tupleList = []
dict1 = {
    '[1]': 1,
    '[2]': 2,
    '(2)': 2,
    '[3]': 3,
    '[4]': 4.2,
    '[5]': 5,
    '/5/': 5
}
dict2 = {}

for key, value in dict1.items():
    if value in dict2:
        dict2[value].append(key)
    else:
        dict2[value] = [key]
for key, value in dict2.items():
    tupleList.append((key, value))

for i in dict1.items():
    print(i)
print('\n')
for i in tupleList:
    print(i)

```

5. Сгенерировать, используя модуль псевдослучайных чисел `random`, или ввести с клавиатуры два словаря, где ключом является строка, значением — целое число или число с плавающей точкой. Вывести в консоль. Найти пересечения множеств значений словарей. Создать новый словарь, содержащий только те пары ключ-значение, значения из которых входит в пересечение. Вывести в консоль.

Создаю два словаря и вывожу уникальные значения пересечения двух словарей

```python

dict1 = {
    '[1]': 1,
    '[2]': 2,
    '[3]': 3,
    '[4]': 4.2
}
dict2 = {
    '[6]': 6,
    '[2]': 2,
    '[5]': 5,
    '[4]': 4.2
}

print(set(dict1.items()).intersection(set(dict2.items())))

```

# Практика №2

1. Скопировать из Википедии данные по кодам аэропортов (например, отсюда [https://en.wikipedia.org/wiki/List_of_airports_by_IATA_airport_code:\_P](https://en.wikipedia.org/wiki/List_of_airports_by_IATA_airport_code:_P)). Сохранить их в JSON-подобном формате с использованием словарей. Реализовать функцию получения кода по названию аэропорта. Реализовать и русское, и английское название. Предусмотреть, что аэропорта может не существовать.

В data.json сохранены индексы аэропортов и их названия. Циклом проверяю соответсиве введенного ключа с data.json.

```python
import json

data = '/Users/coldreign/code/Study/AIAP/practice/practice2/data.json'

with open(data, 'r') as file:
    date = json.load(file)

while True:
  search = input()

  for key,value in date.items():
    if value == search:
      print('key:',key)
      break
    else:
      print('ничего не найдено')
      break
```

2. Реализовать в консоли таск-трекер. Данные хранить в словаре во время работы программы, выгружать список задач в JSON-файл, при запуске загружать файл (используя модуль `json`). Реализовать возможность ввода произвольной строки с описанием задачи, возможность отметки задания выполненным, возможность ввода произвольных категорий. *Бонус: поиск по задачам; вывод всех задач в категории.*

В виде вечного цикла вывод описания таск-трекера и при вводе он проверяет есть ли такая функция исходя из цифры, которая относится к каждой функции

```python
import json

task = {}
data = '/Users/coldreign/code/Study/AIAP/practice/practice2/task.json'

def add_task():
    with open(data, 'r') as file:
        task = json.load(file)

    name = input("Название задачи: ")
    task[name] = '[ ]'

    with open(data, 'w') as file:
        json.dump(task, file, indent=4)

def view_task():
    with open(data, 'r') as file:
        d = json.load(file)
    print(json.dumps(d, indent=4))

def delete_task():
    with open(data, 'r') as file:
        d = json.load(file)

    name = input("Введите название задачи для удаления: ")

    if name in d:
        d.pop(f'{name}')

    with open(data, 'w') as file:
        json.dump(d, file, indent=4)

def change():
    with open(data, 'r') as file:
        d = json.load(file)
    
    name = input("Введите название выполненной задачи: ")
    
    if name in d:
        new_value = '[X]'
        d[name] = new_value

    with open(data, 'w') as file:
        json.dump(d, file, indent=4)

print("Таск-трекер:")
print("1. Добавить задачу")
print("2. Посмотреть задачи")
print("3. Удалить задачу")
print("4. Сменить прогресс")
print("5. Выйти")

while True:

    choice = input("Выберите действие: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        change()
    elif choice == "5":
        print("Выход из программы.")
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")
```
3. Реализовать в консоли трекер бюджета. Данные хранить в словаре во время работы программы, выгружать список задач в JSON-файл, при запуске загружать файл (используя модуль `json`). Реализовать возможность ввода произвольной строки с описанием операции и суммой расхода/дохода, возможность ввода произвольных категорий. *Бонус: аналитика трат/доходов по категориям (например, сколько потратили в сумме за заказ еды); установка лимитов на категории.*

# Лабораторная работа №1: Особенности ООП в Python

```python


```
1. Реализовать структуру данных «очередь» (первый пришел, первый ушел) с помощью класса с возможностью просмотра, добавления и удаления элементов.

FIFO first input first output. Класс имеет методы ввода и вывода когда входит то он удаляет нулевой элемент внутреннего списка класса.

```python

class FIFO:
    def __init__(self):
        self.queue = []
    def input(self, item):
        self.queue.append(item)
        self.queue.pop(0)
    def output(self):
        return self.queue

fifo = FIFO()
fifo.input("kek")
print(fifo.output())
fifo.input("kek2")
print(fifo.output())

```


2. Реализовать структуру данных «стек» (последний пришел, первый ушел) с помощью класса с возможностью просмотра, добавления и удаления элементов.

LIFO last in firt output. Класс LIFO тоже имеет внутренний список и методы ввода и вывода. Если список не пустой то он удалаяет нулевой элемент

```python

class LIFO:
    def __init__(self):
        self.queue = []
    def input(self, item):
        self.queue.append(item)
        if len(self.queue) > 1:
            self.queue.pop(0)
        else:
            return None
    def output(self):
        return self.queue

lifo = LIFO()
lifo.input("kek")
print(lifo.output())
lifo.input("kek2")
print(lifo.__repr__())

```

3. Реализовать иерархию классов, описывающих разные виды объектов одного типа (например, сервоприводов синхронный/асинхронный/линейный и т.п.). Реализовать минимум 3 уровня иерархии. Реализовать возможность задания характеристик (например, для двигателя это угол поворота, скорость вращения, ускорение и т.п.). Реализовать строковое представление классов «магическими» методами `__str__()` и `__repr__()`, быть готовым пояснить различия этих методов. Перегрузить условные операторы (см. магические методы `__eq__()`, `__ne__()`, `__lt__()`, `__gt__()`, `__le__()`, `__ge__()`) для реализации возможности сравнения экземпляров класса.

Основной класс кошки имеет четыре переменные: порода, цвет, ноги, уши. Имеет вывод __str__ для красивого вывода и __repr__ чтобы можно было другому человеку взять как выглядит существующий класс. Так же класс cat имеет перегрузку операторов сравнения. После определения наследующих классов идет пример использования перегрузок.

```python

class Cat:
    def __init__(self, breed: str, color: str, legs=4, ears=2) -> None:
        self.breed = breed
        self.color = color
        self.legs = legs
        self.ears = ears

    def __str__(self):
        return f"{self.color} {self.breed} cat with {self.legs} legs and {self.ears} ears."

    def __repr__(self):
        return f"Cat(name='{self.breed}', color='{self.color}', legs={self.legs}, ears={self.ears})"
    
    def __eq__(self, other):
        if isinstance(other, Cat):
            return self.breed == other.breed
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

class DomesticCat(Cat):
    def __init__(self, breed, color, name: str, legs=4, ears=2) -> None:
        super().__init__(breed, color, legs, ears)
        self.name = name

class WildCat(Cat):
    def __init__(self, breed, color, location: str, legs=4, ears=2) -> None:
        super().__init__(breed, color, legs, ears)
        self.location = location
    
domestic_cat = DomesticCat(breed="Siamese", color="white", name="Snowball")
wild_cat = WildCat(breed="Siamese", color="brown", location="North America")

print(domestic_cat.__str__())
print(wild_cat.__repr__())
print(domestic_cat == wild_cat)

```

4. Реализовать упрощенную модель некоего объекта (например, шестизвенного манипулятора с сервоприводами) при помощи иерархии классов. Реализовать функции объекта (например, перемещение манипулятора в пространстве) через перегрузку арифметических операторов (`__add__()` и т.д.).
5. Расчет расстояния между точками на сфере по их широте и долготе (взять любые GPS-координаты) при помощи иерархии классов: как минимум, Точка и Сфера (к ней относятся Точки). https://en.wikipedia.org/wiki/Haversine_formula

Классы Point, Sphere представляют собой точку и сферу. В методе сферы есть возможность добавления точки в сферу для дальнейшего применения расчета дистанции между точек

```python
class Point:
    def __init__(self, latitude, longitude) -> None:
        self.latitude = math.radians(latitude)
        self.longitude = math.radians(longitude)

class Sphere:
    def __init__(self, radius) -> None:
        self.radius = radius
        self.points = []

    def addPoint(self, point) -> None:
        self.points.append(point)

    def calcDist(self, point1, point2) -> float:
        dLatitude = point2.latitude - point1.latitude
        dLongitude = point2.longitude - point1.longitude
        a = math.sin(dLatitude / 2)**2 +  math.cos(point1.latitude) * math.cos(point2.latitude) * math.sin(dLongitude / 2)**2
        c = 2 * math.asin(math.sqrt(a))
        return self.radius * c

earth = Sphere(6371)

perm = Point(58.064211, 56.363566)
spb = Point(59.93861, 30.31411)
zero = Point(0.0, 0.0)
negative = Point(-20.0, -20.0)

earth.addPoint(perm)
earth.addPoint(spb)
earth.addPoint(zero)
earth.addPoint(negative)

print(earth.calcDist(perm, spb))
print(earth.calcDist(perm, zero))
print(earth.calcDist(spb, negative))
```


# Практика №3
На основе классов из лабораторной работы №2 (основы ООП) создать набор классов данных, добившись паритета по функциональности — т.е. для, например, Сферы и Точки должен быть также доступен расчет расстояния.

Теперь классы сферы и точки представленны дата классами.

```python

    @dataclass
class Point:
        latitude: float 
        longitude: float

@dataclass
class Sphere:
    radius: int
    points: list = field(default_factory=list)

        
    def addPoint(self, point):
        self.points.append(point)

    def calcDist(self, point1, point2):
        point1.latitude = math.radians(point1.latitude)
        point2.latitude = math.radians(point2.latitude)
        point1.longitude = math.radians(point1.longitude)
        point2.longitude = math.radians(point2.longitude)
        dLatitude = point2.latitude - point1.latitude
        dLongitude = point2.longitude - point1.longitude
        a = math.sin(dLatitude / 2)**2 +  math.cos(point1.latitude) * math.cos(point2.latitude) * math.sin(dLongitude / 2)**2
        c = 2 * math.asin(math.sqrt(a))
        return self.radius * c

earth = Sphere(6371)

perm = Point(58.064211, 56.363566)
spb = Point(59.93861, 30.31411)
zero = Point(0.0, 0.0)
negative = Point(-20.0, -20.0)

earth.addPoint(perm)
earth.addPoint(spb)
earth.addPoint(zero)
earth.addPoint(negative)

print(earth.calcDist(perm, spb))
print(earth.calcDist(perm, zero))
print(earth.calcDist(spb, negative))

```

# Лабораторная работа №3: Элементы функционального программирования в Python

## Блок 1
```python

```
1. Загрузите список стран из `countries.json`

Открываю файл на чтние 'r' и загружаю его в data

```python
with open('/Users/coldreign/code/Study/AIAP/lab/countries.json', 'r') as countries:
    data = json.load(countries)
```

2. С помощью `map()` создайте новый список, изменив сделав название каждой страны прописным в списке стран.

Вывожу список пройдясь по каждому его элементу лямбда функцией на снижение регистра. Наличие list обязательно иначе будет выведено место в памяти

```python
print(list(map(lambda x: x.lower(), data)))
```

3. С помощью `filter()`, чтобы отфильтровать страны, содержащие `'land'`.

Проходясь по элементам с fliter остаются только те где есть land 

```python
print(list(filter(lambda x: "land" in x, data)))
```

4. С помощью `filter()`, чтобы отфильтровать страны, содержащие ровно шесть символов.

Проходясь по элементам с fliter остаются только те где длина равна 6

```python
print(list(filter(lambda x: len(x) == 6, data)))

```

5. С помощью `filter()`, чтобы отфильтровать страны, содержащие шесть и более букв в списке стран.

```python
print(list(filter(lambda x: len(x) <= 6, data)))

```

6. С помощью `filter()` для отсеивания стран, начинающихся с буквы `'E'`.

С помощью startswith() возвращает только те элементы, которые начинаются на Е

```python
print(list(filter(lambda x: x.startswith('E'), data)))
```

7. С помощью `reduce()` объедините все страны и получите данное предложение на английском языке: Финляндия, Швеция, Дания, Норвегия и Исландия являются странами Северной Европы.

Применяет переданную функцию к каждому значению в списке и ко внутреннему накопителю результата

```python
NorthCountry = ['Финляндия', 'Швеция', 'Дания', 'Норвегия', 'Исландия']
print(reduce(lambda x,y: x + ", "+ y, NorthCountry) + " являются странами Северной Европы.")
```

8. Решите предыдущие задачи, объединив две или более функций высшего порядка методов

```python
print(list(filter(lambda x: "land" in x, list(map(lambda x: x.lower(), data)))))
```

9. Используя сначала каррирование, а затем замыкания, объявите функцию `categorize_countries()`, которая возвращает список стран с некоторым общим шаблоном (например, `'land', 'ia', 'island', 'stan'`), который можно менять.

Переменная categorize_countries принимает образец, который отвечает за общий шаблон, и применияет filter с ним к каждому элементу из списка стран

```python
def categorize_countries(sample):
    def print_countries(countries):
        return list(filter(lambda x: sample in x, countries))
    return print_countries

print(categorize_countries("ia")(data))
```

10. Используя файл `countries-data.json`, выполните приведенные ниже задания в функциональной парадигме:
    1. Отсортировать страны:
        1. по названию, 
        2. по столице, 
        3. по численности населения
    2. Выявить произвольное число (начать с 10) наиболее распространенных языков и где их используют.
    3. Выявить произвольное число (начать с 10) наиболее населенных стран.

```python
with open("countries-data.json", "r", encoding="utf-8") as file:
    countries_data = json.load(file)

sortedName = sorted(countries_data, key=lambda x: x['name'])
sortedCapital = sorted(countries_data, key=lambda x: x['capital'])
sortedPopulation = sorted(countries_data, key=lambda x: x['population'])

all_languages = [language for country in countries_data for language in country['languages']]
language_count = [(language, all_languages.count(language)) for language in set(all_languages)]
topLanguages = sorted(language_count, key=lambda x: x[1], reverse=True)[:10]

sorted_population_desc = sorted(countries_data, key=lambda x: x['population'], reverse=True)
top_populated_countries = sorted_population_desc[:10]
```

## Блок 2

1. Сгенерировать список из 50 числовых элементов. Используя списковые включения, вычислить 4, 5 и 6 степени каждого элемента.
```python
numbers = list(range(1, 51))
power = [(x**4, x**5, x**6) for x in numbers]
```
2. Сгенерировать матрицу в виде списка списков (например, `[ [1, 2], [3, 4], [5, 6], [7, 8], [1, 2], [3, 4], [5, 6], [7,8] ]`). Используя списковые включения, транспонировать матрицу ([https://ru.wikipedia.org/wiki/Транспонированная_матрица)](https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D0%BF%D0%BE%D0%BD%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D0%B0%D1%8F_%D0%BC%D0%B0%D1%82%D1%80%D0%B8%D1%86%D0%B0))

двумя циклами создается так же два списка опираясь на размер внутреннего списка.

```python
matrix = [[1, 2], [3, 4], [5, 6], [7, 8], [1, 2], [3, 4], [5, 6], [7, 8]]
transposed_matrix = [[x[i] for x in matrix] for i in range(len(matrix[0]))]
```
3. Взять полный диапазон числовых элементов от -9999 до 9999. Используя анонимную функцию и функцию `filter()`, вывести список, содержащий все элементы, которые без остатка делятся на 36.

```python
numbers = list(range(-9999, 9999))
print(list(filter(lambda x: x % 36 == 0, numbers)))
```

4. Используя `map()` и анонимные функции (а также любые вспомогательные методы `str`), написать функцию редактирования заголовков в англоязычном стиле (`Каждое Слово Длиной Более 3 Букв Должно Быть с Большой Буквы`), принимающую на вход исходную строку, возвращающую отредактированную строку.

Функция принимает в себя строку и дальше разюивает ее по пробелу, потом проверяет каждый элемент на длину и при true снижает регистр, а join() соединяет обратно. filter__ имеет такую запись так как такое имя по сути уже используется.

```python
def edit_title(title):
    words = title.split()
    filter__ = map(lambda word: word.capitalize() if len(word) > 3 else word.lower(), words)
    result = ' '.join(filter__)
    return result

original_title = "каждое слово длиной БОЛЕЕ 3 букв должно БЫТЬ с БОЛЬШОЙ буквы"
edited_title = edit_title(original_title)
```

5. Используя иерархию классов из лаб. работы № 1, встроенные коллекции, анонимные функции и `reduce()`, вернуть максимальную длину, на которую может вытянуться шестизвенный манипулятор. Классы в иерархии можно расширять при необходимости.
6. Используя частичное выполнение функции, заменить указанную функцию с 4 аргументами на функцию с 1 аргументом так, чтобы результат был равен:
    1. 60
    2. 120
    3. 180

```python
def foo(a:int, b:int, c:int, d:int) -> int:
    return a*4 + b*3 + c*2 + d

par3 = partial(foo, 2, 4, 20)

print(par3(0))
print(par3(60))
print(par3(120))

```

7. Используя 2 генератора и `sum()`, вернуть сумму квадратов первых 10, 20, 30, 40 и 50 чисел Фибоначчи.
```python

fib = [0, 1]

def fibonacci(n):
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

def fibonacci_squared(n):
    fib = fibonacci(n)
    return (x**2 for x in fib)

print(sum(fibonacci_squared(10)), sum(fibonacci_squared(20)), sum(fibonacci_squared(30)),
      sum(fibonacci_squared(40)),sum(fibonacci_squared(50)))

```
8. Написать генератор, последовательно возвращающий **все** аэропорты из списка IATA. Каждый аэропорты должен быть выведен в виде словаря, где ключами являются параметры из списка на Википедии (например, заголовки колонок таблицы здесь [https://en.wikipedia.org/wiki/List_of_airports_by_IATA_airport_code:\_A)](https://en.wikipedia.org/wiki/List_of_airports_by_IATA_airport_code:_A)) значениями — данные самого аэропорта.

```python
def airports_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            data = eval(line)
            yield data

```
9. Используя генератор из п. 8, сохранить в текстовый файл список IATA-кодов аэропортов и их англоязычные названия, разделенные табуляцией (`\t`).

```python
file_path = "/Users/coldreign/code/Study/AIAP/lab/airport.txt"

for airport in airports_generator(file_path):
    print(airport)
```


# Лабораторная работа №4. Научные вычисления на Python

2. Загрузить данные в DataFrame при помощи библиотеки `pandas`. Проследить за корректными `dtypes (df.info())`

read_csv создает df из файла

```python
file_path = "/Users/coldreign/code/Study/AIAP/lab/weatherHistory.csv"
    data = pd.read_csv(file_path)
```

3. Построить регрессионную модель, которая принимает на вход сведения о температуре и влажности, выдает ощущаемую температуру. Для этого использовать класс `LinearRegression` из `Scikit-learn`. При обучении модели использовать `train_test_split` из `Scikit-learn`

Переменные x овечают за входные данные, а y за предположение/предсказание. 20 процентов данных отдается на оценку производительности. model = linear_model.LinearRegression() выбирается регрессионная модель. model.fit(x_train, y_train) обучение модели. y_pred = model.predict(x_test) модель предсказывает значение. mse = mean_squared_error(y_test, y_pred) сравнение прдесказанного значения и настоящим

```python
x = data[['Temperature (C)', 'Humidity', 'Wind Speed (km/h)']]
    y = data['Apparent Temperature (C)']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

    model = linear_model.LinearRegression()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    mse = mean_squared_error(y_test, y_pred)
```
4. Необходимо визуализировать данные по каждой паре параметров и линию регрессии при помощи диаграммы рассеяния. Использовать `seaborn` при построении диаграмм (например, [https://seaborn.pydata.org/generated/seaborn.pairplot.html)](https://seaborn.pydata.org/generated/seaborn.pairplot.html))

Создается копия входных данных, дальше заменяем столбик с ощутимой температурой на столбец с предказанными значения модели. pairplot диаграмма где в kind задается типа regression, и задается цвет линии регрессии.

```python
data_visual = x_test.copy()
    data_visual['Predicted Apparent Temperature (C)'] = y_pred
    sns.pairplot(data_visual, x_vars=['Temperature (C)', 'Humidity', 'Wind Speed (km/h)'], y_vars=['Predicted Apparent Temperature (C)'], kind='reg', plot_kws={'line_kws': {'color': 'black'}})
    plt.show()
```

6. Собрать веб-интерфейс: вывести визуализацию модели, организовать пользовательский интерфейс при помощи HTML-форм. Пользователь вводит температуру, сведения о влажности и иные параметры модели, получает ощущаемую температуру. Можно брать любой фреймворк, например, Flask.

Нужно создать новую папку где будут содержаться app.py и папка templates с index.html. Перменные mse и prediction передается из app.py. Картинка сохраняется в папку static. Трич числовых формы типа any чтобы можно было вводить float. И при значение Predict, которое подается при нажатии кнопки вычленяются перменные и проходят в модель, а на их онснове выдается предсказзанно значение.

```python
app = Flask(__name__)

@app.route('/')
def home():
    file_path = "/Users/coldreign/code/Study/AIAP/lab/weatherHistory.csv"
    data = pd.read_csv(file_path)

    x = data[['Temperature (C)', 'Humidity', 'Wind Speed (km/h)']]
    y = data['Apparent Temperature (C)']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

    model = linear_model.LinearRegression()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    mse = mean_squared_error(y_test, y_pred)
    
    data_visual = x_test.copy()
    data_visual['Predicted Apparent Temperature (C)'] = y_pred

    plt.switch_backend('agg')
    sns.pairplot(data_visual, x_vars=['Temperature (C)', 'Humidity', 'Wind Speed (km/h)'], y_vars=['Predicted Apparent Temperature (C)'], kind='reg', plot_kws={'line_kws': {'color': 'black'}})
    plt.savefig('static/output.png')

    return render_template('index.html', mse = mse)

@app.route('/predict', methods=['POST'])
def predict():
    
    file_path = "/Users/coldreign/code/Study/AIAP/lab/weatherHistory.csv"
    data = pd.read_csv(file_path)

    x = data[['Temperature (C)', 'Humidity', 'Wind Speed (km/h)']]
    y = data['Apparent Temperature (C)']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

    model = linear_model.LinearRegression()
    model.fit(x_train, y_train)
    
    temperature = float(request.form.get('temperature'))
    humidity = float(request.form.get('humidity'))
    windspeed = float(request.form.get('windspeed'))

    prediction = model.predict([[temperature, humidity, windspeed]])

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!DOCTYPE html>
<html>
<body>
    <h1>Mean squared error: {{ mse }}</h1>
    <img src="{{ url_for('static', filename='output.png') }}" alt="output image">
<h2>Predict Apparent Temperature</h2>

<form action="/predict" method="post">
    <label for="temperature">Temperature (C):</label><br>
    <input type="number" step="any" id="temperature" name="temperature" value=""><br>
    <label for="humidity">Humidity:</label><br>
    <input type="number" step="any" id="humidity" name="humidity" value=""><br>
    <label for="windspeed">Wind Speed (km/h):</label><br>
    <input type="number" step="any" id="windspeed" name="windspeed" value=""><br><br>
    <input type="submit" value="Predict">
</form> 

{% if prediction %}
  <h2>Predicted Apparent Temperature: {{ prediction }}</h2>
{% endif %}

</body>
</html>

```


# Лабораторная работа №5: Blender

Все картинки в папке lab

     ```python
     A
        for i in range(-50, 51):
            bpy.ops.mesh.primitive_cube_add(size=0.1, location=(0, 0, i*.25))
            bpy.context.active_object.data.materials.append(mat)

            base = 15 - (i**2)*0.05
            
            bpy.ops.transform.resize(value=(base, base, 0.5))
            
            cubes.append(bpy.context.active_object)
        
    B
        for i in range(-55, 55):
            bpy.ops.mesh.primitive_cube_add(size=0.1, location=(0, 0, i*.25))
            bpy.context.active_object.data.materials.append(mat)

            base = 150 - (i**2)*0.05
            
            bpy.ops.transform.resize(value=(base, base, 0.5))
            
            cubes.append(bpy.context.active_object)
        
        
        
    C
        for i in range(0, 51):
            bpy.ops.mesh.primitive_cube_add(size=0.1, location=(0, 0, i*.25))
            bpy.context.active_object.data.materials.append(mat)
            base = i + ( i**2)*0.05
            bpy.ops.transform.resize(value=(base, base, 0.5))
            bpy.context.active_object.rotation_euler[2] = math.degrees(i*25)
            
            cubes.append(bpy.context.active_object)
        for cube in cubes:
            scene.frame_set(frame_num)
            cube.keyframe_insert(data_path="rotation_euler", index=-1)
            frame_num += 1
            scene.frame_set(frame_num)
            cube.rotation_euler[2] = 0
            cube.keyframe_insert(data_path="rotation_euler", index=-1)

```