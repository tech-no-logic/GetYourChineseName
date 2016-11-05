#coding=gbk
import xlrd

def Calc2ConsonantDiff(consonant1,consonant2):
    '''
    Calculate the difference of consonant1 and consonant2
    :param consonant1: string, consonant1
    :param consonant2: string，consonant2
    :return: diff: int, difference of consonant1 and consonant2
    '''
    consonantXLS = xlrd.open_workbook('..\\resources\\声母模糊表达表1.xls');  # 打开声母模糊表达表
    consonantTable = consonantXLS.sheets()[0]  # 打开sheet1
    nRows = consonantTable.nrows  # 获取行数
    nCols = consonantTable.ncols  # 获取列数
    diff=100
    for i in range(1,nRows):
        if(consonantTable.cell(0,i).value==consonant1):
            for j in range(1,nCols):
                if (consonantTable.cell(j, 0).value==consonant2):
                    diff=((consonantTable.cell(i, j).value) \
                                 if (consonantTable.cell(i, j).value!='') \
                                 else (consonantTable.cell(j, i).value))
                    break
            break
    return (diff)

#test
if __name__ == "__main__":
    consonant1=input('请输入声母1：')
    consonant2=input('请输入声母2：')
    print(str(Calc2ConsonantDiff(consonant1,consonant2)))
