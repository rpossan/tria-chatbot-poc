import PyPDF2
import re

file = open ('tr_onesource_manual_usuario_import_brasil_V03R01.pdf', 'rb')
newfile = open('pdf.txt', 'w', encoding = 'utf8')

pdfreader = PyPDF2.PdfFileReader(file)
print(pdfreader.getNumPages())
num_pages = pdfreader.getNumPages()
count = 0
text = ""

while count < num_pages:  # The while loop will read each page
    pageObj = pdfreader.getPage(count)
    count += 1
    print(count)
    text += pageObj.extractText()
    if count == 4:
        print (text)
    newfile.write(pageObj.extractText())

##pageObj = pdfreader.getPage(10)


file.close()
newfile.close()
