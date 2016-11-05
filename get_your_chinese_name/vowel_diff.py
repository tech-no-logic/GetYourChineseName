# coding=gbk
import xlrd


def calc_2_vowel_diff(vowel_1, vowel_2):
    """
    Calculate the difference of vowel1 and vowel2
    :param vowel_1: string, vowel1
    :param vowel_2: string��vowel2
    :return: diff: int, difference of vowel1 and vowel2
    """
    vowel_x_l_s = xlrd.open_workbook('..\\resources\\��ĸģ������2.xls')  # ����ĸģ������
    vowel_table = vowel_x_l_s.sheets()[0]  # ��sheet1
    n_rows = vowel_table.nrows  # ��ȡ����
    n_cols = vowel_table.ncols  # ��ȡ����
    diff = 100
    for i in range(1, n_rows):
        if vowel_table.cell(0, i).value == vowel_1:
            for j in range(1, n_cols):
                if vowel_table.cell(j, 0).value == vowel_2:
                    diff = (vowel_table.cell(i, j).value if (vowel_table.cell(i, j).value != '') else vowel_table.cell(j, i).value)
                    break
            break
    return diff


# test

if __name__ == "__main__":
    vowel1 = input('��������ĸ1��')
    vowel2 = input('��������ĸ2��')
    print(str(calc_2_vowel_diff(vowel1, vowel2)))
