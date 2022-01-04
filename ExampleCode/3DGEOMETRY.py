def dist(A, B):
    return ((A[0] - B[0])**2 + (A[1] - B[1])**2 + (A[2] - B[2])**2)**0.5

n_test = (int)(input())
for i in range(n_test):
    xA, yA, zA, xB, yB, zB, xC, yC, zC = map(float,input().split())
    A = [xA, yA, zA]
    B = [xB, yB, zB]
    C = [xC, yC, zC]
    dAB = dist(A, B)
    dBC = dist(B, C)
    dAC = dist(C, A)
    p = (dAB + dBC + dAC) / 2
    S = (p*(p-dAB)*(p-dBC)*(p-dAC))**0.5
    d = 2 * S / dBC
    print("{:.2f}".format(d))
