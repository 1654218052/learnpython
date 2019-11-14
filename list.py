#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 列表生成式
def low(L):
    print ([x.lower() for x in L if (isinstance(x, str) == True)])

low(['Hello', 'World', 18, 'Apple',None])



# 生成器
def low(L):
    print ((x.lower() for x in L if (isinstance(x, str) == True)))
    
low(['Hello', 'World', 18, 'Apple',None])



# 斐波拉契数列
def fi(m):
    a,b = 0,1
    while b<m:
        print (b)
        a = b
        b = a+b
        
fi(5)      


# 用生成器样式做出杨辉三角
def yang():
    L = [1]
    while 1:
        yield L
        L = [0] + L + [0]
        L = [L[i] + L[i + 1] for i in range(len(L) - 1)]
        
print (next(yang()))