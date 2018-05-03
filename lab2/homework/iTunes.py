from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

url="https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)
raw_data=conn.read()
text = raw_data.decode("utf8")

soup = BeautifulSoup(text,"html.parser")
s = soup.find("section","section chart-grid")
d = s.find("div","section-content")
ul= d.find("ul")

li_list=ul.find_all("li")
songs_list=[]

# for li in li_list:
#     a1=li.h3.a
#     name = a1.string
#     a2=li.h4.a
#     artist = a2.string
#     a3=li.strong
#     num=a3.string
#     song={
#     "Num":num,
#     "Name":name,
#     "Artist":artist
#     }
#     songs_list.append(song)
# pyexcel.save_as(records=songs_list,dest_file_name="song.xlsx")

for li in li_list:
    a1=li.h3.a
    name = a1.string
    a2=li.h4.a
    artist = a2.string
    options = {
        'default_search': 'ytsearch',
        'max_downloads': len(li_list),
        'format': 'bestaudio/audio'
    }
    dl = YoutubeDL(options)
    dl.download([name, "- ", artist, "official video"])
