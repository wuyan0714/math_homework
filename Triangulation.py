'''直接三角分解'''
import numpy as np
def triangle(a):
    u = np.zeros_like(a)
    l = np.zeros_like(a)
    for i in range(len(a)):
        u[0, i] = a[0,i]
        l[i,i] = 1
        if i>0:
            l[i,0] = a[i,0]/u[0,0]
    for r in range(1,len(a)):
        for i in range(r,len(a)):
            t1=0
            for k in range(r):
                t1=t1+l[r,k]*u[k,i]
            u[r,i] = a[r,i]-t1
            t2=0
            for k in range(r):
                t2=t2+l[i,k]*u[k,r]
            l[i,r] = (a[i,r]-t2)/u[r,r]
    return l,u
def back_to_generation(b,l,u):
    x = np.zeros_like(b)
    y = np.zeros_like(b)
    y[0] = b[0]
    for i in range(1,len(b)):
        t1 = 0
        for k in range(i):
            t1 = t1 + l[i,k]*y[k]
        y[i] = b[i]-t1
    x[-1] = y[-1]/u[-1,-1]
    for i in range(len(b)-1,-1,-1):
        t2 = 0
        for k in range(i+1,len(b)):
            t2 = t2 + u[i,k]*x[k]
        x[i] =(y[i]-t2)/u[i,i]
    return x
def triangulation(a,b):
    l,u = triangle(a)
    print(l,u)
    x = back_to_generation(b,l,u)
    return x
def test():
    a = np.array([[1, 2, 3], [2, 5, 2], [3, 1, 5]], dtype=float)
    b = np.array([14, 18, 20], dtype=float)
    x = triangulation(a,b)
    print(x)
if __name__ == '__main__':
    test()