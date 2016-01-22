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


# 時間計測用(begin)
t1 = clock()

# メインルーチン
cnt = 0

for i1 in range(8):
    for i2 in range(8):
        for i3 in range(8):
            for i4 in range(8):
                for i5 in range(8):
                    for i6 in range(8):
                        for i7 in range(8):
                            for i8 in range(8):
                                if admissible([i1,i2,i3,i4,i5,i6,i7,i8]):
                                    cnt += 1
                                    print(cnt,": ",i1,i2,i3,i4,i5,i6,i7,i8)

# 時間計測用(end)
t2 = clock()

# ここまでにかかった時間の表示
print("time --> {}".format(t2-t1))
