def road_count(N, roads):
    count = 0
    for i in range(0, N):
        for j in range(i, N):
            count += int(roads[i][j])
    return count


with open("roads_input") as file:
    N = int(file.readline())
    roads = [file.readline().split() for _ in range(N)]
    print(road_count(N, roads))
