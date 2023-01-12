# AtCoder ABC Contest #177 C
# 数列の和を求める問題は具体例で考え。計算量を減らせるように数式を変形する。

"""
[ 問題文 ]
N 個の整数 A_1, …, A_N が与えられます。

1 ≤ i < j ≤ N を満たす全ての組 (i,j) についての
A_i * A_j の和を mod(10^9 + 7) で求めてください。

[ 制約 ]
2 ≤ N ≤ 2 * 10^5
0 ≤ A_i ≤ 10^9
入力は全て整数

[ 入力 ]
入力は以下の形式で標準入力から与えられる。
N
A_1 … A_N

[ 出力 ]
 N-1        N
∑          ∑        A_i A_j を mod(10^9+7) で出力せよ。
 i=1        j=i+1
"""

def main():
    mod = (10**9) + 7
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    y = 0
    for i in range(1, N):
        y += A[i]
    for i in range(N-1):
        x = A[i]
        sum += (x * y)
        sum %= mod
        y -= A[i+1]
    print(sum)


if __name__ == '__main__':
    main()


"""
[ 入力例 1 ]
3
1 2 3
[ 出力例 1 ]
11

1*2+1*3+2*3=11 です。

[ 入力例 2 ]
4
141421356 17320508 22360679 244949
[ 出力例 2 ]
437235829
"""