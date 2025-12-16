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
    
    
if __name__ == "__main__":

   test = SinglyLinkedList()
   test.append(1)
   test.append(2)
   test.prepend(0)
   test.prepend('hello!')
   test.append(4)
   print(f'\nИмеющийся список:')
   print(test, '\n')
   print(f'Вставляем 3 на 4 место:')
   test.insert(4, 3)
   print(test, '\n')
   print(f'Удаляем 1 элемент:')
   test.remove('hello!')
   print(test, '\n')
   print(f'Количество элементов:')
   print(test.__len__(), '\n')