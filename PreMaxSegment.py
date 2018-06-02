
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 15:22:40 2018

@author: hogen

"""

def PreMaxSeg1(sen,dicts,span):
    '''前向最大匹配算法1'''
    idx = 0
    while idx<len(sen):
        matched=False
        for i in range(span,0,-1):
            phrase = sen[idx:idx+i]
            if phrase in dicts:
                matched=True
                yield phrase
                break
        
        if not matched:
            i=1
            yield sen[idx]
        idx += i

def PreMaxSeg2(sen,dicts,span):
    '''前向最大匹配分词2'''
    cur,tail = 0,span
    while (cur < tail and cur<len(sen)):
        if len(sen)<span:
            tail = len(sen)
        
        if tail == cur+1:
            yield sen[cur:tail]
            cur +=1
            tail = cur+span
        elif sen[cur:tail] in dicts:
            yield sen[cur:tail]
            cur=tail
            tail = cur+span
        else:
            tail-=1

if __name__=="__main__":
    dicts = [u'有些', u'大学生', u'眼高手低', u'小事情']
    sen = u'有些大学生眼高手低，不屑于做小事情。'
    span = 4
    print('/'.join(PreMaxSeg1(sen,dicts,span)))



