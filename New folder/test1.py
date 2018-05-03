while True:
    n=input("Nhập vào 1 dãy số, cách nhau bởi dấu cách: ")
    num=list(n)
    for i in n:
        if i != " " and (i <= "/" or i >= ":"):
            num.remove(i)
    if len(num)>0:
        break
    else:
        print("Hãy nhập lại dãy số !")

while num[0] == " " :
    del num[0]
# print(num)
while num[len(num)-1] == " " :
    del num[len(num)-1]
# print(num)
for i in range(len(num)):
    if (i+1) < (len(num)+1) :
        if num[i] == " " and num[i+1] == " " :
            continue
        elif num[i] != " ":
            print(num[i],end="")
        else:
            print()
