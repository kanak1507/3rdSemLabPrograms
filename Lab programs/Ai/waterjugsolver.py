from collections import deque
q = deque([(0, 0)])
visited = set()
while q:
    a, b = q.popleft()
    if (a, b) in visited:
        continue
    visited.add((a, b))
    print(a, b)
    if a == 2 or b == 2:
        print("Goal Reached!")
        break
    # Fill Jug 1
    q.append((4, b))
    # Fill Jug 2
    q.append((a, 3))
    # Empty Jug 1
    q.append((0, b))
    # Empty Jug 2
    q.append((a, 0))
    # Pour Jug 1 into Jug 2
    q.append((a-min(a, 3-b), b+min(a, 3-b)))
    # Pour Jug 2 into Jug 1
    q.append((a+min(b, 4-a), b-min(b, 4-a)))