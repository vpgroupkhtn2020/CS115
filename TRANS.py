n, m, k = map(int, input().split())
d = [int(-1) for i in range(n + 5)]
a = [[] for j in range(n + 5)]
for i in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)


def bfs(x):
    global a, d
    queue = []
    queue.append(x)
    d[x] = 0
    while queue:
        u = queue.pop(0)
        for v in a[u]:
            if d[v] != -1:
                continue
            d[v] = d[u] + 1
            queue.append(v)


bfs(1)
res = (int)(1e18)
l, r = 1, (int)(1e18)
while l <= r:
    m = (l + r) // 2
    sum = 0
    for i in range(2, n + 1):
        val = m // d[i]
        sum += val
    if sum >= k:
        res = m
        r = m - 1
    else:
        l = m + 1
print(res)