import requests
import re
import json
import time
import bs4
import os
import lxml
#UA伪装
#UA:user_agent

#success

def getAddress(url):
    headers={'User-Agent':'dhasshdsi'}#随便打的
    response = requests.get(url,headers=headers)#伪装，防止反爬
    return response



def getInfor(url,page):
    response=getAddress(url)
    soup= bs4.BeautifulSoup(response.text, 'lxml')
    allPic=soup.findAll('a',class_='directlink largeimg')#此处可以更改
    i=0
    for Pic in allPic:
        i=i+1
        with open("./Data/"+"第"+str(page)+"页"+str(i)+'.jpg','wb') as fp:
            temp=getAddress(Pic.get('href'))
            fp.write(temp.content)
            print("第"+str(page)+"页"+str(i)+'号文件下载完成')

def inputData():
    url = "https://k##onacha##n.com/post?page={}&tags="#这个网址（自己处理一下）仅供学习
    for i in range(1,10):#页面
        temp=url.format(str(i))
        getInfor(temp,i)


if __name__=="__main__":
    #find_ink=re.compile(r'<a class="(.*?)" href="(.*?)">')#创建正则表达式对象，表示规则（字符串的模式)
    inputData()





