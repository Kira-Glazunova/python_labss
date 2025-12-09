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


# Для тестов
stud = [
    Student("Иванов Иван Иванович", "2007-01-15", "БИВТ-25-1", 4.5),
    Student("Петрова Анна Сергеевна", "2007-03-22", "БИВТ-25-2", 4.8),
    Student("Сидоров Алексей Петрович", "2007-05-10", "БИВТ-25-3", 3.9),
    Student("Козлова Мария Владимировна", "2007-07-28", "БИВТ-25-4", 4.2),
]
students_to_json(stud, "data/out/students.json")
print(students_from_json("data/samples/students_input.json"))