from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url="http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)
raw_data=conn.read()
text = raw_data.decode("utf8")

# f = open("vnm.html","wb")
# f.write(raw_data)
# f.close()

soup = BeautifulSoup(text,"html.parser")

# # header
# tblGridData=soup.find("table",id='tblGridData')
# td_list = tblGridData.find_all("td")
# header_list=['']
# for td in td_list:
#     if td and td.string is not None:
#         header = td.string.strip()
#         header_list.append(header)
# header_list.remove("Tăng trưởng")
# print(header_list)

# content
tableContent = soup.find("table",id="tableContent")
tr_list=tableContent.find_all("tr")
table=[]

for tr in tr_list:
    td_list=tableContent.find_all("td")
    dict={}
    if td_list and td_list[0].string is not None:
        dict['Title'] = (td_list[0].string.strip())
        dict['4-2016'] = (td_list[1].string)
        dict['1-2017'] = (td_list[2].string)
        dict['2-2017'] = (td_list[3].string)
        dict['3-2017'] = (td_list[4].string)
    if dict:
        table.append(dict)

pyexcel.save_as(records=table,dest_file_name="vnm.xlsx")
