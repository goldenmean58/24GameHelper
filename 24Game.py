#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : 24Game.py
# @Time     : Tue 24 Jul 2018 12:49:34 PM CST
# @Authand   : Lishuxiang
# @E-mail   : lishuxiang@cug.edu.cn
# @Function : find all solutions fand 24 game
import itertools #combinations and permutations
import copy

def RPN2IN(exp):
    #逆波兰表示法表达式转化为中缀表达式
    stack=list()
    for iter in exp:
        stack.append(iter)
        if stack[-1]=='+' :
            stack.pop()
            a=stack.pop()
            b=stack.pop()
            stack.append('('+str(b)+' + '+str(a)+')')
        if stack[-1]=='-' :
            stack.pop()
            a=stack.pop()
            b=stack.pop()
            stack.append('('+str(b)+' - '+str(a)+')')
        if stack[-1]=='*' :
            stack.pop()
            a=stack.pop()
            b=stack.pop()
            stack.append('('+str(b)+' * '+str(a)+')')
        if stack[-1]=='/' :
            stack.pop()
            a=stack.pop()
            b=stack.pop()
            if a!=0:
                stack.append('('+str(b)+' / '+str(a)+')')
            else:
                return False
    return stack.pop()
    

def calc(exp):
    #计算逆波兰表示法
    #exp=list(1,2,3,4,'+','-','*') and list (1,2,'+',3,'-',4,'*')
    stack=list()
    for iter in exp:
        stack.append(iter)
        if stack[-1]=='+' :
            stack.pop()
            a=stack.pop()
            b=stack.pop()
            stack.append(b+a)
        if stack[-1]=='-' :
            stack.pop()
            a=stack.pop()
            b=stack.pop()
            stack.append(b-a)
        if stack[-1]=='*' :
            stack.pop()
            a=stack.pop()
            b=stack.pop()
            stack.append(b*a)
        if stack[-1]=='/' :
            stack.pop()
            a=stack.pop()
            b=stack.pop()
            if a!=0:
                stack.append(b/a)
            else:
                return False
    return stack.pop()

def func(list_nums,target,dev):
    solutions=list()
    if len(list_nums) == 0 :
        return False
    numbers=list(itertools.permutations(list_nums,4)) #numbers is a list of full permutations of four numbers
    symbol_str='+-*/'
    symbol=list()
    interal_list=list()
    for i in range(4):
        for j in range(4):
            for k in range(4):
                interal_list=list()
                interal_list.append(symbol_str[i])
                interal_list.append(symbol_str[j])
                interal_list.append(symbol_str[k])
                symbol.append(interal_list)
    for iter in numbers:
        exp=list()
        for iter2 in iter:
            exp.append(iter2) # exp=list(1,2,3,4)
        #first situation: three symbols in the last place of the exp
        for iter2 in symbol:
            exp1=copy.copy(exp)
            for iter3 in iter2:
                exp1.append(iter3) #exp1=list(1,2,3,4,'+','-','*')
            ret=calc(exp1)
            if ret<=target+dev and ret>=target-dev:
                solutions.append(RPN2IN(exp1))
        #second situation: one symbol in the third place of the exp two in the last.
        for iter2 in symbol:
            exp1=copy.copy(exp)
            exp1.insert(3,iter2[0])
            exp1.append(iter2[1])
            exp1.append(iter2[2])
            ret=calc(exp1)
            if ret<=target+dev and ret>=target-dev:
                solutions.append(RPN2IN(exp1))
        #third situation: two symbols in the third place and one in the last
        for iter2 in symbol:
            exp1=copy.copy(exp)
            exp1.insert(3,iter2[0])
            exp1.insert(3,iter2[1])
            exp1.append(iter2[2])
            ret=calc(exp1)
            if ret<=target+dev and ret>=target-dev:
                solutions.append(RPN2IN(exp1))
        #forth situation: one symbol in the second place and two in the last
        for iter2 in symbol:
            exp1=copy.copy(exp)
            exp1.insert(2,iter2[0])
            exp1.append(iter2[1]);
            exp1.append(iter2[2]);
            ret=calc(exp1)
            if ret<=target+dev and ret>=target-dev:
                solutions.append(RPN2IN(exp1))
        #fifth situation: one in the second, one in the third and one in the last
        for iter2 in symbol:
            exp1=copy.copy(exp)
            exp1.insert(2,iter2[0])
            exp1.insert(4,iter2[1])
            exp1.append(iter2[2])
            ret=calc(exp1)
            if ret<=target+dev and ret>=target-dev:
                solutions.append(RPN2IN(exp1))
    return solutions

#a=calc([8,3,8,3,'/','-','/'])
while(True):
    base_num=eval(input(("请输入四个由逗号隔开的正整数(1<=N<=13):")))
    ret=func(base_num,24,0.0000001)
    for iter in ret:
        print(iter[1:-1])
    print('共找到 %d 种解法'%len(ret))
