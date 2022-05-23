def best_route(N, squares):
    min_len = 3000
    for i in range(N):
        for j in range(N):
            if i != j:
                for k in range(N):
                    if k != j and k != i:
                        min_len = min(squares[i][j] + squares[j][k] + squares[i][k], min_len)

    print(min_len)


with open("bullying_input") as file:
    N = int(file.readline())
    squares = [list(map(int, file.readline().split())) for _ in range(N)]
    best_route(N, squares)
