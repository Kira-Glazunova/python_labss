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
