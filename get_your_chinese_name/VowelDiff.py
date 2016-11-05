#coding=gbk
import xlrd

def Calc2VowelDiff(vowel1,vowel2):
    '''
    Calculate the difference of vowel1 and vowel2
    :param vowel1: string, vowel1
    :param vowel2: string，vowel2
    :return: diff: int, difference of vowel1 and vowel2
    '''
    VowelXLS = xlrd.open_workbook('..\\resources\\韵母模糊表达表2.xls');  # 打开韵母模糊表达表
    VowelTable = VowelXLS.sheets()[0]  # 打开sheet1
    nRows = VowelTable.nrows  # 获取行数
    nCols = VowelTable.ncols  # 获取列数
    diff=100
    for i in range(1,nRows):
        if(VowelTable.cell(0,i).value==vowel1):
            for j in range(1,nCols):
                if (VowelTable.cell(j, 0).value==vowel2):
                    diff=((VowelTable.cell(i, j).value) \
                                 if (VowelTable.cell(i, j).value!='') \
                                 else (VowelTable.cell(j, i).value))
                    break
            break
    return diff

#test

if __name__ == "__main__":
    vowel1=input('请输入韵母1：')
    vowel2=input('请输入韵母2：')
    print(str(Calc2VowelDiff(vowel1,vowel2)))
