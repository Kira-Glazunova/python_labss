from pathlib import Path
import csv
from typing import Iterable, Sequence
from collections import Counter


def ensure_parent_dir(path: Path | str) -> None:
    p = Path(path)
    parent_dir = p.parent  # создаем родительскую директорию, если ее еще нет
    parent_dir.mkdir(parents=True, exist_ok=True)


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)  # создаем путь к файлу - Path-объект

    if not p.exists():  # проверка существования файла
        raise FileNotFoundError("Файл не найден")
    return p.read_text(encoding=encoding)


def write_csv(
    rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None
) -> None:

    p = Path(path)  # Создаем путь
    rows = list(rows)

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)  # создаем объект writer для записи в csv формат
        if header is not None:
            w.writerow(header)  # записываем заголовок, если такой существует

        if rows:  # проверка на не равную длину строк
            for r in rows:
                if len(r) != len(rows[0]):
                    raise ValueError("Строки имеют разную длину!")

        for r in rows:
            w.writerow(r)  # запись рядов построчно


# функция не возвращает ничего, она записывает данные в CSV файл


"""def write_text(txt: str, path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)   # Создаем путь к файлу - Path-объект
    return p.write_text(encoding=encoding)"""
