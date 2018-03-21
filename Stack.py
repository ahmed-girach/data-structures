#!usr/bin/python3

'''
    Stack implementation
'''


class Stack(object):

    def __init__(self, size):
        self.items = []
        self.size = size

    def push(self, element):
        if len(self.items) < self.size:
            self.items.append(element)
            print(element, "was pushed to Stack!")
        else:
            print("Stack Overflow!")

    def pop(self):
        if self.items:
            element = self.items.pop()
            print(element, "was popped from Stack!")
        else:
            print("Stack Underflow!")

    def traverse(self):
        print("Stack => ", end="")
        print(", ".join([str(elem) for elem in self.items]))


if __name__ == '__main__':
    n = int(input("Size of the stack?"))

    s = Stack(n)

    s.push(5)
    s.push(10)
    s.push(14)
    s.push(23)
    s.traverse()
    s.pop()
    s.traverse()
    s.pop()
    s.pop()
