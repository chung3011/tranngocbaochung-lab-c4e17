from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url="http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)
raw_data=conn.read()
text = raw_data.decode("utf8")

soup = BeautifulSoup(text,"html.parser")
# header
tblGridData=soup.find("table",id='tblGridData')
td_list = tblGridData.find_all("td")
header_list=[]
for td in td_list:
    header = td.string
    header_list.append(header)
# print(header_list)

# content
tableContent = soup.find("table",id="tableContent")
td_list=tableContent.find_all("td")
content_list=[]
for td in td_list:
    name_content = td.string
    content_list.append(name_content)
# print(content_list)
table=[]
for i in range(len(header_list)-1):
    for j in range(i,len(content_list),13):
        dict={
        header_list[i]:content_list[j]
        }
        table.append(dict)

pyexcel.save_as(records=table,dest_file_name="vnm.xlsx")
