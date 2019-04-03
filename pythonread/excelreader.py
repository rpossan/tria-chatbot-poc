import xlrd
import xlwt
from xlutils.copy import copy
import numpy

workbook = xlrd.open_workbook("C:\\Códigos chatbot\\chatbot\\pythonread\\Banco de perguntas e respostas - TP_PIS-Pasep-Cofins_LucroReal.xls")
worksheets = workbook.sheet_names()
num_sheets = len(worksheets)
wb = copy(workbook)
frase = 'despesas pré-operacionais?'
frase = frase.replace("?", "")
frase = frase.replace(".", "")
frase = frase.replace(",", "")
frase = frase.replace("!", "")
frase2 = frase.split(' ')
size = len(frase2)
prepos = ["olá", "ola", "oi", "bom", "dia", "boa", "tarde", "noite", "a", "o", "as", "os", "e", "ao", "aos", "à", "até", "ou", "não", "após", "ante", "com", "conforme", "contra", "de", "da", "do", "desde", "durante", "em", "entre", "mediante", "para", "perante", "por", "salvo", "sem", "sob", "sobre", "trás", "antes", "depois", "?", "!", ".", ","]
num_prepos = len(prepos)
check_prepos = 0

matriz = numpy.zeros(shape=(255,255))

print ("Os parágrafos são:\n")

count_sheets = 0
names_sheets = ''
list = []
for i0 in workbook.sheet_names():
    print (i0)
    list.append(i0)
    count_sheets = count_sheets + 1

for i in range (0, count_sheets):
    worksheet = workbook.sheet_by_name(list[i])
    count_words = 0
    for j in range (worksheet.nrows):
        text = worksheet.cell(j, 1).value
        print ("Parágrafo linha" + str(j))
        print ("o texto é: "+str(text))
        for k in range (0, size):
            for l in range (0, num_prepos):
                if (frase2[k] == prepos[l]):
                    print ("prepos")
                    check_prepos = 1
                    break
            if (check_prepos == 0):
                if (str(frase2[k]) in str(text)):
                    print("sem prepos")
                    print (frase2[k])
                    count_words = count_words + 1
                check_prepos = 0
            else:
                check_prepos = 0
        matriz[i][j] = count_words
        count_words = 0

max_value = matriz.max()
print (max_value)
pos_sheet = []
pos_row = []
num_answer = 0

for i2 in range (0, count_sheets):
    worksheet = workbook.sheet_by_name(list[i2])
    for j2 in range (worksheet.nrows):
        if (matriz[i2][j2] == max_value):
            pos_sheet.append(i2)
            pos_row.append(j2)
            num_answer = num_answer + 1

print ("O número de respostas compatíveis é: "+str(num_answer))

for i3 in range (0, num_answer):
    sheet_answer = pos_sheet[i3]
    worksheet = workbook.sheet_by_name(list[sheet_answer])
    print (sheet_answer)
    row_answer = pos_row[i3]
    print (worksheet.cell(row_answer, 2).value)
