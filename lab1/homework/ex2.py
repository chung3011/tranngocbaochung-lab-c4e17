from matplotlib import pyplot
# data
os = [18,4,2]
# labels
types = ["Window","Mac","Linux"]
# draw
pyplot.pie(os,labels=types,autopct="%.2f%%",shadow=True, explode=[0,0.1,0.2])
# autopct tính phần trăm
# explode tách pie
pyplot.title("OS")
# pyplot.suptitle("---------------------")
pyplot.axis("equal") # chỉnh trục bằng nhau
# show
pyplot.show()
