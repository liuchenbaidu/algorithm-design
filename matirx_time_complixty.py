"""
### 首先规定一下记号：AMN，表示一个有两个指标，大小是M×N的矩阵A。那么AMNBNL的时间复杂度是O(MNL)。如果我们把乘法的过程用计算机语言表示出来，这一结论就会非常清晰：
"""

C = np.zeros((M, L))
for m in range(M):
    for l in range(L):
        for n in range(N):
            C[m][l] += A[m][n] * B[n][l]
            
 
 # 实验
M = 71
N = 513
L = 4097
for i in range(5):
    m1 = np.random.random((M, N))
    m2 = np.random.random((N, L))
    %timeit m1.dot(m2)
    M *= 4
#高维矩阵（张量）乘法-只对一个轴求和
###在numpy中dot，einsum，tensordot等函数都可以做高维矩阵乘法，这里只研究最常见的tensordot。我们从AMNLBLPQ这样一个例子入手。从理论上分析，AMNLBLPQ的时间复杂度是O(MNLPQ)


# 实验
M = 63
N = 17
L = 255
P = 127
Q = 31
for i in range(5):
    m1 = np.random.random((M, N, L))
    m2 = np.random.random((L, P, Q))
    %timeit np.tensordot(m1, m2, 1)
    M *= 4
    
 #高维矩阵（张量）乘法-对多个轴求和 
 #下面我们再考虑对多个轴求和的情况，这种情况下“数学语言”已经不好给出清晰的描述了。如果想举个例子，也只能啰嗦地说：AMNL和BNLP之间进行双点积contract掉维数为N和L的两个指标。倒是计算机语言还算游刃有余
C = np.zeros((M, P))
for m in range(M):
    for p in range(P):
        for n in range(N):
            for l in range(L):
                C[m][p] += A[m][n][l] * B[n][l][p]
 
 # 实验
 M = 63
N = 31
L = 255
P = 127
for i in range(5):
    m1 = np.random.random((M, N, L))
    m2 = np.random.random((N, L, P))
    %timeit np.tensordot(m1, m2, 2)
    M *= 4
 
