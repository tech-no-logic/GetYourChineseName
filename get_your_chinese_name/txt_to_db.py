#
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


def is_item_exist(connect, table_name, pro_name, item):
    """

    :param connect:
    :param table_name:
    :param pro_name:
    :param item:
    :return:
    """
    cursor = connect.execute(
        u'SELECT COUNT(*)FROM {0:s} where {1:s}=\'{2:s}\''.format(table_name, pro_name, item)
    )
    for row in cursor:
        if row[0] == 0:
            return False
    return True


def convert_txt_to_db(txt_name, factor1, factor2):
    """

    :param txt_name:
    :param factor1:
    :param factor2:
    :return:
    """
    f0 = open('..\\resources\\' + txt_name+'.txt', 'r')
    connection = sqlite3.connect('..\\resources\\database.db')
    if is_table_exist(connection, txt_name) is False:
        connection.execute(u'CREATE TABLE {0:s}\
                                        (ID INT PRIMARY KEY   NOT NULL,\
                                        {1:s} CHAR(50),\
                                        {2:s} CHAR(50))\
                                      '.format(txt_name, factor1, factor2))
    i = 0
    for line in f0:
    #    if is_item_exist(connection, txt_name, factor2, line[line.find('\t')+1:line.rfind('\n')]) is False:
            connection.execute(
                u'INSERT INTO {0:s} (ID,{1:s},{2:s})VALUES ({3:d},\'{4:s}\',\'{5:s}\')'.format(
                    txt_name, factor1, factor2, i, line[:line.find( '\t')], line[line.find('\t')+1:line.rfind('\n')]
                )
            )
            connection.commit()
            print(
                u'INSERT INTO {0:s} (ID,{1:s},{2:s})VALUES ({3:d},\'{4:s}\',\'{5:s}\')'.format(
                    txt_name, factor1, factor2, i, line[:line.find( '\t')], line[line.find('\t')+1:line.rfind('\n')]
                )
            )
            i += 1
    return


# test
if __name__ == "__main__":
    convert_txt_to_db('foreignName2Chinese', 'English_name', 'Chinese_name')
    convert_txt_to_db('chineseName2Pinyin','Chinese','pinyin')
    convert_txt_to_db('常用汉字拼音对照表1','pinyin','Chinese')