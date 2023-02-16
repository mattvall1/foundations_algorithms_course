# Get support for 'deque' datatype - this is an object
from collections import deque
# Setup queue variable
queue = deque()

# Add items to queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

# Print the queue
print("Queue: ", queue)

# Pop item from fromt of queue
x = queue.popleft()
print("Popped left item: ", x)
print("Queue: ", queue)