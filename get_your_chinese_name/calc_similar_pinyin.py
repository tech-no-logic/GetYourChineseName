#coding: gbk
import separate_vowel_consonant
import sqlite3


def calc_sim_pinyin(input_pinyin):
    similar_pinyin=[]
    std_pinyin=''
    connection = sqlite3.connect('..\\resources\\database.db')
    cursor=connection.execute(u'SELECT COUNT(std_pinyin) FROM 拼音整理1 WHERE pinyin=\'{0:s}\''.format(input_pinyin))
    for row in cursor:
        if row[0]!=0:
            cursor1 = connection.execute(
                u'SELECT std_pinyin FROM 拼音整理1 WHERE pinyin=\'{0:s}\''.format(input_pinyin))
            for row1 in cursor1:
                std_pinyin=row1[0]
    init_consonant, init_vowel = separate_vowel_consonant.separate_vowel_and_consonant(std_pinyin)
    cursor=connection.execute(u'SELECT 声母模糊表达表1.consonant2,韵母模糊表达表2.vowel2 \
                              FROM 声母模糊表达表1 JOIN 韵母模糊表达表2 \
                              WHERE 声母模糊表达表1.consonant1=\'{0:s}\'\
                              AND 韵母模糊表达表2.vowel1=\'{1:s}\' \
                              AND 声母模糊表达表1.VALUE+韵母模糊表达表2.VALUE<30\
                              '.format(init_consonant,init_vowel))
    for row in cursor:
        cursor1=connection.execute(u'SELECT COUNT(std_pinyin) FROM 拼音整理1 WHERE std_pinyin=\'{0:s}\' '.format(row[0]+row[1]))
        for row1 in cursor1:
            if row1[0]!=0:
                similar_pinyin.append(row[0]+row[1])

    return similar_pinyin

if __name__ == "__main__":
    pinyin = input('please input a pinyin:')
    sim_pinyin=calc_sim_pinyin(pinyin)
    print(sim_pinyin)
