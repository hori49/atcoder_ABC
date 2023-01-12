# AtCoder ABC Contest #183 C
# itertoolsを使う

"""
[ 問題文 ]
N 個の都市があります。都市 i から都市 j へ移動するには T_(i,j)の時間がかかります。

都市 1 を出発し、全ての都市をちょうど 1 度ずつ訪問してから都市 1 に戻るような経路のうち、
移動時間の合計がちょうど K になるようなものはいくつありますか？

[ 制約 ]
2 ≤ N ≤ 8
i != j のとき 1 ≤ T_(i,j) ≤ 10^8
T_(i,i) = 0
T_(i,j) = T_(j,i)
1 ≤ K ≤ 10^9
入力はすべて整数

[ 入力 ]
入力は以下の形式で標準入力から与えられる。
N K
T_(1,1) … T_(1,N)
⋮
T_(N,1) … T_(N,N)

[ 出力 ]
答えを整数で出力せよ。
"""

import itertools

def main():
    N, K = map(int, input().split())
    graph_lst = []
    for _ in range(N):
        tmp_lst = list(map(int, input().split()))
        graph_lst.append(tmp_lst)

    ans = 0

    city_lst = []
    for i in range(2, N+1):
        city_lst.append(i)

    # 2からNまでのすべての組み合わせをリストに追加する。
    all_route = list(itertools.permutations(city_lst, N-1))

    for i in range(len(all_route)):
        curr_city = 1
        time_total = 0
        for j in range(N-1):
            next_city = int(all_route[i][j])
            time_total += int(graph_lst[curr_city - 1][next_city - 1])
            curr_city = next_city
        time_total += int(graph_lst[curr_city - 1][0])  # ルートの最後の都市から都市１に戻る為に時間を追加する。
        if (time_total == K):
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()


"""
[ 入力例 1 ]
4 330
0 1 10 100
1 0 20 200
10 20 0 300
100 200 300 0
[ 出力例 1 ]
2

都市 1 を出発し、全ての都市をちょうど 1 度ずつ訪問してから都市 1 に戻るような経路は、
    1→2→3→4→1
    1→2→4→3→1
    1→3→2→4→1
    1→3→4→2→1
    1→4→2→3→1
    1→4→3→2→1
の 6 通りがあります。それぞれの移動時間は、421,511,330,511,330,421 なので、ちょうど 330 であるようなものは 2 通りです。

[ 入力例 2 ]
5 5
0 1 1 1 1
1 0 1 1 1
1 1 0 1 1
1 1 1 0 1
1 1 1 1 0
[ 出力例 2 ]
24

どのような順で都市を訪問しても、移動時間の合計は 5 になります。
"""
