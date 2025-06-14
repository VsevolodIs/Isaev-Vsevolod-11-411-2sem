from collections import deque
import time

def join_deque(q1, q2):
    res = deque()

    while q1 and q2:
        if  q1[0] <= q2[0]:
            res.append(q1.popleft())
        else:
            res.append(q2.popleft())
    
    while q1:
        res.append(q1.popleft())
    
    while q2:
        res.append(q2.popleft())

    return res

class QueueTwoStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, value):
        self.stack_in.append(value)

    def dequeue(self):
        if not self.stack_out:
            if not self.stack_in:
                raise IndexError("Очередь пуста")
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()
    
    def peek(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:
            raise IndexError("Очередь пуста")
        return self.stack_out[-1]

    def is_empty(self):
        return not self.stack_in and not self.stack_out

    def __str__(self):
        return str(self.stack_out[::-1] + self.stack_in)
    
def join_twostacks(q1, q2):
    res = QueueTwoStacks()

    while not q1.is_empty() and not q2.is_empty():
        if q1.peek() <= q2.peek():
            res.enqueue(q1.dequeue())
        else:
            res.enqueue(q2.dequeue())

    return res

def test():
    times_deque = []
    for _ in range(10):
        q1 = deque([1, 4, 6, 9])
        q2 = deque([2, 3, 7, 10])
        start = time.perf_counter()
        join_deque(q1, q2)
        end = time.perf_counter()
        times_deque.append(end - start)
    
    times_twostacks = []
    for _ in range(10):
        q1_stack = QueueTwoStacks()
        q2_stack = QueueTwoStacks()
        for x in [1, 4, 6, 9]:
            q1_stack.enqueue(x)
        for x in [2, 3, 7, 10]:
            q2_stack.enqueue(x)
        start = time.perf_counter()
        join_twostacks(q1_stack, q2_stack)
        end = time.perf_counter()
        times_twostacks.append(end - start)
    
    avg_deque = sum(times_deque) / len(times_deque)
    avg_two_stacks = sum(times_twostacks) / len(times_twostacks)

    print(f"Среднее время для deque: {avg_deque:.8f} секунд")
    print(f"Среднее время для очереди на двух стеках: {avg_two_stacks:.8f} секунд")
    
if __name__ == '__main__':
    test()