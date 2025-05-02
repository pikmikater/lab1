tasks = {
    "Прибрати кімнату": "очікує",
    "Зробити домашнє": "в процесі",
    "Погуляти з собакою": "виконано"
}

def add_task(name, status):
    tasks[name] = status

def delete_task(name):
    if name in tasks:
        del tasks[name]

def change_status(name, new_status):
    if name in tasks:
        tasks[name] = new_status

add_task("Купити продукти", "очікує")
change_status("Зробити домашнє", "виконано")
delete_task("Погуляти з собакою")

print("Усі задачі:", tasks)

waiting_tasks = []
for name, status in tasks.items():
    if status == "очікує":
        waiting_tasks.append(name)

print("Задачі зі статусом 'очікує':", waiting_tasks)
