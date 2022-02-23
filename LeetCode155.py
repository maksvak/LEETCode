'''
LeetCode # 155 - Min Stack
Maksim Vakulenko
2/23/22
'''



class MinStack(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, val: int) -> None:
        self.stack1.append(val)
        if not self.stack2:
            self.stack2.append(val)
        else:
            self.stack2.append(min(self.stack2[-1], val))


    def pop(self) -> None:
        self.stack1.pop()
        self.stack2.pop()

    def top(self) -> int:
        return self.stack1[-1]

    def getMin(self):
        return self.stack2[-1]


