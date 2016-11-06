#coding: gbk
import separate_vowel_consonant
import consonant_diff
import vowel_diff
import xlrd


def calc_sim_pinyin(input_pinyin):
    cons_prop=[]
    vowel_prop=[]
    similar_pinyin=[]
    init_consonant, init_vowel = separate_vowel_consonant. \
        separate_vowel_and_consonant(input_pinyin)
#    print(init_consonant + '  ' + init_vowel)

    vowel_xls = xlrd.open_workbook('..\\resources\\��ĸģ������2.xls')  # ����ĸģ������
    vowel_table = vowel_xls.sheets()[0]  # ��sheet1
    n_vowel_cols = vowel_table.ncols  # ��ȡ����

    consonant_xls = xlrd.open_workbook('..\\resources\\��ĸģ������1.xls')  # ����ĸģ������
    consonant_table = consonant_xls.sheets()[0]  # ��sheet1
    n_consonant_cols = consonant_table.ncols  # ��ȡ����

    for i in range(n_consonant_cols):
        cons_diff = consonant_diff.calc_2_consonant_diff(consonant_table.cell(i, 0).value, init_consonant)
        if cons_diff<30:
            cons_prop.append(consonant_table.cell(i,0).value)
    for j in range(n_vowel_cols):
        vowel_difference=vowel_diff.calc_2_vowel_diff(vowel_table.cell(j,0).value,init_vowel)
        if vowel_difference<10:
            vowel_prop.append(vowel_table.cell(j,0).value)
    for cons in cons_prop:
        for vowel in vowel_prop:
            similar_pinyin.append(cons + vowel)
    return similar_pinyin

if __name__ == "__main__":
    pinyin = input('please input a pinyin:')
    sim_pinyin=calc_sim_pinyin(pinyin)
    print(sim_pinyin)
