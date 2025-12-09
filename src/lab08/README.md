# Лабораторная работа №8
### Задание A
``` python
from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        # Валидация формата даты
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Неверная запись времени")

        # Валидация диапазона GPA
        if not (0 <= float(self.gpa) <= 5):
            raise ValueError("GPA должен находиться между 0 и 5")

    def age(self) -> int:
        """Возвращает количество полных лет"""
        birth_day = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        if birth_day > today:
            raise ValueError("Студент еще не родился")
        if today.month < birth_day.month or (
            today.month == birth_day.month and today.day < birth_day.day
        ):
            return today.year - birth_day.year - 1
        return today.year - birth_day.year

    def to_dict(self) -> dict:
        return {
            "Студент": self.fio,
            "Группа": self.group,
            "Дата рождения": self.birthdate,
            "Средний балл": self.gpa,
        }

    @classmethod  # Метод создаёт новый объект из существующих данных
    def from_dict(cls, d: dict):
        # Создание объекта класса Student из словаря
        return cls(
            fio=d["Студент"],
            group=d["Группа"],
            birthdate=d["Дата рождения"],
            gpa=d["Средний балл"],
        )

    def __str__(self):
        return (
            f"Студент: {self.fio};\n"
            f"Группа: {self.group};\n"
            f"Дата рождения: {self.birthdate};\n"
            f"Средний балл: {self.gpa}."
        )

```
### Запуск задания
``` python
if __name__ == "__main__":
    student = Student("Иванов Иван Иванович", "2007-01-15", "БИВТ-25-1", 4.5)
    print(student)
    print("=" * 140)

    # age
    print(f"Возраст: {student.age()}")

    # to_dict
    student_dict = student.to_dict()
    print(f"Сериализованный: {student_dict}")

    # from_dict
    restored_student = Student.from_dict(student_dict)
    print(f"Десериализованный: {restored_student}")
```
![A](images/lab08/2.png)
### Задание B 
``` python
import json
from pathlib import Path
from models import Student


def students_to_json(students: list[Student], path: str):
    data = [s.to_dict() for s in students]
    path = Path(path)
    with open(path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)


def students_from_json(path: str):
    path = Path(path)
    with open(path, "r", encoding="utf-8") as json_file:
        try:
            students = json.load(json_file)
        except (
            json.JSONDecodeError
        ):  # Выходит, когда файл невозможно загрузить в формате JSON
            raise ValueError("Пустой JSON или неподдерживаемая структура")

    if not students:  # Явная проверка существования данных
        raise ValueError("Пустой файл")

    if not isinstance(students, list):
        raise ValueError("Файл не JSON формата: не список словарей")

    if not all(isinstance(row, dict) for row in students):
        raise ValueError("Файл не JSON формата: в списке не словари")

    stud_list = []

    for data in students:
        student = Student.from_dict(data)
        stud_list.append(student)
    return stud_list

```
### Тест
``` python
stud = [
    Student("Иванов Иван Иванович", "2007-01-15", "БИВТ-25-1", 4.5),
    Student("Петрова Анна Сергеевна", "2007-03-22", "БИВТ-25-2", 4.8),
    Student("Сидоров Алексей Петрович", "2007-05-10", "БИВТ-25-3", 3.9),
    Student("Козлова Мария Владимировна", "2007-07-28", "БИВТ-25-4", 4.2),
]
students_to_json(stud, "data/out/students.json")
print(students_from_json("data/samples/students_input.json"))
```
![b](images/lab08/1.png)