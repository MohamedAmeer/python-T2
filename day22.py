# read a image and print it.
import cv2
import PyPDF2
import mysql.connector
img = cv2.imread('minion.JPG', 1)
print(img)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# merging a pdf

pdf1 = open('Additional Programs 1.pdf', 'rb')
pdf2 = open('Additional Programs.pdf', 'rb')

pdf1Reader = PyPDF2.PdfFileReader(pdf1)
pdf2Reader = PyPDF2.PdfFileReader(pdf2)

pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('MergedFiles.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
print(pdfOutputFile)
pdfOutputFile.close()
pdf1.close()
pdf2.close()

# scrape website and store data in db

import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.storyline')
subtext = soup.select('.subtext')
links2 = soup2.select('.storyline')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(link, subt):
    hn = []
    for idx, item in enumerate(link):
        title = item.getText()
        href = item.get('href', None)
        vote = subt[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(mega_links, mega_subtext))

# fiter the data in db

mydb =mysql.connector.connect(host="localhost", user="root", password="king786", database ='db1')
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM employee WHERE emp_id=02")
res = mycursor._fetch_row()

for x in res:
    print(x)