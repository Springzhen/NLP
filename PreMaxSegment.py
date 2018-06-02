
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 15:22:40 2018

@author: hogen

"""




def PreMaxSeg(sen,dicts,span):
    '''前向最大匹配算法'''
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



if __name__=="__main__":
    dicts = [u'有些', u'大学生', u'眼高手低', u'小事情']
    sen = u'有些大学生眼高手低，不屑于做小事情。'
    span = 4
    print('/'.join(PreMaxSeg(sen,dicts,span)))



