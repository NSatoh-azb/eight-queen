# -*- coding:utf-8 -*-
# N-クイーン バックトラック版

def solve(N):
    cnt = 0

    def put(board, r, c):
        pass

    def remove(board, r, c):
        pass

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
