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