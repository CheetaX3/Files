class Stack:
    OPEN_BRACKETS = ['(', '[', '{']
    CLOSE_BRACKETS = {')': '(', ']': '[', '}': '{'}
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Стек пуст")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Стек пуст")
    
    def is_bracket_sequence_balanced(self, bracket_sequence):
        balanced = True
        for bracket in bracket_sequence:
            if bracket in Stack.OPEN_BRACKETS:
                self.push(bracket)
            elif bracket in Stack.CLOSE_BRACKETS:
                if not self.is_empty() and self.peek() == Stack.CLOSE_BRACKETS[bracket]:
                    self.pop()
                else:
                    balanced = False
                    break
            else:
                balanced = False
                break
        
        if balanced and self.is_empty():
            result = "Сбалансированная скобочная последовательность"
        else:
            result = "Несбалансированная скобочная последовательность"

        return result

my_stack = Stack()
bracket_sequence = ['[', '(', '{', '(', ')', '}', ')', ']', '[', ']', ']']
print(my_stack.is_bracket_sequence_balanced(bracket_sequence))