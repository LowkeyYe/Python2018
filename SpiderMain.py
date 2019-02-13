from CxExtractor import CxExtractor 
from bs4 import BeautifulSoup
import re
import chardet
import urllib

class SpiderMain:
    def __init__(self,name="周琦凡",pageNum=20):
        self.name = name
        self.pageNum = pageNum
    def getSearchList(self,name,pageNum):
        page = 0
        html_list = list()
        while pageNum-page>10:
            html = urllib.request.quote("https://www.baidu.com/s?wd="+str(name)+"&pn="+str(page),safe=";/?:@&=+$,",encoding="utf-8")
            print(html)
            page = page + 10
            user_agent="Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13 "
            header={'User-Agent':user_agent}
            req = urllib.request.Request(html,headers=header)
            response = urllib.request.urlopen(req)   
            html_content = response.read().decode('UTF-8') 
            soup = BeautifulSoup(html_content,'html.parser',from_encoding='utf-8')
            soup1 = soup.find_all('div',class_='result c-container ')
            for soup2 in soup1:
                link = soup2.find('h3',class_='t').find('a')['href']
            #    print(link)
                html_list.append(link)
        return html_list
    def crawl(self,html_list):
        output = list()
        cx = CxExtractor(threshold=180,blocksWidth=3)
        for html in html_list:
            try:
               test_html = cx.getHtml(html)
               #user_agent="Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13 "
               #header={'User-Agent':user_agent}
               #req = urllib.request.Request(html,headers=header)
               #response = urllib.request.urlopen(req)   
               #test_html = response.read().decode('utf-8') 
               content = cx.filter_tags(test_html)
               s = cx.getText(content)
               print(html) 
            except:
                print("抓取异常")
            if s!="This page has no content to extract":
                output.append(s)
        return output  
    def output(self,output):
        id = 0
        while len(output)!=0:
            try:
                fout = open("./data/%s_%s.txt"%(self.name,id),'a')
                fout.write(output.pop())
                id = id +1
            except:
                print("输出非法")
if __name__=="__main__":
  #  name = input("please input your name：")
    spider = SpiderMain('洪金宝')
    html_list = spider.getSearchList(spider.name, spider.pageNum)
    output = spider.crawl(html_list)
    spider.output(output)
    
    
