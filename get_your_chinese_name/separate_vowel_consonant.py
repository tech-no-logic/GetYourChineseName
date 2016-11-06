# coding=gbk
import re


def separate_vowel_and_consonant(pinyin):
    """
    Separate Vowel and Consonant in pinyin
    :type pinyin: String
    return: consonant, vowel
    """
    consonant=''
    vowel=''
    vowel_head = re.compile(r'\(|a|e|i|o|u|v')
    find_vowel_head = vowel_head.search(pinyin)
    if find_vowel_head is not None:
        consonant = pinyin[:pinyin.find(find_vowel_head.group())]
        vowel = pinyin[pinyin.find(find_vowel_head.group()):]
    return consonant, vowel


# test

if __name__ == "__main__":

    pinyin=input("������ƴ����")
    consonant,vowel=separate_vowel_and_consonant(pinyin)
    print(consonant+' '+vowel)

