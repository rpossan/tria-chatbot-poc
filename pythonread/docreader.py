from docx import Document
import numpy

newfile = open('pdf.txt', 'w', encoding = 'utf8')
frase = "acesso login"
frase2 = frase.split(' ')
size = len(frase2)

matriz = numpy.zeros(shape=(255,1280))

paragraph = 0
paragraph_total = 0
j = 1

document = Document('manual_rps_V19R01.docx')
full_size = len(document.paragraphs)
print ("Os parágrafos são:\n")

for i in range (0,size):
    paragraph = 0;
    matriz [i][0] = i + 1
    j=1
    for para in document.paragraphs:
        ##print (frase2[i])
        ##textfinder = frase2[i]
        if frase2[i] in para.text:
            matriz [i][j] = paragraph
            print(para.text + " - " + str(paragraph))
            newfile.write(para.text+"\n")
            j = j + 1;
        paragraph = paragraph + 1;
    print ("Fim para "+frase2[i]+"\n")

    if (paragraph_total <= j):
        paragraph_total = j

count = 0;
final_count = 0
final_paragraph = 0;
list = []
aux1 = 0;

for k in range (0, size):
    for m in range (1, paragraph_total):
        if matriz[k][m] != 0:
            for n in range (0, size):
                for o in range (1, paragraph_total):
                    if matriz[k][m] == matriz[n][o]:
                        count = count + 1
            if final_count < count:
                final_count = count
                final_paragraph = matriz[k][m]
                list.clear()
                list.append(final_paragraph)
            elif final_count == count:
                final_paragraph = matriz[k][m]
                aux0 = len(list)
                for a in range (0,aux0):
                    if list[a] == matriz[k][m]:
                        aux1 = 1
                if aux1 == 0:
                    list.append(final_paragraph)
                    aux1 = 0
            count = 0;

print (final_count)
print (list)
print (len(list))
aux = len(list)

parag = 1
document = Document('manual_rps_V19R01.docx')
for p in document.paragraphs:
    for q in range (0, aux):
        if parag == list[q] + 1:
            print(p.text)
    parag = parag + 1
