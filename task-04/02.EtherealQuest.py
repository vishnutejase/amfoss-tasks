def isStable(vectors):
    full_vector = [0, 0, 0]
    for vector in vectors:
        full_vector[0] += vector[0]
        full_vector[1] += vector[1]
        full_vector[2] += vector[2]
    return full_vector == [0, 0, 0]

n = int(input())
vector = []

for j in range(n):
    x, y, z = map(int, input().split())
    vector.append([x, y, z])

if isStable(vector):
    print("YES")
else:
    print("NO")
