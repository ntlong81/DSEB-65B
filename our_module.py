def STgcdr(a,b):
    if a<b:
        a,b =b,a 
    if b==0:
        s=1
        t=0
        return a, s, t
    gcd,s1,t1 = STgcdr(b, a%b)
    s = t1
    t = s1-t1*(a//b)
    return gcd,s,t
def gcd(a,b):
    if a<b:
        a,b = b,a
    while b !=0:
        r = a%b
        a = b
        b = r
    return a 
print('Our_module is imported')

## classes
class Stack:
    def __init__(self):
        self.__stack = []
    def push(self, item):
        return self.__stack.append(item)
    def is_empty(self):
        return not bool(self.__stack)
    def size(self):
        return len(self.__stack)
    def pop(self):
        if self.is_empty():
            return "the stack is empty"
        else:
            return self.__stack.pop()
    def peek(self):
        if self.is_empty():
            return "the stack is empty"
        else:
            return self.__stack[-1]
    def __str__(self):
        return str(self.__stack)


class Queue:
    def __init__(self) -> None:
        self.__queue = []
    def enqueue(self,item):
        return self.__queue.insert(0,item)
    def dequeue(self):
        if self.is_empty():
            return 'The queue is empty'
        else:
            return self.__queue.pop()
    def front(self):
        if self.is_empty():
            return 'The queue is empty'
        else:
            return self.__queue[-1]
    def is_empty(self):
        return not bool(self.__queue)
    def __str__(self):
        return str(self.__queue)