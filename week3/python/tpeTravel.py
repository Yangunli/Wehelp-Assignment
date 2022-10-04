import urllib.request as request
import json
from datetime import datetime

src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response)
result=(data["result"]["results"])
with open("data.csv", "w",encoding="utf-8") as file:
    for view in result:
        viewName=view["stitle"]
        address= view["address"].split()
        district=address[1][:3]
        longitude= view["longitude"][:8]
        latitude=view["latitude"][:7]
        photo=view["file"].split("htt")
        firstPhoto="htt"+photo[1]
        postYear=datetime.strptime(view["xpostDate"], '%Y/%m/%d').date().strftime("%Y")
        if int(postYear)>=2015:
            file.write(f'{viewName},{district},{longitude},{latitude},{firstPhoto}\n')
            
       
