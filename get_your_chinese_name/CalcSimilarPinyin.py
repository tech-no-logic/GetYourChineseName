import SeparateVowelConsonant
import ConsonantDiff
import VowelDiff
import xlrd

def CalcSimPinyin(pinyin):
    consProp=[]
    vowelProp=[]
    simPinyin=[]
    initConsonant, initVowel = SeparateVowelConsonant. \
        SeparateVowelAndConsonant(pinyin)
    print(initConsonant + '  ' + initVowel)

    VowelXLS = xlrd.open_workbook('resources\韵母模糊表达表2.xls');  # 打开韵母模糊表达表
    VowelTable = VowelXLS.sheets()[0]  # 打开sheet1
    nVowelCols = VowelTable.ncols  # 获取列数

    consonantXLS = xlrd.open_workbook('resources\声母模糊表达表1.xls');  # 打开声母模糊表达表
    consonantTable = consonantXLS.sheets()[0]  # 打开sheet1
    nConsonCols = consonantTable.ncols  # 获取列数
    sumDiff=0

    for i in range(nConsonCols):
        consDiff = ConsonantDiff.Calc2ConsonantDiff(consonantTable.cell(i, 0).value, initConsonant)
        if consDiff<30:
            consProp.append(consonantTable.cell(i,0).value)
    for j in range(nVowelCols):
        vowelDiff=VowelDiff.Calc2VowelDiff(VowelTable.cell(j,0).value,initVowel)
        if vowelDiff<10:
            vowelProp.append(VowelTable.cell(j,0).value)
    for cons in consProp:
        for vowel in vowelProp:
            simPinyin.append(cons+vowel)
    return simPinyin

if __name__ == "__main__":
    pinyin = input('please input a pinyin:')
    simpy=CalcSimPinyin(pinyin)
    print(simpy)