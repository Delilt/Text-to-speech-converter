import PyPDF2 # convert to pdf islemi icin
from gtts import gTTS # metin dosyasini sese cevirmek icin
import tkinter as tk
import os
from tkinter import filedialog

#pdf dosyasini acip okuma
def pdfMetniCikar(pdfPath):
    metin = ""
    readPDF = PyPDF2.PdfReader(open(pdfPath,'rb'))
    for pageNum in range(len(readPDF.pages)):
        metin += readPDF.pages[pageNum].extract_text()
    return metin

#metinleri sese cevirme
def pdfDosyasiniSeslendir(metin , outputFile):
    converter = gTTS(text=metin, lang='tr')
    converter.save(outputFile)

# dosya secme
def chooseFile():
    filePath = filedialog.askopenfilename(filetypes=[("PDF Dosyalari","*pdf")])
    if filePath:
        pdfText = pdfMetniCikar(filePath)
        pdfDosyasiniSeslendir(pdfText, "ceviri.mp3")
        os.system("start ceviri.mp3")
        flagLabel = tk.Label(appWindow,text="uygulama basarili",padx=10,pady=10)
        flagLabel.pack(padx=10,pady=10)
appWindow = tk.Tk()

appWindow.title("pdf to voice converter")
appWindow.geometry(["300x200"])

selectButton = tk.Button(appWindow,text="pdf sec",command=chooseFile,padx=20,pady=20)
selectButton.pack(padx=20,pady=20)


appWindow.mainloop()