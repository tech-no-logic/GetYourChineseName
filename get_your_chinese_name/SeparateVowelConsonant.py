#coding=gbk
import re

def SeparateVowelAndConsonant(Pinyin):
    """
    Separate Vowel and Consonant in Pinyin
    :type Pinyin: String
    return: consonant, vowel
    """
    vowelHead = re.compile(r'\(|a|e|i|o|u|v')
    findVowelHead =vowelHead.search(Pinyin)
    consonant=Pinyin[:Pinyin.find(findVowelHead.group())]
    vowel=Pinyin[Pinyin.find(findVowelHead.group()):]
    return consonant,vowel

#test
'''
if __name__ == "__main__":

    pinyin=input("请输入拼音：")
    consonsant,vowel=SeparateVowelConsonsant(pinyin)
    print(consonsant+' '+vowel)
'''
