class Stack:
    def __init__(self):
        """
        Реализация структуры стэк, в который элемент кладутся
        "наверх" и берутся из "верха"
        """
        self.sp = []
        self.stack_min = []

    def push(self, x: int) -> None:
        self.sp.append(x)
        if len(self.stack_min) == 0 or x <= self.stack_min[-1]:
            self.stack_min.append(x)

    def is_empty(self) -> bool:
        if len(self.sp) == 0:
            return True
        return False

    def pop(self) -> int:
        if not self.is_empty():
            res = self.sp.pop()
            if res == self.stack_min[-1]:
                self.stack_min.pop()
            return res
        raise IndexError("Pop from empty stack")

    def peek(self) -> int:
        if not self.is_empty():
            return self.sp[-1]
        raise IndexError("Peek from empty stack")

    def min(self) -> int:
        if len(self.stack_min) > 0:
            return self.stack_min[-1]
        else:
            raise IndexError("Min from empty stack")
