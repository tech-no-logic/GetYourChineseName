#
import sqlite3
import calc_similar_pinyin

def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if u'\u4e00' <= uchar <= u'\u9fa5':
        return True
    else:
        return False


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


def english_name_to_common_chinese(english_name):
    """

    :param english_name:
    :return:
    """
    chinese_name=[]
    connection = sqlite3.connect('..\\resources\\database.db')
    if is_item_exist(connection,'foreignName2Chinese','English_name',english_name) is True:
        cursor=connection.execute(
            u'SELECT Chinese_name FROM foreignName2Chinese WHERE English_name=\'{0:s}\''.format(english_name)
        )
        for itm in cursor:
            chinese_name.append(itm[0])
    return chinese_name


def chinese_string_to_single(chinese_string):
    """

    :param chinese_string: string
    :return: char[]
    """
    char=[]
    num=len(chinese_string)
    for i in range(0,num):
        char.append(chinese_string[i])
    return char


def chinese_char_to_pinyin(chinese_char):
    """

    :param chinese_char:
    :return:
    """
    pinyin_of_chinese_char=[]
    connection = sqlite3.connect('..\\resources\\database.db')
    if is_item_exist(connection,'chineseName2Pinyin','Chinese',chinese_char) is True:
        cursor=connection.execute(
            u'SELECT pinyin FROM chineseName2Pinyin WHERE Chinese=\'{0:s}\''.format(chinese_char)
        )
        for each_pinyin in cursor:
            pinyin_of_chinese_char.append(each_pinyin[0])
    return pinyin_of_chinese_char


def pinyin_to_chinese(pinyin):
    """

    :param pinyin:
    :return:
    """
    chinese_chars=[]
    connection = sqlite3.connect('..\\resources\\database.db')
    if is_item_exist(connection,'常用汉字拼音对照表1','pinyin',pinyin) is True:
        cursor = connection.execute(
            u'SELECT Chinese FROM 常用汉字拼音对照表1 WHERE pinyin=\'{0:s}\''.format(pinyin)
        )
        for each_chinese in cursor:
            chinese_chars.append(each_chinese[0])
    return chinese_chars

if __name__ == "__main__":
    english_name=input('please input English name:')
    chinese=english_name_to_common_chinese(english_name)
    for chars in chinese:
        print(chars)
    #    print(chinese_string_to_single(chars))
        single_chars=chinese_string_to_single(chars)
        for every_char in single_chars:
            print(every_char)
            pinyin=chinese_char_to_pinyin(every_char)
            for each_pinyin in pinyin:
                print(each_pinyin)
                similar_pinyin=calc_similar_pinyin.calc_sim_pinyin(each_pinyin)
                for each_similar_pinyin in similar_pinyin:
                    print(each_similar_pinyin)
                    similar_pinyin_chars=pinyin_to_chinese(each_similar_pinyin)
                    for each_similar_pinyin_char in similar_pinyin_chars:
                        print(each_similar_pinyin_char)
