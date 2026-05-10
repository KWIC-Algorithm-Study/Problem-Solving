from collections import deque

def solution(board):
    n = len(board)
    m = len(board[0])

    visited = [[-1] * m for _ in range(n)]

    def bfs(s1, s2):
        dq = deque([(s1, s2)])
        visited[s1][s2] = 0

        moves = [(1,0), (-1,0), (0,1), (0,-1)]

        while dq:
            o1, o2 = dq.popleft()

            for m1, m2 in moves:
                t1, t2 = o1, o2

                while True:
                    nt1 = t1 + m1
                    nt2 = t2 + m2

                    if nt1 < 0 or nt1 >= n or nt2 < 0 or nt2 >= m:
                        break
                    if board[nt1][nt2] == 'D':
                        break

                    t1, t2 = nt1, nt2

                if visited[t1][t2] == -1:
                    visited[t1][t2] = visited[o1][o2] + 1
                    dq.append((t1, t2))

                    if board[t1][t2] == "G":
                        return visited[t1][t2]

        return -1

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                return bfs(i, j)