# https://app.codility.com/programmers/lessons/6-sorting/number_of_disc_intersections/
def solution(A):
    if not A :
        return 0
    intervals = []
    N = len(A)
    for i in range(N) :
        intervals.append((i - A[i], i + A[i]))
    intervals.sort(key= lambda x: x[0])
    # print(intervals)
    def binary_search(i, end):
        # find the largest j that start[j] <= end[i] return j - i
        output = 0
        left, right = i + 1, N - 1
        while left <= right :
            mid = (left + right) // 2 
            if intervals[mid][0] <= end :
                left = mid + 1
                output = mid - i
            else :
                right = mid - 1
        return output

    count = 0
    for i in range(N) :
        count += binary_search(i, intervals[i][1])
        if count > 10**7 :
            return -1
    return count