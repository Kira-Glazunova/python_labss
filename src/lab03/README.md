# Лабораторная работа 3 — Тексты и частоты слов (словарь/множество)

### Задание A
```python
from re import finditer

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold: 
        text = text.casefold()          # нижний регистр
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')         # меняем "ё" на "е"
    text = text.replace('\t', ' ').replace('\r', ' ').replace('\n', ' ')
    while '  ' in text:
        text = text.replace('  ', ' ')          # схлопывыаем пробелы
    return text.strip()


def tokenize(text: str) -> list[str]:
    tokens = finditer(pattern = r'\w+(?:-\w+)*', string = text)         # ищем слова с дефисами
    return [i.group() for i in tokens]


def count_freq(tokens: list[str]) -> dict[str, int]:
    count = {}          # создаем пустой словарь для подсчетов
    for i in tokens:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1            # если есть, то счетчик увеличивается на 1, иначе добавляем значение с единицей
    return count


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    freq = sorted(freq.items(), key=lambda item: [-item[1], item[0]])       # список кортежей (ключ, значение) сортируем частоту по убыванию, а слова по возрастанию
    result = []
    for i in range(min(n, len(freq))):
        result.append((freq[i][0], freq[i][1]))
    return result
```
![exA](images/lab03/exA.png)

### Задание B
```python
import sys   # импортируем систему, чтобы применить ввод stdin и добавить путь к папке
sys.path.append(r'C:\Users\kira_\OneDrive\Рабочий стол\python_labss\src')  # добавляем путь к папке
from lib.text import normalize, tokenize, count_freq, top_n

def main():
    stroke = sys.stdin.read()   # читаем весь ввод до конца файла. Чтобы его прервать -> Ctr+Z+Enter
    norm_stroke = tokenize(normalize(stroke))   # приводим все к одному регистру
    uniq_stroke = len(set(norm_stroke))   # возвращаем список уникальных элементов
    freq = count_freq(norm_stroke)
    top_5 = top_n(freq, 5)

    print('Всего слов:', len(norm_stroke))
    print('Уникальных слов:', uniq_stroke)
    print('Топ-5:')
    for i in top_5:
        print(f'{i[0]}:{i[1]}') 

while True:  # для бесконечного вызова функции
    main()   # вызов функции
```
![exB](images/lab03/exB.png)