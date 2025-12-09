# Лабораторная работа №9
``` python
import csv
from pathlib import Path
import sys

sys.path.append("C:/Users/kira_/OneDrive/Рабочий стол/python_labss/")
from src.lab08.models import Student


class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        self._ensure_storage_exists()
        # self._validation()

    def _ensure_storage_exists(self) -> None:
        """Создаём файл для записи, если его нет"""
        if not self.path.exists():
            with open(self.path, "w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(
                    f, fieldnames=["Студент", "Группа", "Дата рождения", "Средний балл"]
                )
                writer.writeheader()

    # def _validation(self):
    #     with

    def _read_all(self):
        """Читает все строки из csv-файла"""
        rows = []
        with self.path.open("r", encoding="utf-8") as csv_file:
            data_csv = csv.DictReader(csv_file)
            if data_csv.fieldnames != [
                "Студент",
                "Группа",
                "Дата рождения",
                "Средний балл",
            ]:
                raise ValueError("Неккоректные заголовки")
            for row in data_csv:
                try:
                    float(row["Средний балл"])
                except ValueError:
                    raise ValueError("Средний балл должен быть числом")
                rows.append(row)
        return rows

    def _write_all(self, rows):
        """Записать все строки в CSV файл"""
        with open(self.path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file, fieldnames=["Студент", "Группа", "Дата рождения", "Средний балл"]
            )
            writer.writeheader()
            writer.writerows(rows)

    def list(self) -> list[Student]:
        rows = self._read_all()
        students = []
        for row in rows:
            try:
                student = Student.from_dict(row)
                students.append(student)
            except ValueError:
                raise ValueError("Ошибка валидации студента")

        return students

    def add(self, student: Student):
        """Добавить в список ещё 1 строку-студента"""
        all_students = self._read_all()

        if not isinstance(student, Student):  # Проверка корректности формата данных
            raise ValueError("Должен быть передан объект Student")
        for row in all_students:  # Проверяем, есть ли уже такой студент в списке
            if row["Студент"] == student.fio:
                raise ValueError(f"Студент с ФИО '{student.fio}' уже существует")

        try:
            validated_student = Student(
                fio=student.fio,
                birthdate=student.birthdate,
                group=student.group,
                gpa=student.gpa,
            )
        except ValueError:
            raise ValueError("Ошибка валидации студента")

        with open(self.path, "a", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(
                f, fieldnames=["Студент", "Группа", "Дата рождения", "Средний балл"]
            )
            writer.writerow(validated_student.to_dict())

    def find(self, substr: str):
        students = self.list()
        return [
            student for student in students if substr.lower() in student.fio.lower()
        ]

    def remove(self, fio: str):
        """Удалить записи с определенным ФИО"""
        rows = self._read_all()
        initial_count = len(rows)

        rows = [row for row in rows if row["Студент"] != fio]
        if len(rows) == initial_count:
            raise ValueError(f"Студент с ФИО '{fio}' не найден")
        self._write_all(rows)

    def update(self, fio: str, **fields):
        """
        Обновить поля существующего студента
        **fields - передаёт любое количество полей для обновления
        """
        all_students = self._read_all()
        updated = (
            False  # Используем флаг, чтобы в случае отсутсвия студента вывести ошибку
        )

        for student in all_students:
            if student["Студент"] == fio:
                if "Группа" in fields:
                    student["Группа"] = fields["Группа"]
                if "Дата рождения" in fields:
                    student["Дата рождения"] = fields["Дата рождения"]
                if "Балл" in fields:
                    student["Средний балл"] = fields["Балл"]
                updated = True  # Поднимаем флаг
                break
                if not updated:
                    raise ValueError(f"Студент с ФИО {fio} не найден")

        self._write_all(all_students)
```
### Просмотр всей группы студентов
``` python
if __name__ == "__main__":

    group = Group("data/lab09/students.csv")  # Создаем группу

    print("Просмотр всей группы студентов:")
    students = group.list()
    for student in students:
        print(student)
        print()
```
![1](/images/lab09/1.png)

### Добавление новых студентов
``` python
if __name__ == "__main__":
    group = Group("data/lab09/students.csv")
    
    new_students = [
            Student("Смирнов Дмитрий Александрович", "2007-07-18", "БИВТ-25-1", 4.2),
            Student("Кузнецова Екатерина Игоревна", "2007-09-05", "БИВТ-25-2", 4.6),
        ]
        for student in new_students:
            group.add(student)
``` 
![2](/images/lab09/2.png)

### Поиск студента по фамилии Петрова
``` python
if __name__ == "__main__":
    group = Group("data/lab09/students.csv")

    print("Поиск студента по фамилии Петрова")
        for student in group.find("Петрова"):
            print(f"  {student}")
``` 
![3](/images/lab09/3.png)

### Удаление студента с ФИО Сидоров Алексей Петрович
``` python
if __name__ == "__main__":
    group = Group("data/lab09/students.csv")

    print("Удаление студента с ФИО Сидоров Алексей Петрович:")
        group.remove("Сидоров Алексей Петрович")
        students = group.list()
        for student in students:
            print(f"  {student}")
```
![4](/images/lab09/4.png)

### Изменение существующей информации
``` python
if __name__ == "__main__":
    group = Group("data/lab09/students.csv")

    print("Изменение существующей информации:")
        print("Данные Ивана до:")
        for student in group.find("Иванов"):
            print(f"  {student}")
        group.update("Иванов Иван Иванович", Группа="БИВТ-25-8", Балл=4.8)
        print("Данные Ивана после:")
        for student in group.find("Иванов"):
            print(f"  {student}")
```
![5](/images/lab09/5.png)