# AtCoder ABC Contest #193 C
# setを使う

"""
[ 問題文 ]
整数 N が与えられます。 1 以上 N 以下の整数のうち、 2 以上の整数 a,b を用いて
a^b と表せないものはいくつあるでしょうか？

[ 制約 ]
N は整数
1 ≤ N ≤ 10^10

[ 入力 ]
入力は以下の形式で標準入力から与えられる。
N

[ 出力 ]
答えを出力せよ。
"""

import math

def main():
    N = int(input())
    last_num = int(math.sqrt(N))

    # 2 以上の整数 a,b を用いて a^b と表せる数字をsetを用いて集合化する。
    myset = set()
    for i in range(2, last_num + 1):
        j = 2
        while (i ** j <= N):
            myset.add(i ** j)
            j += 1

    # 1 以上 N 以下のすべての整数の集合との差分の数を出力する。
    # print("myset : ", myset)
    print(N - len(myset))

if __name__ == '__main__':
    main()


"""
[ 入力例 1 ]
8
[ 出力例 1 ]
6

4,8 は 2^2 = 4, 2^3 = 8 と、a b の形で表すことができます。
1,2,3,5,6,7 は 2 以上の整数 a,b を用いて a^b と表せないので、答えは 6 です。

[ 入力例 2 ]
100000
[ 出力例 2 ]
99634
"""
