class Fibonacci:
    def __init__(self):
        pass

    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)
