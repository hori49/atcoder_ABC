# AtCoder ABC Contest #192 C

"""
[ 問題文 ]
0 以上の整数 x に対して、g_1(x), g_2(x), f(x)を次のように定めます。
g_1(x) = x を十進法で表したときの各桁の数字を大きい順に並び替えてできる整数
g_2(x) = x を十進法で表したときの各桁の数字を小さい順に並び替えてできる整数
f(x) = g_1(x) - g_2(x)
例えば g_1(314) = 431, g_2(3021) = 123, f(271) = 721 - 127 = 594 です。
先頭の余分な 0 は無視されることに注意してください。

整数 N,K が与えられるので、a_0 = N, a_(i+1) = f(a_i) (i≥0) で定まる数列の a_K を求めてください。

[ 制約 ]
0 ≤ N ≤ 10^9
0 ≤ K ≤ 10^5
入力は全て整数

[ 入力 ]
入力は以下の形式で標準入力から与えられる。
N K
"""

def main():
    N, K = map(int, input().split())
    ai = N  # a_i (a_0 = N)

    # a_1 = f(N) = g_1(N) - g_2(N)
    # a_2 = f(a_1) = g_1(a_1) - g_2(a_1)
    for i in range(1, K+1):
        str_g1 = str(ai)
        lst_g1 = []
        str_g2 = str(ai)
        lst_g2 = []
        str_len = len(str_g1)
        for j in range(str_len):
            lst_g1.append(str_g1[j])
            lst_g2.append(str_g2[j])

        lst_g1.sort(reverse=True)
        lst_g2.sort()

        str_g1 = "".join(lst_g1)
        int_g1 = int(str_g1)

        str_g2 = "".join(lst_g2)
        int_g2 = int(str_g2)  # Leading 0 will be deleted automatically.

        fi = int_g1 - int_g2

        ai = fi

    print(ai)


if __name__ == '__main__':
    main()

"""
入力例 1
314 2
出力例 1
693

入力例 2
1000000000 100

出力例 2
0

入力例 3
6174 100000

出力例 3
6174
"""
