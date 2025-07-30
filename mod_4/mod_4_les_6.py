class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Стек пуст")

    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

rpn = '12-34+*/'
stack = Stack()
error_occurred = False

for i in rpn:
    try:
        if i in '0123456789':
            stack.push(int(i))
        else:
            if stack.size()  < 2:
                raise ValueError ('Ошибка: недостаточно операндов для операции')
            b = stack.pop()
            a = stack.pop()
            if i == '+':
                stack.push(a + b)
            elif i == '-':
                stack.push(a - b)
            elif i == '*':
                stack.push(a * b)
            elif i == '/':
                stack.push(a / b)
    except ValueError as e:
        print(e)
        error_occurred = True
        break

if not error_occurred and stack.size() == 1:
    print("Результат:", stack.pop())
elif not error_occurred:
    print("Ошибка: выражение некорректно")