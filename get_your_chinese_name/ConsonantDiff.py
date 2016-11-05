#coding=gbk
import xlrd

def Calc2ConsonantDiff(consonant1,consonant2):
    '''
    Calculate the difference of consonant1 and consonant2
    :param consonant1: string, consonant1
    :param consonant2: string��consonant2
    :return: diff: int, difference of consonant1 and consonant2
    '''
    consonantXLS = xlrd.open_workbook('resources\��ĸģ������1.xls');  # ����ĸģ������
    consonantTable = consonantXLS.sheets()[0]  # ��sheet1
    nRows = consonantTable.nrows  # ��ȡ����
    nCols = consonantTable.ncols  # ��ȡ����
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
    consonant1=input('��������ĸ1��')
    consonant2=input('��������ĸ2��')
    print(str(Calc2ConsonantDiff(consonant1,consonant2)))
