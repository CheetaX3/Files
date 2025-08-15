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

def evaluate_rpn(rpn):
    stack = Stack()
    rpn = rpn.split()
    for token in rpn:
        if token.isdigit():
            stack.push(int(token))
        else:
            if stack.size() < 2:
                raise ValueError('Ошибка: недостаточно операндов для операции')
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError("Ошибка: деление на ноль")
                stack.push(a / b)
            else:
                raise ValueError(f"Неизвестный оператор: {token}")

    if stack.size() != 1:
        raise ValueError("Ошибка: выражение некорректно")

    return stack.pop()


rpn = '80 1 3 4 + * /'

try:
    result = evaluate_rpn(rpn)
    print("Результат:", result)
except (ValueError, ZeroDivisionError, IndexError) as e:
    print(e)