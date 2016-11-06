#
import xlrd
import sqlite3


def turn_xls_to_db(xls_name, factor_name):
    consonant_xls = xlrd.open_workbook('..\\resources\\' + xls_name + '.xls')  # 打开拼音模糊表达表
    consonant_table = consonant_xls.sheets()[0]  # 打开sheet1
    n_rows = consonant_table.nrows  # 获取行数
    n_cols = consonant_table.ncols  # 获取列数

    connection = sqlite3.connect('..\\resources\\pinyin_diff.db')
    connection.execute('''CREATE TABLE %s
                             (ID INT PRIMARY KEY   NOT NULL,
                              %s1 CHAR(5),
                         %s2 CHAR(5),
                      VALUE REAL);
                ''' % (xls_name, factor_name, factor_name))
    for i in range(1, n_rows):
        for j in range(1, n_cols):
            if consonant_table.cell(i, j).value != '':

                connection.execute(u'INSERT INTO {0:s}(ID,{1:s}1,{2:s}2,VALUE) VALUES({3:d},\"{4:s}\",\"{5:s}\",{6})'
                                   .format(xls_name, factor_name, factor_name,
                                           i * 100 + j,
                                           consonant_table.cell(i, 0).value,
                                           consonant_table.cell(0, j).value,
                                           consonant_table.cell(i, j).value))
                connection.commit()
                print(u'INSERT INTO {0:s}(ID,{1:s}1,{2:s}2,VALUE) VALUES({3:d},\"{4:s}\",\"{5:s}\",{6})'
                      .format(xls_name, factor_name, factor_name,
                              i * 100 + j,
                              consonant_table.cell(i, 0).value,
                              consonant_table.cell(0, j).value,
                              consonant_table.cell(i, j).value))
    return


if __name__ == "__main__":
    turn_xls_to_db('声母模糊表达表1', 'consonant')
    turn_xls_to_db('韵母模糊表达表2', 'consonant')

