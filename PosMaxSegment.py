#encoding=utf8
"""
Created on Mon May 28 20:29:41 2018

@author: hogen
"""

def PosMax1(sen,dicts,span):
    idx = len(sen)
    senlis = []
    while idx>0:
        matched = False
        for i in range(span,0,-1):
            phrase = sen[idx-i:idx]
            if phrase in dicts:
                matched=True
                senlis.append(phrase)
                break
        if not matched:
            senlis.append(sen[idx-1])
            i=1
        idx-=i
    senlis.reverse()
    return senlis



def PosMax2(sentence,dicts,span):
    cur = len(sentence)-span
    tail = len(sentence)
    if cur<0:
        cur=0

    ParseList = []
    while(cur<tail and tail>0):
        if tail == cur+1:
            ParseList.append(sentence[cur:tail])
            tail-=1
            cur = tail - span
            if cur<0:
                cur=0
        elif sentence[cur:tail] in dicts:
            ParseList.append(sentence[cur:tail])
            tail=cur
            cur = tail-span
            if cur<0:
                cur=0
        else:
            cur+=1
    ParseList.reverse()
    return ParseList


if __name__=="__main__":
    dicts = [u'有些', u'大学生', u'眼高手低', u'小事情']
    sen = u'有些大学生眼高手低，不屑于做小事情。'
    span = 4
    print('/'.join(PosMax(sen,dicts,span)))
