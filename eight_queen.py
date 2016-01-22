# -*- coding:utf-8 -*-

from time import clock

def admissible(cols):
    """
    リスト cols を受け取り，i行目の cols[i] 列にクイーンが配置されているとき，
    すべての列と対角線について，クイーンが2個以上配置されていないか確認をして，
    OKならTrue，ダメならFalseを返す
    """
    N = len(cols) # N x N chess board

    for i in range(N-1):
        for j in range(i+1, N):
            # i行とj行(i < j)を確認
            if (cols[i] == cols[j]) or (abs(cols[i] - cols[j]) == j - i):
                # 同じ列，または同じ対角線上に配置されていればFalse
                return False

    # ここまでのチェックを全部通過したならTrue
    return True


def solve(N):

    def _solve(r, cols):
        ans = 0
        if r == N:
            if admissible(cols):
                print(cols)
                ans += 1
        else:
            for i in range(N):
                cols[r] = i
                ans += _solve(r+1, cols)
        return ans

    cols = [0] * N # initialize
    return _solve(0, cols)


# 時間計測用(begin)
t1 = clock()

# メインルーチン
cnt = solve(8)
print("The answer is --> {}".format(cnt))
# 時間計測用(end)
t2 = clock()

# ここまでにかかった時間の表示
print("time --> {}".format(t2-t1))
