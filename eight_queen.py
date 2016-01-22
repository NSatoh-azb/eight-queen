# -*- coding:utf-8 -*-

from time import clock

def admissible(i1,i2,i3,i4,i5,i6,i7,i8):
    """
    i1 ～ i8 のすべてについて，
    同じ列にないことの確認と，同じ対角線上にないことの確認をして，
    OKならTrue，ダメならFalseを返す
    """
    return (
        (i1 != i2) and (i1 != i3) and (i1 != i4) and (i1 != i5)
    and (i1 != i6) and (i1 != i7) and (i1 != i8)
    and (i2 != i3) and (i2 != i4) and (i2 != i5) and (i2 != i6)
    and (i2 != i7) and (i2 != i8)
    and (i3 != i4) and (i3 != i5) and (i3 != i6) and (i3 != i7)
    and (i3 != i8)
    and (i4 != i5) and (i4 != i6) and (i4 != i7) and (i4 != i8)
    and (i5 != i6) and (i5 != i7) and (i5 != i8)
    and (i6 != i7) and (i6 != i8)
    and (i7 != i8)
    and abs(i1 - i2) != 1 and abs(i1 - i3) != 2 and abs(i1 - i4) != 3
    and abs(i1 - i5) != 4 and abs(i1 - i6) != 5 and abs(i1 - i7) != 6
    and abs(i1 - i8) != 7
    and abs(i2 - i3) != 1 and abs(i2 - i4) != 2 and abs(i2 - i5) != 3
    and abs(i2 - i6) != 4 and abs(i2 - i7) != 5 and abs(i2 - i8) != 6
    and abs(i3 - i4) != 1 and abs(i3 - i5) != 2 and abs(i3 - i6) != 3
    and abs(i3 - i7) != 4 and abs(i3 - i8) != 5
    and abs(i4 - i5) != 1 and abs(i4 - i6) != 2 and abs(i4 - i7) != 3
    and abs(i4 - i8) != 4
    and abs(i5 - i6) != 1 and abs(i5 - i7) != 2 and abs(i5 - i8) != 3
    and abs(i6 - i7) != 1 and abs(i6 - i8) != 2
    and abs(i7 - i8) != 1
    )



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
                                if admissible(i1,i2,i3,i4,i5,i6,i7,i8):
                                    cnt += 1
                                    print(cnt,": ",i1,i2,i3,i4,i5,i6,i7,i8)

# 時間計測用(end)
t2 = clock()

# ここまでにかかった時間の表示
print("time --> {}".format(t2-t1))
