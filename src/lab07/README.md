# Лабораторная работа №7
### Задание A - test_text
```python
import pytest
import sys
from pathlib import Path

# Добавляем путь к проекту для импорта
sys.path.append("C:/Users/kira_/OneDrive/Рабочий стол/python_labss/")

from src.lib.text import normalize, tokenize, count_freq, top_n


class TestNormalize:
    """Тесты для функции normalize()"""

    @pytest.mark.parametrize(
        "input_text, expected",
        [
            ("ПрИвЕт\nМИр\t", "привет мир"),
            ("ёжик, Ёлка", "ежик, елка"),
            ("Hello\r\nWorld", "hello world"),
            ("  двойные   пробелы  ", "двойные пробелы"),
            ("", ""),
            ("   ", ""),
            ("Текст\nс\nпереносами", "текст с переносами"),
            ("Раз\t\tдва\tтри", "раз два три"),
            ("Верхний РЕГИСТР", "верхний регистр"),
            ("смесь Ё и Е", "смесь е и е"),
        ],
    )
    def test_normalize_basic(self, input_text, expected):
        """Базовые тесты нормализации"""
        assert normalize(input_text) == expected

    def test_normalize_casefold_false(self):
        """Тест с отключенным casefold"""
        text = "ПрИвЕт МиР"
        result = normalize(text, casefold=False)
        assert result == "ПрИвЕт МиР"

    def test_normalize_yo2e_false(self):
        """Тест с отключенной заменой ё на е"""
        text = "ёжик Ёлка"
        result = normalize(text, yo2e=False)
        assert result == "ёжик ёлка"


class TestTokenize:
    """Тесты для функции tokenize()"""

    @pytest.mark.parametrize(
        "input_text, expected",
        [
            ("привет мир", ["привет", "мир"]),
            ("hello,world!!!", ["hello", "world"]),
            ("по-настоящему круто", ["по-настоящему", "круто"]),
            ("2025 год", ["2025", "год"]),
            ("emoji 😀 не слово", ["emoji", "не", "слово"]),
            ("", []),
            ("   ", []),
            ("!!! @#$ %^&*", []),
            ("слово-с-дефисом и еще", ["слово-с-дефисом", "и", "еще"]),
            ("много     пробелов", ["много", "пробелов"]),
        ],
    )
    def test_tokenize_basic(self, input_text, expected):
        """Базовые тесты токенизации"""
        assert tokenize(input_text) == expected

    def test_tokenize_with_normalized_text(self):
        """Тест токенизации после нормализации"""
        text = "ПрИвЕт, МиР! 2025-й год."
        normalized = normalize(text)
        tokens = tokenize(normalized)
        assert tokens == ["привет", "мир", "2025", "й", "год"]


class TestCountFreq:
    """Тесты для функции count_freq()"""

    def test_count_freq_basic(self):
        """Базовый тест подсчета частот"""
        tokens = ["a", "b", "a", "c", "b", "a"]
        result = count_freq(tokens)
        expected = {"a": 3, "b": 2, "c": 1}
        assert result == expected

    def test_count_freq_empty(self):
        """Тест с пустым списком"""
        result = count_freq([])
        assert result == {}

    def test_count_freq_single_token(self):
        """Тест с одним токеном"""
        result = count_freq(["слово"])
        assert result == {"слово": 1}

    def test_count_freq_case_sensitive(self):
        """Тест чувствительности к регистру"""
        tokens = ["Word", "word", "WORD"]
        result = count_freq(tokens)
        assert result == {"Word": 1, "word": 1, "WORD": 1}


class TestTopN:
    """Тесты для функции top_n()"""

    def test_top_n_basic(self):
        """Базовый тест top_n"""
        freq = {"a": 5, "b": 3, "c": 7, "d": 1, "e": 4}
        result = top_n(freq, n=3)
        expected = [("c", 7), ("a", 5), ("e", 4)]
        assert result == expected

    def test_top_n_tie_breaker(self):
        """Тест разрешения ничьих по алфавиту"""
        freq = {"banana": 3, "apple": 3, "cherry": 3, "date": 2}
        result = top_n(freq, n=3)
        # При одинаковой частоте сортировка по алфавиту
        expected = [("apple", 3), ("banana", 3), ("cherry", 3)]
        assert result == expected

    def test_top_n_more_than_available(self):
        """Тест когда запрашиваем больше элементов чем есть"""
        freq = {"a": 2, "b": 1}
        result = top_n(freq, n=10)
        assert result == [("a", 2), ("b", 1)]

    def test_top_n_empty_dict(self):
        """Тест с пустым словарем"""
        result = top_n({}, n=5)
        assert result == []

    def test_top_n_n_zero(self):
        """Тест с n=0"""
        freq = {"a": 1, "b": 2}
        result = top_n(freq, n=0)
        assert result == []

    def test_top_n_negative_n(self):
        """Тест с отрицательным n"""
        freq = {"a": 1, "b": 2}
        result = top_n(freq, n=-1)
        assert result == []

    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, [("c", 3)]),
            (2, [("c", 3), ("a", 2)]),
            (3, [("c", 3), ("a", 2), ("b", 1)]),
        ],
    )
    def test_top_n_parametrized(self, n, expected):
        """Параметризованный тест top_n"""
        freq = {"a": 2, "b": 1, "c": 3}
        result = top_n(freq, n=n)
        assert result == expected


class TestIntegration:
    """Интеграционные тесты всех функций вместе"""

    def test_full_pipeline(self):
        """Полный пайплайн: нормализация -> токенизация -> подсчет -> топ"""
        text = "Привет мир! Привет всем. Мир прекрасен."

        normalized = normalize(text)
        assert normalized == "привет мир привет всем мир прекрасен"

        tokens = tokenize(normalized)
        assert tokens == ["привет", "мир", "привет", "всем", "мир", "прекрасен"]

        freq = count_freq(tokens)
        assert freq == {"привет": 2, "мир": 2, "всем": 1, "прекрасен": 1}

        top = top_n(freq, n=2)
        # При одинаковой частоте "мир" идет перед "привет" по алфавиту
        assert top == [("мир", 2), ("привет", 2)]

    def test_empty_text_pipeline(self):
        """Тест пайплайна с пустым текстом"""
        text = ""

        normalized = normalize(text)
        assert normalized == ""

        tokens = tokenize(normalized)
        assert tokens == []

        freq = count_freq(tokens)
        assert freq == {}

        top = top_n(freq, n=5)
        assert top == []

```
![A](/images/lab07/1.png)

### Задание B - test_json_csv
```python
import pytest
import json
import csv
import sys
from pathlib import Path
from unittest.mock import mock_open, patch

# Добавляем путь к проекту для импорта
sys.path.append("C:/Users/kira_/OneDrive/Рабочий стол/python_labss/")

from src.lab05.json_csv import json_to_csv, csv_to_json


class TestJsonToCsv:
    """Тесты для функции json_to_csv()"""

    def test_json_to_csv_basic(self, tmp_path):
        """Базовый тест конвертации JSON -> CSV"""
        # Создаем тестовый JSON файл
        json_file = tmp_path / "test.json"
        json_data = [
            {"name": "Alice", "age": 22, "city": "SPB"},
            {"name": "Bob", "age": 25, "city": "Moscow"},
            {"name": "Carlos", "age": 30, "city": "Kazan"},
        ]
        json_file.write_text(
            json.dumps(json_data, ensure_ascii=False), encoding="utf-8"
        )

        # Конвертируем в CSV
        csv_file = tmp_path / "test.csv"
        json_to_csv(str(json_file), str(csv_file))

        # Проверяем результат
        assert csv_file.exists()

        with open(csv_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        assert len(rows) == 3
        assert set(rows[0].keys()) == {"name", "age", "city"}
        assert rows[0]["name"] == "Alice"
        assert rows[0]["age"] == "22"
        assert rows[0]["city"] == "SPB"

    def test_json_to_csv_missing_fields(self, tmp_path):
        """Тест с отсутствующими полями в некоторых объектах"""
        json_file = tmp_path / "test.json"
        json_data = [
            {"name": "Alice", "age": 22},
            {"name": "Bob", "age": 25, "city": "Moscow"},
            {"name": "Carlos", "city": "Kazan"},
        ]
        json_file.write_text(
            json.dumps(json_data, ensure_ascii=False), encoding="utf-8"
        )

        csv_file = tmp_path / "test.csv"
        json_to_csv(str(json_file), str(csv_file))

        with open(csv_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        # Проверяем что все поля есть в заголовке
        assert set(rows[0].keys()) == {"name", "age", "city"}

        # Проверяем значения (пустые строки для отсутствующих полей)
        assert rows[0]["city"] == ""
        assert rows[2]["age"] == ""

    def test_json_to_csv_unicode(self, tmp_path):
        """Тест с Unicode символами"""
        json_file = tmp_path / "test.json"
        json_data = [
            {"name": "Анна", "city": "Москва", "comment": "Привет!"},
            {"name": "John", "city": "New York", "comment": "Hello!"},
        ]
        json_file.write_text(
            json.dumps(json_data, ensure_ascii=False), encoding="utf-8"
        )

        csv_file = tmp_path / "test.csv"
        json_to_csv(str(json_file), str(csv_file))

        with open(csv_file, "r", encoding="utf-8") as f:
            content = f.read()

        assert "Анна" in content
        assert "Москва" in content
        assert "Привет" in content

    def test_json_to_csv_file_not_found(self):
        """Тест с несуществующим файлом"""
        with pytest.raises(FileNotFoundError, match="Файл не найден"):
            json_to_csv("nonexistent.json", "output.csv")

    def test_json_to_csv_invalid_json(self, tmp_path):
        """Тест с некорректным JSON"""
        json_file = tmp_path / "test.json"
        json_file.write_text("{invalid json", encoding="utf-8")

        with pytest.raises(
            ValueError, match="Пустой JSON или неподдерживаемая структура"
        ):
            json_to_csv(str(json_file), "output.csv")

    def test_json_to_csv_empty_json(self, tmp_path):
        """Тест с пустым JSON"""
        json_file = tmp_path / "test.json"
        json_file.write_text("[]", encoding="utf-8")

        with pytest.raises(ValueError, match="Пустой JSON"):
            json_to_csv(str(json_file), "output.csv")

    def test_json_to_csv_not_list(self, tmp_path):
        """Тест с JSON не являющимся списком"""
        json_file = tmp_path / "test.json"
        json_file.write_text('{"name": "Alice"}', encoding="utf-8")

        with pytest.raises(ValueError, match="не список словарей"):
            json_to_csv(str(json_file), "output.csv")

    def test_json_to_csv_not_list_of_dicts(self, tmp_path):
        """Тест с JSON списком не словарей"""
        json_file = tmp_path / "test.json"
        json_file.write_text('["Alice", "Bob"]', encoding="utf-8")

        with pytest.raises(ValueError, match="в списке не словари"):
            json_to_csv(str(json_file), "output.csv")


class TestCsvToJson:
    """Тесты для функции csv_to_json()"""

    def test_csv_to_json_basic(self, tmp_path):
        """Базовый тест конвертации CSV -> JSON"""
        # Создаем тестовый CSV файл
        csv_file = tmp_path / "test.csv"
        csv_content = """name,age,city
Alice,22,SPB
Bob,25,Moscow
Carlos,30,Kazan"""
        csv_file.write_text(csv_content, encoding="utf-8")

        # Конвертируем в JSON
        json_file = tmp_path / "test.json"
        csv_to_json(str(csv_file), str(json_file))

        # Проверяем результат
        assert json_file.exists()

        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        assert len(data) == 3
        assert isinstance(data, list)
        assert all(isinstance(item, dict) for item in data)

        assert data[0] == {"name": "Alice", "age": "22", "city": "SPB"}
        assert data[1] == {"name": "Bob", "age": "25", "city": "Moscow"}
        assert data[2] == {"name": "Carlos", "age": "30", "city": "Kazan"}

    def test_csv_to_json_quotes_and_commas(self, tmp_path):
        """Тест с кавычками и запятыми в значениях"""
        csv_file = tmp_path / "test.csv"
        csv_content = '''name,message
Alice,"Hello, world!"
Bob,"He said ""wow"" and left"'''
        csv_file.write_text(csv_content, encoding="utf-8")

        json_file = tmp_path / "test.json"
        csv_to_json(str(csv_file), str(json_file))

        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        assert data[0]["message"] == "Hello, world!"
        assert data[1]["message"] == 'He said "wow" and left'

    def test_csv_to_json_unicode(self, tmp_path):
        """Тест с Unicode символами"""
        csv_file = tmp_path / "test.csv"
        csv_content = """name,city
Анна,Москва
John,New York"""
        csv_file.write_text(csv_content, encoding="utf-8")

        json_file = tmp_path / "test.json"
        csv_to_json(str(csv_file), str(json_file))

        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        assert data[0]["name"] == "Анна"
        assert data[0]["city"] == "Москва"

    def test_csv_to_json_empty_csv(self, tmp_path):
        """Тест с пустым CSV (только заголовки)"""
        csv_file = tmp_path / "test.csv"
        csv_content = "name,age,city"
        csv_file.write_text(csv_content, encoding="utf-8")

        json_file = tmp_path / "test.json"
        csv_to_json(str(csv_file), str(json_file))

        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        assert data == []

    def test_csv_to_json_missing_file(self):
        """Тест с несуществующим CSV файлом"""
        with pytest.raises(FileNotFoundError):
            csv_to_json("nonexistent.csv", "output.json")

    def test_csv_to_json_wrong_extension(self):
        """Тест с файлом неверного расширения"""
        with pytest.raises(ValueError, match="Неверный тип файла"):
            csv_to_json("data.txt", "output.json")

    def test_csv_to_json_empty_file(self, tmp_path):
        """Тест с полностью пустым файлом"""
        csv_file = tmp_path / "test.csv"
        csv_file.write_text("", encoding="utf-8")

        with pytest.raises(ValueError, match="Пустой файл"):
            csv_to_json(str(csv_file), "output.json")


class TestRoundTrip:
    """Тесты циклической конвертации (туда-обратно)"""

    def test_json_csv_json_roundtrip(self, tmp_path):
        """JSON -> CSV -> JSON должен сохранять данные"""
        # Исходные данные
        original_data = [
            {"name": "Alice", "age": 22, "city": "SPB"},
            {"name": "Bob", "age": 25, "city": "Moscow"},
            {"name": "Carlos", "age": 30, "city": "Kazan", "extra": "field"},
        ]

        # 1. Сохраняем в JSON
        json1 = tmp_path / "test1.json"
        json1.write_text(
            json.dumps(original_data, ensure_ascii=False), encoding="utf-8"
        )

        # 2. Конвертируем JSON -> CSV
        csv_file = tmp_path / "test.csv"
        json_to_csv(str(json1), str(csv_file))

        # 3. Конвертируем CSV -> JSON
        json2 = tmp_path / "test2.json"
        csv_to_json(str(csv_file), str(json2))

        # 4. Загружаем и сравниваем
        with open(json2, "r", encoding="utf-8") as f:
            roundtrip_data = json.load(f)

        # Проверяем количество записей
        assert len(roundtrip_data) == len(original_data)

        # Проверяем что все оригинальные поля присутствуют
        for orig, rt in zip(original_data, roundtrip_data):
            for key in orig:
                assert key in rt
                # CSV хранит все как строки, поэтому сравниваем как строки
                assert str(orig[key]) == rt[key]

    def test_csv_json_csv_roundtrip(self, tmp_path):
        """CSV -> JSON -> CSV должен сохранять данные"""
        # Исходный CSV
        csv1 = tmp_path / "test1.csv"
        csv_content = """name,age,city
Alice,22,SPB
Bob,25,Moscow
Carlos,30,Kazan"""
        csv1.write_text(csv_content, encoding="utf-8")

        # 1. Конвертируем CSV -> JSON
        json_file = tmp_path / "test.json"
        csv_to_json(str(csv1), str(json_file))

        # 2. Конвертируем JSON -> CSV
        csv2 = tmp_path / "test2.csv"
        json_to_csv(str(json_file), str(csv2))

        # 3. Сравниваем CSV файлы
        with open(csv1, "r", encoding="utf-8") as f1, open(
            csv2, "r", encoding="utf-8"
        ) as f2:
            content1 = f1.read()
            content2 = f2.read()

        # Игнорируем возможные различия в порядке строк
        lines1 = sorted(content1.splitlines())
        lines2 = sorted(content2.splitlines())

        assert lines1 == lines2

```
![B](/images/lab07/2.png)

### Задание C - black
![C](/images/lab07/3.png)