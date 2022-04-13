#------------------------連結問題--------------------------------
# 縦に H マス、横に W マスの長さの二次元グリッドが与えられます。
# それぞれのセルには、正負両方の値をとる整数が与えられます。
# 0 以上の整数が書かれた整数のみからなるセルをすべて選択したとき、
# 連結成分がいくつできるかを求めてください。ただし、セルの集合が連結
# であるとは、セル集合内のある一つのセルから、上下左右に繋がっている
# 集合内のセルを辿ることで、集合内の全てのセルを辿れることを指します。
# 例えば、下の図では、黒いセルの集合は、左の 2 つの例では連結であり、
# 右の 2 つの例では連結ではありません。

import queue
H,W = map(int,input().split())
g = [[int(x) for x in input().split()] for _ in range(W)]
# print(g)

list = []

cell_num = 0
choice = [[False for _ in range(H)] for _ in range(W)]
for i in range(H):
    for j in range(W):
        if g[i][j]>=0:

            choice[i][j] = True
            list.append([i,j])
# print(list,choice)


kk=[]
di = [-1, 1, 0, 0]
dj = [0, 0, 1, -1]

while True:
    if len(list)==0:
        break
    e =list[-1][0]
    f =list[-1][1]
    q = queue.Queue()
    choice[e][f]=False
    q.put([e,f])
    print("e,f",[e,f])
    g_num = []
    while not q.empty():
        i, j = q.get()
        # print("i,j",[i,j])
        list.remove([i,j])
        g_num.append([i,j])
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if ni in range(H) and nj in range(W) and choice[ni][nj] == True:
                choice[ni][nj] = False
                q.put([ni, nj])
    # print(g_num)

    kk.append(g_num)

print(len(kk))
print(kk)