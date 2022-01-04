from sys import stdin
input = lambda: stdin.readline().rstrip()
 
n, mod = map(int, input().split())
g = [[] for i in range(n)]
# dp = {}
for i in range(n - 1):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    g[x].append(y)
    g[y].append(x)
    # dp[x, y] = 0
    # dp[y, x] = 0
 
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)
 
dp = {}
# dp[-1, 0] = 0
# dp[0, -1] = 0
# dp1[v] = dp[p, v]
# dp2[v] = dp[v, p]
# dp1[nv] = dp[v, nv]
# dp2[nv] = dp[nv, v]
# dp1[0] = dp[-1, 0]
# dp2[0] = dp[0, -1]
 
def dfs1(v, p=-1):
    ans_black = 1
    for nv in g[v]:
        if nv == p:
            continue
        dfs1(nv, v)
        ans_black *= dp[v, nv]
        ans_black %= mod
    ans = (ans_black + 1) % mod
    dp[p, v] = ans
 
dfs1(0)
 
def dfs2(v, p=-1):
    # child len
    cl = len(g[v])
    lprod = [1] * (cl + 1)
    rprod = [1] * (cl + 1)
    for i, nv in enumerate(g[v]):
        # lprod[i + 1] = lprod[i] * (dp1[nv] if nv != p else dp2[v]) % mod
        # lprod[i + 1] = lprod[i] * dp[v -> nv(nv==pであっても)] % m
        lprod[i + 1] = lprod[i] * dp[v, nv] % mod
    for i, nv in list(enumerate(g[v]))[::-1]:
        # rprod[i] = rprod[i + 1] * (dp1[nv] if nv != p else dp2[v]) % mod
        rprod[i] = rprod[i + 1] * dp[v, nv] % mod
    for i, nv in enumerate(g[v]):
        if nv == p:
            continue
        # dp2[v]: v -- p 以上
        ansi = lprod[i] * rprod[i + 1] % mod + 1
        ansi %= mod
        # dp2[nv] = product([dp1[nvi] for nvi in g[v] if nvi != p and nvi != nv]) * dp2[v] % m + 1
        dp[nv, v] = ansi
        dfs2(nv, v)
 
dp[0, -1] = 1
dfs2(0)
 
ans = [0] * n
 
def dfs3(v, p=-1):
    ansi = dp[v, p]
    for nv in g[v]:
        if nv == p:
            continue
        ansi *= dp[v, nv]
        ansi %= mod
        dfs3(nv, v)
    ans[v] = ansi
dfs3(0)
 
print(*ans, sep="\n")