import os
from config import Manager
from comands import *

while True:
    print("\nТекущая директория:", file_manager.curr_dir)
    command = input("Введите команду (Введите 'help', чтобы увидеть все команды): ").strip()
    if command in commands:
        if command == 'exit':
            print("Выход из файлового менеджера")
            break
        elif command == 'help':
            file_manager.help()
        elif command == 'to_root_dir':
            file_manager.to_root_dir()
        else:
            args = input("Введите аргумент(ы через пробел): ").strip()
            commands[command](args)
    else:
        print("Несуществующая команда. Введите 'help', чтобы увидеть все команды")
