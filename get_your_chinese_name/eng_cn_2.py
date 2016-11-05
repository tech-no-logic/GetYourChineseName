# coding:UTF-8
import codecs
import re

# 这是第二步处理，所以注释掉第一步的不相关信息
# cntry=re.compile(r'\(|希伯來|英國|斯堪的那|阿拉伯|德國|希臘|拉丁|法國|丹麥|條頓|蓋爾|義大利|古英國|塞爾特|古威爾斯|威爾斯|西班牙')
# fname='eng_names_2_standard_Chinese-4.txt'
# wfname1='a1.txt'
# wfname2='a2.txt'
# f=codecs.open(fname,'r','utf-8')
# f1=open(wfname1,'w')
# f2=open(wfname2,'w')
# for line in f:
#    ch=line[:line.find('\t')+1]
#    m1=re.search(r'[^a-zA-Z\/]',ch)
#    if m1:
#        ch0=ch[:ch.find(m1.group())]
#        ch1=ch[ch.find(m1.group()):]
#        m2=cntry.search(ch1)
#        if m2:
#            ch2=ch1[ch1.find(m2.group()):]
#            ch1=ch1[:ch1.find(m2.group())]
#            print(ch0+'\t'+ch1+'\t'+ch2)
#            f1.write(ch0+'\t'+ch1+'\n')
#            f2.write(ch0+'\t'+ch2+'\n')
#        else:
#            print(ch0+'\t'+ch1)
#            f1.write(ch0+'\t'+ch1+'\n')
#            f2.write(ch0+'\t'+'\n')
# f.close()
# f1.close()
# f2.close()

fname2 = '../resources/a1.txt'
wfname3 = '../resources/a3.txt'
f3 = codecs.open(fname2, 'r')
f4 = open(wfname3, 'w')
for line in f3:
    ch3 = line[:line.find('\t') + 1]
    ch4 = line[line.find('\t') + 1:line.find('\n')]
    m3 = re.search(r'[\/]', ch3)
    #    t=m3
    #    if t:
    #        print(t)
    if m3:
        ch5 = ch3[:ch3.find(m3.group())]
        ch6 = ch3[ch3.find(m3.group()) + 1:]
        m4 = re.search(r'[\/]', ch6)
        if m4:
            ch7 = ch6[:ch6.find(m4.group())]
            ch8 = ch6[ch6.find(m4.group()) + 1:]
            f4.write(ch7 + '\t' + ch4)
            f4.write(ch8 + ch4)
        else:
            f4.write(ch5 + '\t' + ch4)
            f4.write(ch6 + ch4)
    else:
        ch12 = line[:line.find('\t') + 2]
        m5 = re.search(r'[\t]', ch12)
        if m5:  ##########
            print(m5)
            ch9 = ch12[:ch12.find(m5.group())]
            print(ch9)
            ch10 = line[line.find('\t') + 1:]
            m6 = re.search(r'[\n]', ch10)
            if m6:  ############
                ch11 = ch10[:ch10.find(m6.group())]
                f4.write(ch9 + ch11 + '\n')
f3.close()
f4.close()
