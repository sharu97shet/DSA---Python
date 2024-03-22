class demoqueue:
    def __init__(self):
        self.values=[]

    def enqueue(self, x) :
        self.values.append(x)

    def dequeue(self):
        front=self.values[0]
        self.values=self.values[1:]
        return front
    
q1=demoqueue()   

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)

print(q1.values) 
print(q1.dequeue())
print("after fifo")
print(q1.values)


from collections import deque 

class Queue:
    def __init__(self) -> None:
        print("constructor is called")
        self.values=deque()

    def enterqueue(self, x):
        self.values.appendleft(x)

    def leavequeue(self):
        self.values.pop()

    def size(self):
        return len(self.values)        


q=Queue()
q.enterqueue(
    {
        'name':"arun",
        'movie':"gar"
    }
)
q.enterqueue({
        'name':"anil",
        "movie":"tanu"

    }
)
# q.appendleft(5)
# q.appendleft(15)
# q.appendleft(25)

print(q)
print(q.values)
print(q.size())

# q.pop()
# print(q)
