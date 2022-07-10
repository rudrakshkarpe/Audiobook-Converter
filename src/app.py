import PyPDF2
import pyttsx3
pdfReader = PyPDF2.PdfFileReader(open('audiobook.pdf', 'rb'))
speaker = pyttsx3.init()

for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    text = pageObj.extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()

speaker.save_to_file(text, 'audio.mp3')
speaker.runAndWait()    