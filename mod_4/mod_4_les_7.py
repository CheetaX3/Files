# В этом классе мы будем использовать список для хранения элементов очереди
class Queue:
    def __init__(self):
        self.items = []

    # Метод is_empty, который будет проверять, есть ли элементы в очереди
    def is_empty(self):
        return len(self.items) == 0

    # Метод enqueue, который будет добавлять элемент в очередь. 
    # Мы будем добавлять элемент в конец списка
    def enqueue(self, item):
        self.items.append(item)

    # Метод dequeue, который будет удалять и возвращать элемент из вершины очереди. 
    # При этом проверим, не отсутствуют ли элементы в очереди перед попыткой извлечения элемента
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("В очереди нет элементов.")

    # метод size, который будет возвращать количество элементов в очереди
    def size(self):
        return len(self.items)

# Пример использования:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Размер очереди:", queue.size())  # Размер очереди: 3

while not queue.is_empty():
    item = queue.dequeue()
    print("Извлечен элемент:", item)