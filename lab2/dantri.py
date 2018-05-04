# web scraping/crawling
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url="http://dantri.com.vn"
# 1.1 open connection
conn = urlopen(url)
# 1.2 read data
raw_data=conn.read()
# 1.3 decode
text = raw_data.decode("utf8")
# print(text)

# dan_tri = open("dantri.html","wb")
# dan_tri.write(raw_data)
# dan_tri.close()

# 2 find roi
soup = BeautifulSoup(text,"html.parser")
# print(soup.prettify())
ul = soup.find("ul","ul1 ulnew")
# print(ul.prettify())
li_list=ul.find_all("li")
item_list=[]
for li in li_list:

# li=li_list[0]
# print(li.prettify())

# 3
    a=li.h4.a
# print(a.prettify())
    title = a.string
# print(title)
    link = url + a['href']
    # print(link)
    # print(title)
    # print("-------------------------------------------------------")
    item={
    "title":title,
    "link":link
    }
    item_list.append(item)
    # print(item)
    # print()
# print(item_list)
pyexcel.save_as(records=item_list,dest_file_name="test1.xlsx")
