# https://medium.com/@rqaiserr/how-to-convert-pdfs-into-searchable-key-words-with-python-85aab86c544f

import PyPDF2 
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#write a for-loop to open many files -- leave a comment if you'd #like to learn how
# Change the fileName to the pdf file which exists in the same working directory
filename = 'digital.pdf' 
#open allows you to read the file
pdfFileObj = open(filename,'rb')
#The pdfReader variable is a readable object that will be parsed
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#discerning the number of pages will allow us to parse through all #the pages
num_pages = pdfReader.numPages
count = 0
text = ""
#The while loop will read each page
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText().encode('utf-8')
# the encode method helps in converting the text which is complied in terms of unicoded value back to readable format by using the utf-8 transcription method
#This if statement exists to check if the above library returned #words. It's done because PyPDF2 cannot read scanned files.
if text != "":
   text = text
#If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text
else:
   text = textract.process(fileurl, method='tesseract', language='eng').encode('utf-8')
# Now we have a text variable which contains all the text derived #from our PDF file. Type print(text) to see what it contains. It #likely contains a lot of spaces, possibly junk such as '\n' etc.
# Now, we will clean our text variable, and return it as a list of keywords.
# print(text)
# Lentext firstly we convert all the text which is in list to individual word and then we can find the no of words in that particular pdf book
Lentext = len(str(text))
print(Lentext)


