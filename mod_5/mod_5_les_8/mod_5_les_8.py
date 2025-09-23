import random
from collections import Counter
from collections import namedtuple
from collections import defaultdict
from collections import deque


# Задание 1: Анализ списка чисел с помощью Counter
random_list = random.choices(range(10), k=10)
counter = Counter(random_list)
most_common = counter.most_common(3)

print(random_list)
print(counter)
print(most_common)

# Задание 2: Работа с именованными кортежами
Book = namedtuple('Book', ['title', 'author', 'genre'])
book1 = Book('The Great Gatsby', 'F. Scott Fitzgerald', 'Classic')
book2 = Book('To Kill a Mockingbird', 'Harper Lee', 'Classic')
book3 = Book('1984', 'George Orwell', 'Dystopian')

books = [book1, book2, book3]
for book in books:
    print(f'Книга: {book.title}, автор: {book.author}, жанр: {book.genre}')

# Задание 3: Работа с defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(3)
print(dict(d))

# Задание 4: Использование deque для обработки данных
queue = deque([1, 2, 3])
queue.append(4)
print(queue)
queue.appendleft(0)
print(queue)
queue.pop()
print(queue)
queue.popleft()
print(queue)

# Задание 5: Реализация простой очереди с помощью deque


def append_item(queue, item):
    queue.append(item)


def appendleft_item(queue, item):
    queue.appendleft(item)


def pop_item(queue):
    if not queue:
        print("Очередь пуста")
        return None
    return queue.pop()


def popleft_item(queue):
    queue.popleft()


queue = deque()
append_item(queue, 10)
append_item(queue, 20)
append_item(queue, 30)
print(queue)
appendleft_item(queue, 1)
print(queue)
pop_item(queue)
print(queue)
popleft_item(queue)
print(queue)
