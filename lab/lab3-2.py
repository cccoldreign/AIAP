from functools import partial

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

    def calculate_jump(self):
        return self.legs*3

class DomesticCat(Cat):
    def __init__(self, breed, color, name: str, legs=4, ears=2) -> None:
        super().__init__(breed, color, legs, ears)
        self.name = name

class WildCat(Cat):
    def __init__(self, breed, color, location: str, legs=4, ears=2) -> None:
        super().__init__(breed, color, legs, ears)
        self.location = location

numbers = list(range(1, 51))
power = [(x**4, x**5, x**6) for x in numbers]
print(list(power))

matrix = [[1, 2], [3, 4], [5, 6], [7, 8], [1, 2], [3, 4], [5, 6], [7, 8]]
transposed_matrix = [[x[i] for x in matrix] for i in range(len(matrix[0]))]
print(transposed_matrix)

numbers = list(range(-9999, 9999))
print(list(filter(lambda x: x % 36 == 0, numbers)))

def edit_title(title):
    words = title.split()
    filter__ = map(lambda word: word.capitalize() if len(word) > 3 else word.lower(), words)
    result = ' '.join(filter__)
    return result

original_title = "каждое слово длиной БОЛЕЕ 3 букв должно БЫТЬ с БОЛЬШОЙ буквы"
edited_title = edit_title(original_title)
print(edited_title)

def foo(a:int, b:int, c:int, d:int) -> int:
    return a*4 + b*3 + c*2 + d

par3 = partial(foo, 2, 4, 20)

print(par3(0))
print(par3(60))
print(par3(120))

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

def airports_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            data = eval(line)
            yield data

file_path = "/Users/coldreign/code/Study/AIAP/lab/airport.txt"

for airport in airports_generator(file_path):
    print(airport)