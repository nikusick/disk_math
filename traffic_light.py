def traffic_count(tunnels, N):
    for i in range(1, N + 1):
        count = tunnels.count(str(i))
        print(count, end=' ')


with open("traffic_input") as file:
    N, M = file.readline().split()
    N, M = int(N), int(M)
    tunnels = file.read().split()
    traffic_count(tunnels, N)

