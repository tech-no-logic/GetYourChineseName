# coding:UTF-8

import urllib.request
import re
import socket
import time
from urllib import parse
from bs4 import BeautifulSoup


def multiple_replace(text, a_dict):
    rx = re.compile('|'.join(map(re.escape, a_dict)))

    def one_xlate(match):
        return a_dict[match.group(0)]

    return rx.sub(one_xlate, text)


def make_xlate(*args, **key_words):
    addict = dict(*args, **key_words)
    rx = re.compile('|'.join(map(re.escape, addict)))

    def one_xlate(match):
        return addict[match.group(0)]

    def xlate(text):
        return rx.sub(one_xlate, text)

    return xlate


def replace_py(text):
    addict = {
        "ā": "a", "á": "a", "ǎ": "a", "à": "a",
        "ē": "e", "é": "e", "ě": "e", "è": "e",
        "ī": "i", "í": "i", "ǐ": "i", "ì": "i",
        "ō": "o", "ó": "o", "ǒ": "o", "ò": "o",
        "ū": "u", "ú": "u", "ǔ": "u", "ù": "u",
        "ǖ": "v", "ǘ": "v", "ǚ": "v", "ǜ": "v", "ü": "v",
    }
    return multiple_replace(text, addict)


def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if u'\u4e00' <= uchar <= u'\u9fa5':
        return True
    else:
        return False


def is_in_file(character):
    flag = 0
    file1 = open('a3.txt', 'r')
    for line_f in file1:
        for c in line_f:
            if is_chinese(c):
                if character == c:
                    flag = 1
                    break
        if flag == 1:
            break
    file1.close()
    if flag == 1:
        return True
    else:
        return False


if __name__ == "__main__":
    timeout = 10
    socket.setdefaulttimeout(timeout)
    sleep_download_time = 2
    i = 0
    f0 = open('..\\resources\\a2.txt', 'r')

    for line in f0:
        for ch in line:
            s = ch
            if is_chinese(s):
                if i == 0 or is_in_file(s) is False:
                    s = parse.quote(s)
                    web_url = "http://hanyu.baidu.com/zici/s?wd=%s&tupu=01" % s
                    web_headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

                    time.sleep(sleep_download_time)
                    req = urllib.request.Request(url=web_url, headers=web_headers)
                    web_page = urllib.request.urlopen(req)
                    contentBytes = web_page.read()
                    web_page.close()

                    soup = BeautifulSoup(contentBytes, 'html.parser')
                    f1 = open('..\\resources\\a3.txt', 'a')
                    lis = []
                    fl = 0
                    for cs in soup.body.find_all('span')[2].find_all('b'):
                        new_cs = replace_py(cs.string)
                        for cc in lis:
                            if cc == new_cs:
                                fl = 1
                        if fl == 0:
                            lis.append(new_cs)
                            print(ch + '\t' + new_cs)
                            f1.write(ch + '\t' + new_cs + '\n')
                    f1.close()
                    i += 1
    f0.close()

    print('完成')
