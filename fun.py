#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
def quadratic(a,b,c):
    t = (b*b)-(4*a*c)
    if t>0:
        s = math.sqrt(t)
        x1 = (-b+s)/(2*a)
        x2 = (-b-s)/(2*a)
        print ('方程',a,'x^2+',b,'x+',c,'=0的解是:x1 =',x1,'x2=',x2)
    else:
        print ('方程',a,'x^2+',b,'x+',c,'=0无解')
        
quadratic(5,9,2)
quadratic(5,6,2)


