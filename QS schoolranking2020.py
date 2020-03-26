import requests
from bs4 import BeautifulSoup
import bs4
def getHTMLText(url):
    try:
        r = requests.get("https://www.dxsbb.com/news/16131.html")
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
        #print(r.text)  这里必须是return，不能用print
    except:
        return "failed to get content"
def FILLUNIVERSITYLIST(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr("td")
            ulist.append([tds[0].string,tds[1].string,tds[2].string])

def PRINTUNIVERSITYLIST(ulist,num):
    print("{:^10}\t{:^6}\t{:^10}".format("ranking","name of University","Country"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0],u[1],u[2]))
        



def main():
    uinfo = []
    url = "https://www.dxsbb.com/news/16131.html"
    html =  getHTMLText(url)
    FILLUNIVERSITYLIST(uinfo,html)
    PRINTUNIVERSITYLIST(uinfo,1000) #top 20 universities
main()
