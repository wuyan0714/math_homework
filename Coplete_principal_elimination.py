'''完全主元素消去法'''
import numpy as np
#按列选主元
def max(a,k):
    i ,j = np.where(np.abs(a[k:,k:]==np.max(np.abs(a[k:,k:]))))
    ik = i[0]+k
    jk = j[0]+k
    return ik,jk
#第k+1次对第i+1行进行消元
def elimination_line(a,b,k,i):
    m = a[i][k]/a[k][k]
    for j in range(k+1,len(a)):
        a[i][j] = a[i][j] - m*a[k][j]
    a[i][k] = 0
    b[i] = b[i]-m*b[k]
    return a,b
#对于n*n阶矩阵，需要进行n-1次迭代，每次需要从第k+1行到第n行进行消元
def elimination(a,b):
    IZ = np.arange(len(a))
    for k in range(0,len(a)-1):
        ik,jk = max(a,k)
        if a[ik,jk]==0:
            print('此矩阵非奇异')
            return
        if ik!=k:
            a[[ik, k], :] = a[[k, ik], :]
            b[[ik,k]] = b[[k,ik]]
        if jk!=k:
            a[:,[jk,k]] = a[:,[k,jk]]
            IZ[[jk, k]] = IZ[[k, jk]]
        for i in range(k+1,len(a)):
            elimination_line(a,b,k,i)
    return a,b,IZ
def back_to_generation(a,b,IZ):
    y = np.zeros(len(a))
    y[-1] = b[-1]/a[-1][-1]
    for i in range(len(a)-2,-1,-1):
        t = 0
        for j in range(i+1,len(a)):
            t = t+a[i][j]*y[j]
        y[i] = (b[i]-t)/a[i][i]
    IZ_y = np.vstack((IZ, y))
    IZ_y = IZ_y.T
    IZ_y= np.sort(IZ_y,axis=0)
    x = IZ_y[:,1]
    return x
#对a，b进行消元计算与回代计算
def gauss_elimination(a,b):


    a,b,IZ= elimination(a,b)
    x = back_to_generation(a,b,IZ)
    return x
def test():
    a = np.array([[1, 2, 3], [2, 5, 2], [3, 1, 5]],dtype=float)
    b = np.array([14, 18, 20],dtype=float)
    x = gauss_elimination(a, b)
    print(x)
if __name__ == '__main__':
    test()