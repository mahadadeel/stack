##Stack Data Structure

#Main Stack Class
class Stack():
    def __init__(self, length):
        #When initiating, user defines the length.
        #The head pointer is set at -1 (i.e. not pointing to anything, index beginning as one)
        #The stack is set as a series of None objects in a list the length the user gave
        self._length = length
        self._head = -1
        self._stack = [None]*length
    def push(self, *args):
        #Push - Add value to Stack (First In)
        #Arguments are taken as a tuple of any length and are processed one at a time
        for i in args:
            if not self.isFull():
                #The stack is checked if it is full. If it isn't, the value is added to the stack and the head is updated.
                self._head += 1
                self._stack[self._head] = i
            else:
                #Otherwise, if the list is full, the loop breaks and no more values are taken from the arguments.
                break
    def pop(self):
        #Pull - Take value from Stack (Last Out)
        if self.isEmpty():
            #If the stack is empty, None is returned
            return None
        else:
            #If the list is not empty, the value being pointed to is returned and the pointer shifts back one
            #To emulate a real Stack, this value is not removed, however would be overwritten when pushing
            self._poppedValue = self._stack[self._head]
            self._head -= 1
            return self._poppedValue
    def peek(self):
        #Peek - Display value on top of Stack
        if not self.isEmpty():
            #If the Stack is not empty, the value returned is given, i.e. where the pointer indicates
            return self._stack[self._head]
        else:
            #If the Stack is empty however, none is returned
            return None
    def isFull(self):
        return self._head == (self._length-1) #If the pointer is the same as the length (minus one) of the stack then it is full. If not, it isn't full.
    def isEmpty(self):
        return self._head == -1 #If the pointer is -1, i.e. the head is not pointing to anything, the stack is empty.

#Testing Playground with a Stack of Length 5 named 's'
s = Stack(5)
print("Created Stack of Length 5: No values")
print("empty",s.isEmpty())
s.push(1, 2, 3)
print("Added values 1, 2 and 3")
print("peak",s.peek())
print("empty",s.isEmpty())
print("popped",s.pop())
print("popped",s.pop())
print("peak",s.peek())
print("Added values 4, 5, 6, 7")
s.push(4, 5, 6, 7)
print("peek",s.peek())
print("full",s.isFull())
