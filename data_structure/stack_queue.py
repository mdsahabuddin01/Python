
from collections import deque
my_deque = deque()

for i in range(0, 10):
    my_deque.append(i)

queue = deque()
print("First in first out")
for i in range(len(my_deque)):
    my_deque.popleft()
    print(my_deque)
    

print("Last in last out")

stack = deque()

for i in range(0,5):
    stack.appendleft(i)
    print(stack)

print("Removing element from last in")
for i in range(len(stack)):
    stack.popleft()
    print(stack)

