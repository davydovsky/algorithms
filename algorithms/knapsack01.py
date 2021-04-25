def knapsack(P, W, K):
    n = len(P)
    F = [[0] * (K + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        for k in range(1, K + 1):
            if k >= W[i]:
                F[i][k] = max(F[i - 1][k], F[i - 1][k - W[i]] + P[i])
            else:
                F[i][k] = F[i - 1][k]

    k = K
    ans = []
    for i in range(n, 0, -1):
        if F[i][k] != F[i - 1][k]:
            ans.append(i)
            k -= W[i]

    return ans


if __name__ == '__main__':
    print(knapsack([0, 1, 6, 4, 7, 6], [0, 3, 4, 5, 8, 9], 13))
