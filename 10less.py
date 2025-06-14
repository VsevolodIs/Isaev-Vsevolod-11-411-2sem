#1
# string = '(()))()(((((((())))))))))))))()())))(())))('
# open_count = 0
# removals = 0

# for i in string:
#     if i == '(':
#         open_count += 1

#     else:
#         if open_count > 0:
#             open_count -= 1
#         else:
#             removals += 1

# print(f'Наименьшее необходимое количество для удаления: {open_count + removals}')

#2
class QueueTwoStack:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, a):
        self.stack_in.append(a)

    def dequeue(self):
        if len(self.stack_out) == 0:
            if len(self.stack_in) == 0:
                raise IndexError('Очередь пустая')
            
            while len(self.stack_in) != 0:
                self.stack_out.append(self.stack_in.pop())

        return self.stack_out.pop()
    

queue = QueueTwoStack()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)


print(queue.dequeue())
