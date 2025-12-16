# Лабораторная работа №10 — Структуры данных: Stack, Queue, Linked List и бенчмарки
## Теоретическая часть
### Stack
Стек — это структура данных, работающая по принципу "последним пришёл — первым вышел" (LIFO, Last In First Out). Представляет собой список элементов, организованных по принципу LIFO.

**Основные операции:**
* `push(item)` — добавить элемент на вершину стека — O(1)
* `pop()` — извлечь верхний элемент — O(1)
* `peek()` — посмотреть верхний элемент без извлечения — O(1)
* `is_empty()` — проверить, пуст ли стек — O(1)

**Применение:**
* Обратная польская нотация
* Рекурсивные вызовы функций
* Отмена операций (undo)

### Реализация
``` python
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
```
![](/images/lab10/1.png)



### Queue
Очередь — это структура данных, работающая по принципу "первым пришёл — первым вышел" (FIFO, First In First Out). Представляет собой список элементов, организованных по принципу FIFO.

**Основные операции:**
* `enqueue(item)` — добавить элемент в конец очереди
* `dequeue()` — извлечь первый элемент
* `peek()` — посмотреть первый элемент без извлечения
* `is_empty()` — проверить, пуста ли очередь

**Применение:**
* Планирование задач
* Обработка запросов
* Алгоритмы обхода графов

### Реализация
```python
from collections import deque
from typing import Any


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
```
![alt text](/images/lab10/2.png)

### Односвязный список
Односвязный список — это динамическая структура данных, состоящая из последовательности узлов (DoubleNode), где каждый узел содержит данные, ссылку на следующий узел и ссылку на предыдущий узел.

**Основные операции:**
* `append(x)` — добавить элемент в конец списка.
* `prepend(x)` — добавить элемент в начало списка.
* `pinsert(i, x)` — вставить элемент по индексу.
* `remove(x)` — удалить элемент по значению.
* `remove_at(i)` — удалить элемент по индексу.

**Применение:**
* Динамическое управление памятью.
* Списки свободных блоков в файловых системах.
* Реализация стеков и очередей.

### Двусвязный список
Двусвязный список — это динамическая структура данных, состоящая из последовательности узлов (DNode), где каждый узел содержит данные, ссылку на следующий узел и ссылку на предыдущий узел.

**Применение:**
* Реализация LRU-кэша (Least Recently Used).
* История в браузерах (вперёд/назад).
* Редакторы текста с возможностью отмены.

### Реализация
```python
from typing import Any

class Node: # Узел
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self): # Инициализация пустого списка
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value): # Добавить элемент в конец списка
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else: # Для непустого списка
            self.tail.next = new_node # Устанавливаем указатель next последнего узла на новый элемент
            self.tail = new_node # Теперь new_node - последний узел
            """Итог - не О(n), а о(1)"""
            
        self._size += 1 # Обновляем длину

    def prepend(self, value):
        """Добавить элемент в начало списка, 1 операция"""
        new_node = Node(value, next=self.head)
        self.head = new_node
        
        self._size += 1 # Обновляем длину


    def insert(self, idx, value):
        """Вставка по индексу — неполная реализация, есть ошибки"""
        if idx < 0 or idx > self._size:
            raise IndexError("negative index is not supported")
        
        if idx == 0:
            self.prepend(value)
            return
        
        if idx == self._size:
            self.append(value)
            return
        
        current = self.head
        for _ in range(idx - 1):
            current = current.next # Доходим до эл-та, стоящего до необходимого

        new_node = Node(value, next=current.next) # Создаем необходимый узел. След. за ним - который сейчас на его месте
        current.next = new_node # Делаем ссылке на необходимый новый узел
        
        self._size += 1 # Обновляем длину


    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next


    def remove(self, value) -> None:
        current = self.head
        if current is None: # 1. Если список пустой
            return
        if current.value == value: # 2. Если удаляем голову
            self.head = current.next
            self._size -= 1

            # Если список стал пустым, обновляем tail
            if self.head is None:
                self.tail = None

        while current.next is not None: # 3. Если ищем в середине списка
            if current.next.value == value:
                current.next = current.next.next # Если нашли элемент, то меняем его на следующий
                self._size -= 1

                if current.next is None: # Если удалили последний элемет, меняем tail
                    self.tail = current
                return # Выкидывает из списка, когда условие выполнится
            
            current = current.next # Переходим к след. узлу

    def __iter__(self) -> None:
        current = self.head  # Начинаем с головы
        while current is not None:  # Пока не дойдём до конца
            yield current.value     # Возвращаем значение текущего узла
            current = current.next  # Переходим к следующему узлу

    def __len__(self) -> int:
        return self._size
    
    def is_empty(self) -> bool:
        """Проверка, пуст ли список - O(1)"""
        return self._size == 0

    def __repr__(self) -> str:
        values = list(self)
        return f"SinglyLinkedList({values})"
```
![alt text](/images/lab10/3.png)
