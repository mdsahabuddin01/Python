from collections import deque

# Create a deque
my_deque = deque()

# Add elements to the back
my_deque.append(1)
my_deque.append(2)

# Add elements to the front
my_deque.appendleft(0)

# Remove elements from the back
last_element = my_deque.pop()

# Remove elements from the front
first_element = my_deque.popleft()

# The deque now contains [1]
print(my_deque)
