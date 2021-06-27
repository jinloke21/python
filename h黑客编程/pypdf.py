import PyPDF2
from PyPDF2 import PdfFileReader

def printMeta(filename):
    pdffile = PdfFileReader(filename,"rb")
    docinfo = pdffile.getDocumentInfo()
    for i in docinfo:
        print(i+':'+docinfo[i])

printMeta('/root/桌面/a.pdf')

