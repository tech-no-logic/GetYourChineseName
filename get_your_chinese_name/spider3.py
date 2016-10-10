#coding:UTF-8

import urllib.request
import re
import socket
import time
from urllib import parse
from bs4 import BeautifulSoup

def multiple_replace(text, adict):  
     rx = re.compile('|'.join(map(re.escape, adict)))  
     def one_xlat(match):  
           return adict[match.group(0)]  
     return rx.sub(one_xlat, text)
def make_xlat(*args, **kwds):  
     adict = dict(*args, **kwds)  
     rx = re.compile('|'.join(map(re.escape, adict)))  
     def one_xlat(match):  
           return adict[match.group(0)]  
     def xlat(text):  
           return rx.sub(one_xlat, text)  
     return xlat
def replace_py(text):
    adict={
        "ā":"a","á":"a","ǎ":"a","à":"a",
        "ē":"e","é":"e","ě":"e","è":"e",
        "ī":"i","í":"i","ǐ":"i","ì":"i",
        "ō":"o","ó":"o","ǒ":"o","ò":"o",
        "ū":"u","ú":"u","ǔ":"u","ù":"u",
        "ǖ":"v","ǘ":"v","ǚ":"v","ǜ":"v","ü":"v",
        }
    return multiple_replace(text,adict)
def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False
def is_in_file(ch):
    flag=0
    f1=open('a3.txt','r')
    for line in f1:
        for c in line:
            if is_chinese(c):
                if ch==c:
                    flag=1
                    break
        if flag==1:
            break        
    f1.close()
    if flag==1:
        return True
    else:
        return False
if __name__ == "__main__":
    timeout=10
    socket.setdefaulttimeout(timeout)
    sleep_download_time=2
    i=0
    f0=open('a2.txt','r')
    
    for line in f0:
        for ch in line:
            s=ch
            if is_chinese(s):
                if i==0 or is_in_file(s)==False:
                    s=parse.quote(s)
                    weburl = "http://hanyu.baidu.com/zici/s?wd=%s&tupu=01"%(s)
                    webheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'} 

                    time.sleep(sleep_download_time)
                    req = urllib.request.Request(url=weburl, headers=webheaders)  
                    webpage = urllib.request.urlopen(req)  
                    contentBytes = webpage.read()
                    webpage.close()

                    soup=BeautifulSoup(contentBytes,'html.parser')
                    f1=open('a3.txt','a')
                    lis=[]
                    fl=0
                    for cs in soup.body.find_all('span')[2].find_all('b'):
                        csss=replace_py(cs.string)
                        for cc in lis:
                             if cc==csss:
                                  fl=1
                        if fl==0:
                             lis.append(csss)
                             print(ch+'\t'+csss)
                             f1.write(ch+'\t'+csss+'\n')
                    f1.close()
                    i=i+1
    f0.close()
    
    print('完成')
