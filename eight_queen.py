# -*- coding:utf-8 -*-


def admissible(i1,i2,i3,i4,i5,i6,i7,i8):
    """
    i1 ～ i8 のすべてについて，
    同じ列にないことの確認と，同じ対角線上にないことの確認をして，
    OKならTrue，ダメならFalseを返す
    """
    pass


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
