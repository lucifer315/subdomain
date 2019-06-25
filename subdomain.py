import requests
from bs4 import BeautifulSoup
import re
#create by lucifer315

url = input( 'url(如baidu.com): ' )
head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
ip = 'http://site.ip138.com/{}'.format( url )
domain_url = url
domain = 'http://site.ip138.com/{}/domain.htm'.format( domain_url )
file_name=url+'子域名.txt'
r = requests.get( domain,headers = head )
html=r.text

soup=BeautifulSoup(html, "html.parser")
soup=soup.body.div
soup=soup.find('div',class_='panels')
for i in soup.find_all('p'):    #find_all()方法后不能再次用find_all()方法，请注意和find()方法的搭配前后顺序
	name=i.find('a')
	link=name.get_text('title')
	print(link)
	f=open(file_name,'a')
	f.write(link+'\r')  #若将数据写入txt文件时使用 \n 无法换行则使用 \r\n(回车+换行)
	f.close()