# AtCoder ABC Contest #186 C
# 10進数からN進数への変換

"""
[ 問題文 ]
高橋君は 7 が嫌いです。
1 以上 N 以下の整数のうち、10 進法で表しても 8 進法で表しても 7 を含まないような数はいくつありますか？

[ 制約 ]
1 ≤ N ≤ 10^5
N は整数である。

[ 入力 ]
入力は以下の形式で標準入力から与えられる。
N
"""

def main():
    N = int(input())
    cnt = 0  # This variable counts the total numbers which do not contain '7'

    for i in range(1, N+1):
        str_i = str(i)
        flag10 = True
        flag8 = True

        for j in range(len(str_i)):
            if (str_i[j] == '7'):
                flag10 = False
        if (flag10):
            str_i = str(oct(i))
            for k in range(len(str_i)):
                if (str_i[k] == '7'):
                    flag8 = False

        if (flag10 and flag8):
            cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()

"""
入力例 1
20
出力例 1
17

[出力例 1 解説]
1 以上 20 以下の整数のうち、10 進法で表したときに 7 を含む数は 7,17、8 進法で表したときに 7 を含む数は 7,15 です。
よって、7,15,17 以外の 17 個の数が条件を満たします。

入力例 2
100000

出力例 2
30555
"""
