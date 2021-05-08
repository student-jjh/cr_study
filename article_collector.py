import os, codecs, re, datetime,requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs
import ssl

contexts = ssl._create_unverified_context()
news='https://news.daum.net/'
f=open(str(datetime.date.today())+'article.txt','w')


soup=bs(ur.urlopen(news,context=contexts).read(),'html.parser')
for i in soup.find_all('div',{'class':'thumb_relate'}):
    try:
        f.write(i.text+'\n')
        f.write(i.find_all('a')[0].get('href')+'\n')

        soup2=bs(ur.urlopen(i.find_all('a')[0].get('href'),context=contexts).read(),'html.parser')

        for j in soup2.find_all('p'):
            f.write(j.text)
    except:
        pass

f.close()