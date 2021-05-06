import csv,os,re
import urllib.request as ur
from bs4 import BeautifulSoup as bs
import ssl

os.chdir('/Users/junjoonheak/Desktop/웹클롤링_스터디')

contexts = ssl._create_unverified_context()


news='https://news.daum.net/'

soup=bs(ur.urlopen(news,context=contexts).read(),'html.parser')

#soup.find_all('div',{"class":"item_issue"}

f=open('link.txt','w')

for i in soup.find_all("div",{"class":"item_issue"}):
    f.write(i.find_all('a')[0].get('href')+'\n')

f.close()


'''
for i in soup.find_all('a')[:5]:
    print(i.get('href'))


article1='https://news.v.daum.net/v/20210506201322021'

soup2=bs(ur.urlopen(article1,context=contexts).read(),'html.parser')

for i in soup2.find_all("p"):
    print(i.text)


head_line=soup.find_all('div',{"class","item_issue"})
for i in head_line:
    print(i.text,'\n')

    soup3=bs(ur.urlopen(i.find_all("a")[0].get("href"),context=contexts).read(),'html.parser')
    for j in soup3.find_all("p"):
        print(j.text)
'''