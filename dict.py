#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print ('Bob的成绩是：',d['Bob'])

d['xiaoming'] = 68
print ('小明的成绩是：',d['xiaoming'])

print ('小明在这个d的列表里吗？\n答案是:','xiaoming' in d)

print (d)

# set开始啦,set不能选择可变的对象list

b = set((1,2,(1,2)))
b.remove(2)
print (b)

c = set([1,2,(1,2)])
c.add(8)
print (c)

#d = set([1,2,[1,2]])
#print (d)

#a = set((1,2,[1,2]))
#print (a)

