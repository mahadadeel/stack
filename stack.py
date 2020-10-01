##Stack Data Structure

class Stack():
    def __init__(self, length):
        self._length = length
        self._head = -1
        self._stack = [None]*length
    def push(self, *args):
        for i in args:
            if not self.isFull():
                self._head += 1
                self._stack[self._head] = i
            else:
                print("Head of Stack reached")
                break
    def pop(self):
        if self.isEmpty():
            return None
        else:
            self._poppedValue = self._stack[self._head]
            self._stack[self._head] = None
            self._head -= 1
            return self._poppedValue
    def peek(self):
        if not self.isEmpty():
            return self._stack[self._head]
        else:
            return None
    def isFull(self):
        return self._head == self._length
    def isEmpty(self):
        return self._head == -1

s = Stack(5)
s.push(1, 2, 3)
print("peak",s.peek())
s.push(4, 5)
print("peek",s.peek())
s.pop()
print("peek after popped",s.peek())
