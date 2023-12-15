def robot_route(m, n):
    result = []
    for i in range(m):
        for k in range(n):
            if i % 2 == 0:
                result.append(i*n+k+1)
            else:
                result.append(i*n+n-k)
    return result

def route(seed_list):
    m = len(seed_list)
    if m == 0:
        return []
    n = len(seed_list[0])
    matrix = [[0 for _ in range(n)] for _ in range(m)]
    order = []

    for i in range(m):
        if i % 2 == 0:
            for j in range(n):
                matrix[i][j] = seed_list[i][j]
                order.append(seed_list[i][j])
        else:
            for j in range(n-1, -1, -1):
                matrix[i][j] = seed_list[i][n - 1 - j]
                order.append(seed_list[i][j])
    return order


if __name__ == "__main__":
    arr = [[1, 3, 7], [4, 2, 5], [1, 3, 8]]
    print(route(arr))



