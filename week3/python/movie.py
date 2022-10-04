import urllib.request as req
import bs4 
import re
regex = r"^\[([^\]]+)\]"
total=[]
isOk=[]
isSoso=[]
def getData(url):
    request = req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    
    root=bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div",class_="title")
  
    for title in titles:
        if title.a != None:
            isFilter = re.split(regex ,title.a.string)
            if len(isFilter) >2:  
                if isFilter[1] =="好雷":
                    total.append(title.a.string)
                    total.append("\n")
                elif isFilter[1] =="普雷":
                    isOk.append(title.a.string)
                    isOk.append("\n")
                elif isFilter[1] == "負雷":
                    isSoso.append(title.a.string)
                    isSoso.append("\n")
    nextLink= root.find("a", string="‹ 上頁")
    return(nextLink["href"])
pageUrl ="https://www.ptt.cc/bbs/movie/index.html"
count=0
while count<10:
    pageUrl="https://www.ptt.cc/"+getData(pageUrl)
    count+=1
total.extend(isOk)
total.extend(isSoso)
with open("movie.txt", "w",encoding="utf-8") as file:
    for item in total:
        file.write(item)
