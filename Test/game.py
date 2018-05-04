import random

while True:
    e=[[random.randint(0, 3),random.randint(0,3)],[random.randint(0, 3),random.randint(0,3)]]
    if e[0][0]==e[1][0] and e[0][1]==e[1][1]:
        continue
    else:
        break
print(e)

hit = []
for i in range(4):
    for j in range(4):
        print("_",end=" ")
    print()

count_e=2
count_r=5

loop=True
loop1=True

while loop:
    count=0
    check=0
    n=input("Nhập vào hoành độ (0-3) và tung độ (0-3) của đạn ( cách nhau bằng dấu cách): ")
    if n=="out":
        break
    num=list(n)

    for i in n:
        if i <= "/" or i >= ":":
            num.remove(i)
    # print(num)
    if len(num)!=2:
        print("Nhập lại!")
        continue

    r=[int(num[0]),int(num[1])]
    # print(r)
    if r[0] > 3 or r[1] > 3:
        print("Nhập lại!")
        continue

    if len(hit)==0:
        for i in range(4):
            for j in range(4):
                if i==r[1] and j==r[0]:
                    if r[0]==e[0][0] and r[1]==e[0][1]:
                        print('x',end=" ")
                    elif r[0]==e[1][0] and r[1]==e[1][1]:
                        print('x',end=" ")
                    else:
                        print("_",end=" ")
                else:
                    print("_",end=" ")
            print()
    else:
        for i in range(4):
            for j in range(4):
                if i==hit[0][1] and j==hit[0][0]:
                    print('o',end=" ")
                elif i==r[1] and j==r[0]:
                    if r[0]==e[0][0] and r[1]==e[0][1]:
                        print('x',end=" ")
                    else:
                        print("_",end=" ")
                else:
                    print("_",end=" ")
            print()

    count_r=count_r-1

    for ei in e:
        if ((r[0]-1)==ei[0] and (r[1]-1)==ei[1]):
            count=count+1
        if (r[0]==ei[0] and (r[1]-1)==ei[1]):
            count=count+1
        if ((r[0]+1)==ei[0] and (r[1]-1)==ei[1]):
            count=count+1
        if ((r[0]-1)==ei[0] and r[1]==ei[1]):
            count=count+1
        if ((r[0]+1)==ei[0] and r[1]==ei[1]):
            count=count+1
        if ((r[0]-1)==ei[0] and (r[1]+1)==ei[1]):
            count=count+1
        if (r[0]==ei[0] and (r[1]+1)==ei[1]):
            count=count+1
        if ((r[0]+1)==ei[0] and (r[1]+1)==ei[1]):
            count=count+1


        if r[0]==ei[0] and r[1]==ei[1]:
            count_e=count_e-1
            print("hit")
            check=1
            hit.append(ei)
            e.remove(ei)
            # print(e)
            # print(hit)
    if check==0:
        print("miss")

    if count_r < 1:
        if count_e > 0:
            print("lose")
            loop = False
        else:
            print("win")
            loop = False
    elif count_e < 1:
        print("win")
        loop = False

    print(count,"enemy(s) around")
    print(count_r,"rocket(s) left")
    print(count_e,"enemy(s) left")
    continue
