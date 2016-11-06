# coding=gbk
# this program should run only  once
import xlrd
import sqlite3


def is_table_exist(connect, table_name):
    """

    :param connect:
    :param table_name:
    :return:
    """
    cursor = connect.execute(
        u'SELECT COUNT(*) FROM sqlite_master WHERE  type=\'table\' AND name=\'{0:s}\''.format(table_name))
    for row in cursor:
        if row[0] == 0:
            return False
    return True


def convert_xls_to_db(xls_name, factor_name):
    """
    to convert a comparing table
    :param xls_name: the name of excel file
    :param factor_name: the name of factors
    :return: nothing
    """
    consonant_xls = xlrd.open_workbook('..\\resources\\' + xls_name + '.xls')  # 打开拼音模糊表达表
    consonant_table = consonant_xls.sheets()[0]  # 打开sheet1
    n_rows = consonant_table.nrows  # 获取行数
    n_cols = consonant_table.ncols  # 获取列数

    connection = sqlite3.connect('..\\resources\\database.db')
    if is_table_exist(connection,xls_name) is False:
            connection.execute(u'CREATE TABLE {0:s}\
                                (ID INT PRIMARY KEY   NOT NULL,\
                                {1:s}1 CHAR(5),\
                                {2:s}2 CHAR(5),\
                                VALUE REAL)\
                              '.format(xls_name, factor_name, factor_name))
    for i in range(1, n_rows):
        for j in range(1, n_cols):
            cursor = connection.execute(
                u'SELECT COUNT(*) FROM {0:s} WHERE  {1:s}1=\'{2:s}\' AND {3:s}2=\'{4:s}\''
                    .format(xls_name, factor_name, consonant_table.cell(i, 0).value,
                            factor_name, consonant_table.cell(0, j).value))
            for row in cursor:
                if row[0] == 0:
                    if consonant_table.cell(i, j).value == '':
                        connection.execute(
                            u'INSERT INTO {0:s}(ID,{1:s}1,{2:s}2,VALUE) VALUES({3:d},\"{4:s}\",\"{5:s}\",{6})'
                                .format(xls_name, factor_name, factor_name,
                                        i * 100 + j,
                                        consonant_table.cell(i, 0).value,
                                        consonant_table.cell(0, j).value,
                                        consonant_table.cell(j, i).value))
                        connection.commit()
                        print(u'INSERT INTO {0:s}(ID,{1:s}1,{2:s}2,VALUE) VALUES({3:d},\"{4:s}\",\"{5:s}\",{6})'
                              .format(xls_name, factor_name, factor_name,
                                      i * 100 + j,
                                      consonant_table.cell(i, 0).value,
                                      consonant_table.cell(0, j).value,
                                      consonant_table.cell(j, i).value))
                    else:
                        connection.execute(u'INSERT INTO {0:s}(ID,{1:s}1,{2:s}2,VALUE) VALUES({3:d},\"{4:s}\",'
                                           u'\"{5:s}\",{6})'
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


def convert_xls_to_db_2(xls_name, factor_name1, factor_name2):
    """
    to convert one to one xls tables
    :param xls_name: string, the name of xls files
    :param factor_name1: first factor's name
    :param factor_name2: second factor's name
    :return: nothing
    """
    consonant_xls = xlrd.open_workbook('..\\resources\\' + xls_name + '.xls')  # 打开excel表
    consonant_table = consonant_xls.sheets()[0]  # 打开sheet1
    n_rows = consonant_table.nrows  # 获取行数

    connection = sqlite3.connect('..\\resources\\database.db')
    if is_table_exist(connection,xls_name):
            connection.execute(u'CREATE TABLE {0:s}(ID INT PRIMARY KEY   NOT NULL,\
                                {1:s} CHAR(10),\
                                {2:s} CHAR(10))'.format(xls_name, factor_name1, factor_name2))

    for i in range(1, n_rows):
        cursor = connection.execute(
            u'SELECT COUNT(*) FROM {0:s} WHERE  {1:s}=\'{2:s}\''
                .format(xls_name, factor_name1, consonant_table.cell(i, 0).value))
        for row in cursor:
            if row[0] == 0 and consonant_table.cell(i, 0).value != '':
                connection.execute(
                    u'INSERT INTO {0:s}(ID,{1:s},{2:s}) VALUES({3:d},\"{4:s}\",\"{5:s}\")'
                        .format(xls_name, factor_name1, factor_name2,
                                i, consonant_table.cell(i, 0).value,
                                consonant_table.cell(i, 1).value))
                connection.commit()
                print(
                    u'INSERT INTO {0:s}(ID,{1:s},{2:s}) VALUES({3:d},\"{4:s}\",\"{5:s}\")'
                        .format(xls_name, factor_name1, factor_name2,
                                i, consonant_table.cell(i, 0).value,
                                consonant_table.cell(i, 1).value))
    return


# test
if __name__ == "__main__":
    convert_xls_to_db('声母模糊表达表1', 'consonant')
    convert_xls_to_db('韵母模糊表达表2', 'vowel')
    convert_xls_to_db_2('拼音整理1', 'pinyin', 'std_pinyin')
