"""
python 实现栈
"""

class Stack():

    def __init__(self):
        self.items = []

    def pop(self):
        self.items.pop()

    def push(self,item):
        self.items.append(item)

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []



if __name__ == '__main__':

    s= Stack()
    s.push('h')
    s.push('a')

    s.pop()
    print(s.peek())

    print(s.size())

