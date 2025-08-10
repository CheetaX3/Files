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

    def evaluate_rpn(self, rpn):
        rpn = rpn.split()
        for token in rpn:
            if token.isdigit():
                self.push(int(token))
            else:
                if self.size() < 2:
                    raise ValueError('Ошибка: недостаточно операндов для операции')
                b = self.pop()
                a = self.pop()

                if token == '+':
                    self.push(a + b)
                elif token == '-':
                    self.push(a - b)
                elif token == '*':
                    self.push(a * b)
                elif token == '/':
                    if b == 0:
                        raise ZeroDivisionError("Ошибка: деление на ноль")
                    self.push(a / b)
                else:
                    raise ValueError(f"Неизвестный оператор: {token}")

        if self.size() != 1:
            raise ValueError("Ошибка: выражение некорректно")

        return self.pop()


# Пример
rpn = '80 0 3 4 + * /'
stack = Stack()

try:
    result = stack.evaluate_rpn(rpn)
    print("Результат:", result)
except (ValueError, ZeroDivisionError, IndexError) as e:
    print(e)