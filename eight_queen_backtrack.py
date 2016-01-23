# -*- coding:utf-8 -*-
# N-クイーン バックトラック版

def solve(N):
    cnt = 0

    def put(board, r, c):
        nonlocal N
        if r < N:
            for row in range(r+1, N):
                # 同じ列の下の行に，クイーンの利き数を+1
                board[row][c] += 1

                # 下の行の各対角線上に，クイーンの利き数を+1
                d = row - r
                if (c+d < N):
                    board[row][c + d] += 1
                if (c-d >= 0):
                    board[row][c - d] += 1

    def remove(board, r, c):
        nonlocal N
        if r < N:
            for row in range(r+1, N):
                # 同じ列の下の行から，クイーンの利き数を-1
                board[row][c] += - 1

                # 下の行の各対角線上から，クイーンの利き数を-1
                d = row - r;
                if (c+d < N):
                   board[row][c + d] += - 1
                if (c-d >= 0):
                   board[row][c - d] += - 1


    def _solve(r, board):
        ans = 0
        nonlocal N

        if r >= N:
            ans = 1
        else:
            for col in range(N):
                if board[r][col] == 0: # まだ利きがないマス
                    put(board, r, col)
                    ans += _solve(r+1, board)
                    remove(board, r, col)

        return ans

    board = [[0 for i in range(N)] for j in range(N)] # initialize
    return _solve(0, board)

# main
print(solve(8))
