from collections import deque
from typing import Any


class Stack:
    def __init__(self):  # Инициализация стека
        self._data = []

    def is_empty(self) -> bool:
        if len(self._data) == 0:
            return True

    def push(self, item) -> Any:  # Добавление элемента item на вершину стека
        self._data.append(item)

    def pop(self) -> Any:  # Извлечь последний элемент стека
        if self.is_empty():
            raise IndexError("Стек пустой, невозможно извлечь последний элемент")
        return self._data.pop()

    def peek(self) -> Any | None:  # Снять верхний элемент стека и вернуть его
        if self.is_empty():
            return None  # При пустом стеке просмотреть верхний элемент стека и вернуть его невозможно
        return self._data[-1]

    def __len__(self) -> int:
        return len(self._data)


class Queue:
    def __init__(self):  # Инициализация очереди
        self._data = deque()

    def enqueue(self, item) -> None:  # Вставка в конец очереди
        self._data.append(item)

    def dequeue(self) -> Any:  # Взять элемент из начала очереди и вернуть его
        if self.is_empty():
            raise IndexError("Очередь пуста:невозможно извлечь первый элемент")
        return self._data.popleft()

    def peek(self) -> Any | None:  # Вернуть первый элемент без удаления
        if self.is_empty():
            raise None
        return self._data[0]

    def is_empty(self) -> bool:  # Проверка пустоты очереди
        if len(self._data) == 0:
            return True

    def __len__(self) -> int:
        return len(self._data)

if __name__ == "__main__":
    test = Stack()
    test.push(1)
    test.push(2)
    test.push(3)
    print(f'\nИмеющийся стек - длина 3')
    print(f'Смотрим последний элемент:')
    print(test.peek(), '\n')
    print(f'Извлекаем последний элемент -> длина теперь 2')
    test.pop()
    print(f'Количество элементов:')
    print(test.__len__(), '\n')
    test = Queue()
    test.enqueue(1)
    test.enqueue(2)
    test.enqueue(3)
    test.enqueue(4)
    print(f'\nИмеющаяся очередь - длина 4: 1, 2, 3, 4')
    print(f'Возвращаем элемент из начала очереди без удаления:')
    print(test.peek(), '\n')
    print(f'Берем элемент из начала очереди:')
    print(test.dequeue(), '\n')
    print(f'Количество элементов в очереди после удаления (3):')
    print(test.__len__(), '\n')