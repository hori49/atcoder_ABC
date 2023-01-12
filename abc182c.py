# AtCoder ABC Contest #182 C
# 余りは足し算、引き算、掛け算ができる

"""
[ 問題文 ]
各桁に 0 が出現しないような正の整数 N が与えられます。
N の桁数を k とします。N の桁を 0 個以上 k 個未満消して、残った桁をそのままの順序で結合することで 3 の倍数を作りたいです。
3 の倍数を作ることができるか判定し、作ることができるなら作るのに必要な最少の消す桁数を求めてください。

[ 制約 ]
1 ≤ N < 10^18
N は各桁に 0 が出現しない整数

[ 入力 ]
入力は以下の形式で標準入力から与えられる。
N
"""

import itertools

def main():
    N = int(input())
    N_str = str(N)
    N_list = []
    K = len(N_str)
    sum = 0

    for i in range(K):
        sum += int(N_str[i])
        N_list.append(N_str[i])

    if (sum % 3 == 0):
        print(0)
        exit()

    for i in range(1, K):
        lst_comb = []
        lst_comb_str = []
        for pair in itertools.combinations(N_list, K - i):
            lst_comb.append(list(pair))

        for x in range(len(lst_comb)):
            comb_str = "".join(lst_comb[x])
            lst_comb_str.append(comb_str)

        for j in range(len(lst_comb_str)):
            sum = 0
            for k in range(len(lst_comb_str[0])):
                sum += int(lst_comb_str[j][k])
            if (sum % 3 == 0):
                print(i)
                exit()

    print(-1)


if __name__ == '__main__':
    main()

"""
[ 入力例 1 ]
35
[ 出力例 1 ]
1

5 を消した 3 という数は 3 の倍数です。このとき消した桁数は 1 で最少です。

[ 入力例 2 ]
369
[ 出力例 2 ]
0

1 つも桁を消さなくてもいいことに注意してください。

[ 入力例 3 ]
6227384
[ 出力例 3 ]
1

例えば、 8 を消した 622734 は 3 の倍数です。

[ 入力例 4 ]
11
[ 出力例 4 ]
-1

消す桁数は N の桁数を k として 0 個以上 k 個未満でなければならないため、全部の桁を消すことはできないことに注意してください。
この場合問題文に従って 3 の倍数を作ることは不可能なため -1 を出力します。
"""
