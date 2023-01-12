# AtCoder ABC Contest #181 C
# 二次元平面上で3点が同一直線上にあるか判定する。

"""
[ 問題文 ]
無限に広い 2 次元平面の上に N 個の点があります。
i 番目の点は (x_i, y_i) にあります。
N 個の点の中の相異なる 3 点であって、同一直線上にあるものは存在するでしょうか？

[ 制約 ]
入力はすべて整数
3 ≤ N ≤ 10^2
|x_i|, |y_i| ≤ 10^3
i != j ならば (x_i, y_i) != (x_j, y_j)

[ 入力 ]
入力は以下の形式で標準入力から与えられる。
N
x_1 y_1
⋮
x_N y_N
"""

import itertools
import math

def main():
    N = int(input())
    lst_xy = []
    for _ in range(N):
        Xi, Yi = map(int, input().split())
        lst_xy.append([Xi, Yi])

    lst_comb = []
    for pair in itertools.combinations(lst_xy, 3):
        lst_comb.append(list(pair))

    for i in range(len(lst_comb)):
        x1 = lst_comb[i][0][0]
        y1 = lst_comb[i][0][1]
        x2 = lst_comb[i][1][0]
        y2 = lst_comb[i][1][1]
        x3 = lst_comb[i][2][0]
        y3 = lst_comb[i][2][1]
        # 二次元平面上に存在する３つの点が一直線上に存在するための条件
        # --> |AB| + |AC| = |BC| or |AB| + |BC| = |AC| or |BC| + |AC| = |AB| のどれかの条件を満たす。
        AB = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
        AC = math.sqrt(((x3-x1)**2) + ((y3-y1)**2))
        BC = math.sqrt(((x3-x2)**2) + ((y3-y2)**2))

        if ((abs(AB + AC - BC) < 0.0000000001) or (abs(AB + BC - AC) < 0.0000000001) or (abs(AC + BC - AB) < 0.0000000001)):
            print("Yes")
            exit()

    print("No")

if __name__ == '__main__':
    main()

"""
[ 入力例 1 ]
4
0 1
0 2
0 3
1 1
[ 出力例 1 ]
Yes

(0,1),(0,2),(0,3) の 3 点は直線 x=0 上にあります。

[ 入力例 2 ]
14
5 5
0 1
2 5
8 0
2 1
0 0
3 6
8 6
5 9
7 9
3 4
9 2
9 8
7 2
[ 出力例 2 ]
No

[ 入力例 3 ]
9
8 2
2 3
1 3
3 7
1 0
8 8
5 6
9 7
0 1
[ 出力例 3 ]
Yes
"""
