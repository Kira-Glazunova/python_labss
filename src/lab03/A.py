from re import finditer


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()  # нижний регистр

    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")  # меняем "ё" на "е"

    text = text.replace("\t", " ").replace("\r", " ").replace("\n", " ")

    while "  " in text:
        text = text.replace("  ", " ")  # схлопывыаем пробелы

    return text.strip()


def tokenize(text: str) -> list[str]:
    tokens = finditer(pattern=r"\w+(?:-\w+)*", string=text)  # ищем слова с дефисами

    return [i.group() for i in tokens]


def count_freq(tokens: list[str]) -> dict[str, int]:
    count = {}  # создаем пустой словарь для подсчетов
    for i in tokens:
        if i in count:
            count[i] += 1
        else:
            count[i] = (
                1  # если есть, то счетчик увеличивается на 1, иначе добавляем значение с единицей
            )
    return count


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    freq = sorted(
        freq.items(), key=lambda item: [-item[1], item[0]]
    )  # список кортежей (ключ, значение) сортируем частоту по убыванию, а слова по возрастанию
    top_n = []
    for i in range(min(n, len(freq))):
        top_n.append((freq[i][0], freq[i][1]))

    return top_n


print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))
print()

print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))
print()

print(top_n(count_freq(["a", "b", "a", "c", "b", "a"]), n=2))
print(top_n(count_freq(["bb", "aa", "bb", "aa", "cc"]), n=2))
