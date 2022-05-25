import sys
input = lambda : sys.stdin.readline().strip()

n, m = map(int, input().split())
x, y, d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[0] * m for _ in range(n)]
visited[x][y] = 1


def turn():
    global d
    d -= 1
    if d == -1:
        d = 3


turns = 0
count = 1
while True:
    turn()
    nx = x + dx[d]
    ny = y + dy[d]
    # 해당 위치가 육지이고 방문하지 않았을 경우
    if matrix[nx][ny] == 0 and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turns = 0
        continue
    else:
        turns += 1

    if turns == 4:   # 모든 방향으로 다 돌았을 경우
        nx = x - dx[d]
        ny = y - dy[d]
        if matrix[nx][ny] == 0:    # 뒤로 돌아갈 수 있는 경우
            x, y = nx, ny
        else:
            break
        turns = 0

print(count)