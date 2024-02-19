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