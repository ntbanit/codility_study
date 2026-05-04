# https://codility.com/media/train/14-GreedyAlgorithms.pdf
def greedyCanoeistB(W, k):
    canoes = 0
    j = 0
    i = len(W)- 1
    while (i >= j):
        if W[i] + W[j] <= k:
            j += 1;
        canoes += 1;
        i-= 1
    return canoes


print(greedyCanoeistB([20, 30, 80, 90], 100))
print(greedyCanoeistB([70, 80, 90], 100))
print(greedyCanoeistB([10, 20, 30, 40, 50, 60], 100))
print(greedyCanoeistB([10, 40, 60, 70, 90], 100))