import requests
import json
import time
import bs4
import os
import lxml
#UA伪装
#UA:user_agent

#success

def getAddress(url):
    headers={'User-Agent':'dhashdsi'}
    response = requests.get(url,headers=headers)#伪装，防止反爬
    return response

def getInfor(url):
    response=getAddress(url)
    response.encoding='utf-8'
    soup= bs4.BeautifulSoup(response.text, 'lxml')
    pageList=soup.select('.box_con >div>dl>dd')#此处可以更改
    i=0
    for page in pageList:
        i=i+1
        with open("./Novel/"+str(i)+'.'+page.a.text+'.txt','w',encoding='utf-8') as fp:
            temp=getAddress(url+page.a.get('href'))
            temp.encoding='utf-8'
            tempSoup=bs4.BeautifulSoup(temp.text, 'lxml')
            if(tempSoup!=None):
                words=tempSoup.find('div',id='content').get_text()
                fp.write(words)
                print("第"+str(i)+"章"+'文件下载完成')

def inputData():
    url = "http://www.loubiqu.com/10_10240/"
    getInfor(url)


if __name__=="__main__":
    #find_ink=re.compile(r'<a class="(.*?)" href="(.*?)">')#创建正则表达式对象，表示规则（字符串的模式)
    inputData()





