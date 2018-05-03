from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url="http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)
raw_data=conn.read()
text = raw_data.decode("utf8")

soup = BeautifulSoup(text,"html.parser")

# tblGridData = soup.find("table","tblGridData")
# td_list=tblGridData.find_all("td")
# header_list=[]
# for td in td_list:
#     header = td.string
#     header_list.append(header)

# table = soup.find("table","tableContent")
# tr_list=table.find_all("tr")
# content_list=[]
# for tr in tr_list:
#     name_content = tr.string
#     content_list.append(name_content)
# print(content_list)
# print()


# pyexcel.save_as(records=time_list,dest_file_name="song.xlsx")
