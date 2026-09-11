"""
is_empty — проверка стека на пустоту. Метод возвращает True или False;
push — добавляет новый элемент на вершину стека. Метод ничего не возвращает;
pop — удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека;
peek — возвращает верхний элемент стека, но не удаляет его. Стек не меняется;
size — возвращает количество элементов в стеке.
"""
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if self.stack:
            return False
        else:
            return True

    def push(self,item):
        self.stack.insert(0,item)

    def pop(self):
        pop_elem = self.stack.pop(0)
        return pop_elem

    def peek(self):
        return self.stack[0]

    def size(self):
        return len(self.stack)
