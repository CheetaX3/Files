# В этом классе мы будем использовать список для хранения элементов стека
class Stack:
    def __init__(self):
        self.items = []

# Метод is_empty, который будет проверять, пуст ли стек
    def is_empty(self):
        return len(self.items) == 0

# Метод push, который будет добавлять элемент в стек. 
# Мы будем добавлять элемент в конец списка
    def push(self, item):
        self.items.append(item)

# Метод pop, который будет удалять и возвращать элемент из вершины стека. 
# При этом проверим, не пуст ли стек перед попыткой извлечения элемента
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Стек пуст")

# Метод peek, который будет возвращать элемент из вершины стека без его удаления. 
# Также проверим, не пуст ли стек перед попыткой просмотра элемента
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Стек пуст")

# метод size, который будет возвращать количество элементов в стеке
    def size(self):
        return len(self.items)

# Создаем экземпляр стека
my_stack = Stack()

# Добавляем элементы в стек
my_stack.push(5)
my_stack.push(10)
my_stack.push(15)

# Просматриваем вершину стека
print("Вершина стека:", my_stack.peek())

# Удаляем элемент из стека
my_stack.pop()

# Проверяем, пуст ли стек
print("Стек пуст?", my_stack.is_empty())

# Выводим размер стека
print("Размер стека:", my_stack.size())