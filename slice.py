#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#利用切片和递归，去除字符串前面所有的空格和后面所有的空格
def trim(s):
    if s == '':
        return s
    elif s[0] == ' ':
        s = trim(s[1:])
    elif s[-1] == ' ':
        s = trim(s[:-1])
    return s
                
        
print (trim('hello  '))
print (trim('  hello'))
print (trim('  hello  '))
print (trim('  hello  world  '))
print (trim(''))
print (trim('    '))


# 利用迭代查找list中的最大值和最小值，返回一个tuple
def findMinAndMax(L):
    l = len(L)
    max = 0
    min = 0
    if l<2:
        print ('请输入2个以上的列表查找最大值和最小值')
    else:
        for x in L:
            if x>=max:
                max = x
                s=(max,min)
            if x<=min:
                min = x
                s=(max,min)
        print (s) 
    
    
findMinAndMax([])
findMinAndMax([7])
findMinAndMax([7, 1, 3, 9, 5])
findMinAndMax([7.8, 1, 3, 9.4533, 5])