import os
import shutil

class Manager:
    def __init__(self, working_dir):
        # Инициализация рабочей директории
        self.working_dir = working_dir
        self.curr_dir = working_dir

    def help(self):
        print("Список доступных команд:")
        print("  create_dir  <название_директории>: Создать новую папку")
        print("  delete_dir  <название_директории>: Удалить существующую папку")
        print("  change_dir  <название_директории>: Перейти в папку")
        print("  create_file <название_файла>: Создать файл")
        print("  read_file   <название_файла>: Отобразить содержимое файла")
        print("  write_file  <название_файла>: Записать в файл")
        print("  delete_file <название_файла>: Удалить файл")
        print("  copy_file   <исходный_файл>, <целевой_файл>: Копировать файл")
        print("  move_file   <исходный_файл>, <целевая_директория>: Переместить файл")
        print("  rename_file <текущее_название_файла>, <новое_название_файла>: Переименовать файл")
        print("  to_root_dir: Перейти в корень рабочего пространства")
        print("  exit: Выйти из менеджера файлов")

    def create_dir(self, new_dir):
        # Создание новой директории
        new_dir_path = os.path.join(self.curr_dir, new_dir)
        if os.path.exists(new_dir_path):
            print(f"Директория '{new_dir}' уже существует в текущей директории")
        else:
            os.makedirs(new_dir_path)
            print(f"Директория '{new_dir}' успешно создана")

    def to_root_dir(self):
        # Возвращение в корень
        self.curr_dir = self.working_dir
        print(f"Текущая директория изменена на '{self.curr_dir}'.")

    def delete_dir(self, dir_name):
        # Удаление директории
        dir_path = os.path.join(self.curr_dir, dir_name)
        if os.path.exists(dir_path):
            os.rmdir(dir_path)
            print(f"Директория '{dir_name}' успешно удалена")
        else:
            print(f"Директория '{dir_name}' не найдена в текущей директории")

    def change_dir(self, dir_name):
        # Изменение текущей рабочей директории
        new_dir = os.path.join(self.curr_dir, dir_name)
        if os.path.exists(new_dir):
            if os.path.abspath(new_dir).startswith(os.path.abspath(self.working_dir)):
                self.curr_dir = new_dir
                print(f"Текущая директория изменена на '{self.curr_dir}'.")
            else:
                print(f"Доступ запрещен: '{new_dir}' находится за пределами рабочей директории")
        else:
            print(f"Директория '{dir_name}' не найдена в '{self.curr_dir}'.")

    def create_file(self, file):
        # Создание нового файла
        with open(os.path.join(self.curr_dir, file), 'w') as f:
            print(f"Файл '{file}' успешно создан")
            
    def read_file(self, file):
        # Прочитать содержимое файла
        try:
            with open(os.path.join(self.curr_dir, file), 'r') as f:
                print(f.read())
        except FileNotFoundError:
            print(f"Файл '{file}' не найден")

    def write_file(self, file, input):
        # Записать в файл
        with open(os.path.join(self.curr_dir, file), 'w') as f:
            f.write(input)
            print(f"Содержимое записано в '{file}' успешно")

    def delete_file(self, file):
        # Удаление файла
        new_path = os.path.join(curr_dir, file)
        try:
            os.remove(new_path)
            print(f"Файл {file} удалён успешно")
        except FileNotFoundError:
            print(f"Файл '{file}' не найден")


    def copy_file(self, from_file, to_file):
        # Скопировать файл
        from_path = os.path.join(self.curr_dir, from_file)
        to_path = os.path.join(self.curr_dir, to_file)
        try:
            shutil.copy(from_path, to_path)
            print(f"Файл '{from_file}' скопирован в '{to_file}' успешно")
        except FileNotFoundError:
            print(f"Файл '{from_file}' не найден")
        except FileExistsError:
            print(f"Файл '{to_file}' уже существует")

    def move_file(self, from_file, to_dir):
        # Переместить файл
        from_path = os.path.join(self.curr_dir, from_file)
        to_path = os.path.join(self.curr_dir, to_dir)
        if os.path.exists(to_path):
            try:
                shutil.move(from_path, to_path)
                print(f"Файл '{from_file}' перемещен в '{to_dir}' успешно")
            except FileNotFoundError:
                print(f"Файл '{from_file}' не найден")
        else:
            print(f"Директория '{to_dir}' не найдена")


    def rename_file(self, file_name, new_file_name):
        # Переименовать файл
        curr_path = os.path.join(self.curr_dir, file_name)
        new_path = os.path.join(self.curr_dir, new_file_name)
        try:
            os.rename(curr_path, new_path)
            print(f"Файл '{file_name}' переименован в '{new_file_name}' успешно")
        except FileNotFoundError:
            print(f"Файл '{file_name}' не найден")
        except FileExistsError:
            print(f"Файл '{new_file_name}' уже существует")

