import hashlib

users = {
    "user1": {
        "password": hashlib.md5("1234".encode()).hexdigest(),
        "name": "Іван Іванов"
    },
    "user2": {
        "password": hashlib.md5("abcd".encode()).hexdigest(),
        "name": "Олена Петрівна"
    }
}

def login():
    login_name = input("Введіть логін: ")
    password_input = input("Введіть пароль: ")
    password_hash = hashlib.md5(password_input.encode()).hexdigest()

    if login_name in users:
        if users[login_name]["password"] == password_hash:
            print("Вхід успішний! Привіт,", users[login_name]["name"])
        else:
            print("Невірний пароль")
    else:
        print("Користувача не знайдено")
      
login()
