import csv,os,re
import urllib.request as ur
from bs4 import BeautifulSoup as bs

def opencsv(filename):
    f=open(filename,'r')
    reader=csv.reader(f)
    output=[]
    for i in reader:
        output.append(i)
    return output

def writecsv(filename,the_list):
    with open(filename,'w',newline='') as f:
        a=csv.writer(f,delimiter=',')
        a.writerows(the_list)

def switch(listName):
    for i in listName:
        for j in i:
            try:
                i[i.index(j)]=float(re.sub(',','',j))
            except:
                pass
        return listName

url1='http://quotes.toscrape.com/'

html=ur.urlopen(url1)

soup=bs(html.read(),'html.parser')

quote=soup.find_all('div',{"class":"quote"})



'''list_of_word=[]
for i in quote:
    if i.text!='':
        list_of_word.append(i.text)

print(list_of_word)'''

print(soup.find_all("div",{"class":"quote"})[0].text)
