
'''高斯消去法'''

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
    for k in range(0,len(a)-1):
        for i in range(k+1,len(a)):
            elimination_line(a,b,k,i)
    return a,b
def back_to_generation(a,b,x):
    x[len(a)-1] = b[-1]/a[-1][-1]
    for i in range(len(a)-2,-1,-1):
        t = 0
        for j in range(i+1,len(a)):
            t = t+a[i][j]*x[j]
        x[i] = (b[i]-t)/a[i][i]
    return x
#对a，b进行消元计算与回代计算
def gauss_elimination(a,b):
    x = [0 for i in range(len(a))]
    a,b = elimination(a,b)
    x = back_to_generation(a,b,x)
    return x
#测试
def test():
    a = [[1,2,3],[2,5,2],[3,1,5]]
    b = [14,18,20]
    x = gauss_elimination(a,b)
    print(x)
if __name__ == '__main__':
    test()