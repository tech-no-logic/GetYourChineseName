# coding:UTF-8
import codecs
import re

cntry = re.compile(r'\(|希伯來|英國|斯堪的那|阿拉伯|德國|希臘|拉丁|法國|丹麥|條頓|蓋爾|義大利|古英國|塞爾特|古威爾斯|威爾斯|西班牙')
file_name = '../resources/eng_names_2_standard_Chinese-4.txt'
write_file_name1 = '../resources/a1.txt'
write_file_name2 = '../resources/a2.txt'
f = codecs.open(file_name, 'r')
f1 = open(write_file_name1, 'w')
f2 = open(write_file_name2, 'w')
for line in f:
    ch = line[:line.find('\t') + 1]
    m1 = re.search(r'[^a-zA-Z\/]', ch)
    if m1:
        ch0 = ch[:ch.find(m1.group())]
        ch1 = ch[ch.find(m1.group()):]
        m2 = cntry.search(ch1)
        if m2:
            ch2 = ch1[ch1.find(m2.group()):]
            ch1 = ch1[:ch1.find(m2.group())]
            print(ch0 + '\t' + ch1 + '\t' + ch2)
            f1.write(ch0 + '\t' + ch1 + '\n')
            f2.write(ch0 + '\t' + ch2 + '\n')
        else:
            print(ch0 + '\t' + ch1)
            f1.write(ch0 + '\t' + ch1 + '\n')
            f2.write(ch0 + '\t' + '\n')
f.close()
f1.close()
f2.close()
