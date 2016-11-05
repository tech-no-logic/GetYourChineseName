# coding=gbk
import xlrd


def calc_2_consonant_diff(consonant_1, consonant_2):
    """
    Calculate the difference of consonant1 and consonant2
    :param consonant_1: string, consonant1
    :param consonant_2: string��consonant2
    :return: diff: int, difference of consonant1 and consonant2
    """
    consonant_xls = xlrd.open_workbook('..\\resources\\��ĸģ������1.xls')  # ����ĸģ������
    consonant_table = consonant_xls.sheets()[0]  # ��sheet1
    n_rows = consonant_table.nrows  # ��ȡ����
    n_cols = consonant_table.ncols  # ��ȡ����
    diff = 100
    for i in range(1, n_rows):
        assert isinstance(consonant_1, str)
        if consonant_table.cell(0, i).value == consonant_1:
            for j in range(1, n_cols):
                if consonant_table.cell(j, 0).value == consonant_2:
                    diff = (consonant_table.cell(i, j).value if consonant_table.cell(i,
                                                                                     j).value != '' else
                            consonant_table.cell(
                        j, i).value)
                    break
            break
    return diff


# test
if __name__ == "__main__":
    consonant1 = input('��������ĸ1��')
    consonant2 = input('��������ĸ2��')
    print(str(calc_2_consonant_diff(consonant1, consonant2)))
