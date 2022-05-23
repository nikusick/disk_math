def bridge_count(N, connections, colors):
    count = 0
    for i in range(N):
        for j in range(i, N):
            if int(connections[i][j]) and colors[i] != colors[j]:
                count += 1
    return count


with open("rain_input") as file:
    N = int(file.readline())
    connections = [file.readline().split() for _ in range(N)]
    file.readline()
    colors = file.readline().split()
    print(bridge_count(N, connections, colors))
