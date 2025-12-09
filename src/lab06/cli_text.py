import argparse
import sys

sys.path.append(r"C:\Users\kira_\OneDrive\Рабочий стол\python_labss\src")

from pathlib import Path
from lib.text import normalize, tokenize, count_freq, top_n


def main():
    parser = argparse.ArgumentParser(description="CLI-утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # Подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к входному файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # Подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    # Если команда не указана, показываем справку
    if not args.command:
        parser.print_help()
        return

    # Проверка существования файла
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Ошибка: файл не найден: {args.input}")
        sys.exit(1)

    # Файл нужно получать из соответствующей команды
    if args.command == "cat":
        with open(input_path, "r", encoding="utf-8") as f:
            count = 1
            for line in f:
                line = line.rstrip("\n")
                if args.n:
                    print(f"{count}: {line}")
                    count += 1
                else:
                    print(line)

    elif args.command == "stats":
        with open(input_path, "r", encoding="utf-8") as f:
            content = f.read()
            normalized = normalize(content)  # Добавил нормализацию
            tokens = tokenize(normalized)
            freq = count_freq(tokens)
            top = top_n(freq, n=args.top)

            print(f"Всего уникальных слов: {len(freq)}")
            print(f"Топ-{args.top} самых частых слов:\n")

            num = 1
            for word, count in top:
                print(f"{num}. {word} - {count}")
                num += 1


if __name__ == "__main__":
    main()
