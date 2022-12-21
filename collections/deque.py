from collections import deque

ticket_queue = deque()
print(ticket_queue)

# People arrive to the queue
ticket_queue.append("Jane")
ticket_queue.append("John")
ticket_queue.append("Linda")

print(ticket_queue)

# People bought their tickets
print(ticket_queue.popleft())
print(ticket_queue.popleft())
print(ticket_queue.popleft())

# No people on the queue
# ticket_queue.popleft()

recent_files = deque(["core.py", "README.md", "__init__.py"], maxlen=3)

recent_files.appendleft("database.py")
print(recent_files)

recent_files.appendleft("requirements.txt")
print(recent_files)

# Use different iterables to create deques
print(deque((1, 2, 3, 4)))
print(deque([1, 2, 3, 4]))

print(deque("abcd"))

# Unlike lists, deque doesn't support .pop() with arbitrary indices
# deque("abcd").pop(2)

# Extend an existing deque
numbers = deque([1, 2])
numbers.extend([3, 4, 5])
print(numbers)

numbers.extendleft([-1, -2, -3, -4, -5])
print(numbers)

# Insert an item at a given position
numbers.insert(5, 0)
print(numbers)

ordinals = deque(["first", "second", "third"])
ordinals.rotate()
print(ordinals)

ordinals.rotate(2)
print(ordinals)

ordinals.rotate(-2)
print(ordinals)

ordinals.rotate(-1)
print(ordinals)

ordinals = deque(["first", "second", "third"])
print(ordinals[1])

print(ordinals[0:2])