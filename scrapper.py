from bs4 import BeautifulSoup
import requests
import re
from pprint import pprint


page=requests.get("https://www.timeanddate.com/weather/germany")

# Getting the page and creating a beautiful soup object out of it.
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)

# Using find function to get the table object
table=soup.find("table",class_="zebra fw tb-wt zebra va-m")
tableRow=table.find_all("tr")
#print("table body----->",tableRow,type(tableRow),len(tableRow))

tempData=[]
p=0

for row in tableRow:
    #print("each row data------>",row.text.encode('utf-8'),row,type(row.text.encode('utf-8')),type(row),row,type(row.text))
    if p != 0:
        td = row.find_all('td')
        city1='j'
        temperature1='k'
        for cell in td:
            city=cell.find("a",href=re.compile("weather/germany/"))
            #print('value in cell',cell.attrs,len(cell.attrs),type(cell))
            if len(cell.attrs) > 0:
                #print('class',cell.attrs['class'],type(cell.attrs['class']),cell.attrs['class'][0])
                if cell.attrs['class'][0] == 'rbi':
                    #print('found',cell.text,type(cell.text),cell.text.encode('utf-8'),cell.string)
                    temperature1 = cell.string[0:2]
                    a={
                        'city':city1,
                        'temperature': temperature1
                    }
                    tempData.append(a)
            if city is None:
                pass
                #print("Blank row")
            else:
                #print("Getting city-->",city.text)
                city1=city.text
    else:
        #print('Blank r')
        p=p+1
pprint(tempData)
