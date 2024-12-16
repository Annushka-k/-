from collections import deque

hash = [[], [], [], [], []]
keys = ['sdf', 'fsdw', 'sad', 'sdf']
for j in keys:
    x = len(j) % 5
    if hash[x] == []:
        hash[x] = deque()
    if j not in hash[x]:
        hash[x].append(j)
print(hash)