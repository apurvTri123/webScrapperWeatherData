from bs4 import BeautifulSoup
import requests
import re


page=requests.get("https://www.timeanddate.com/weather/germany")

# Getting the page and creating a beautiful soup object out of it.
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
# Using find function to get the table object
table=soup.find("table",class_="zebra fw tb-wt zebra va-m")
table2=soup.find_all("table")
print("Table i and 2 ",len(table),len(table2))
print(type(table),type(table2),type(soup))
tableRow=table.find_all("tr")
# print("table body----->",tableRow,type(tableRow),len(tableRow))
tempData=[]

for row in tableRow:
    # print("each row data------>",row.text.encode('utf-8'),type(row.text.encode('utf-8')),type(row),row,type(row.text))
    
    city=row.find("a",href=re.compile("weather/germany/"))
    if city is None:
        print("Blank or header row")
    else:
        print("Getting city",city.text.encode("utf-8"),type(city))
    
    temp=row.find("td",class_="rbi")
    if temp is None:
        print("none recieved",row)
    else:
        # print("temp---->",temp.text.encode('utf-8'),temp.text.encode('utf-32'),type(temp.text.encode('utf-8')))
        text=temp.text.encode('utf-8')
        # print("text-->",text)
        if text != "N/A":
            text=text[0:2]
            # print("text-->2",text)
        a={
            "city": city.text.encode("utf-8"),
            "Temperature": text
        }
        tempData.append(a)
        print("dict",a)
        # print("List updated--->",tempData)
    
# print("Data gathered----.",tempData)
