def Calculate(arr, P):
    arr.sort()
    count = 0
    for i in range(len(arr) - 2):
        l = i + 1
        r = len(arr) - 1
        while l < r:
            count += 1
            if arr[i] + arr[l] + arr[r] == P:
                return True, count
            elif arr[i] + arr[l] + arr[r] < P:
                l += 1
            else:
                r -= 1

    return False, count


if __name__ == '__main__':

    print(Calculate([1, 2, 3, 4, 1000000000], 1000000005))


