import random
print('''Let's play!
p: player, k: key, g: gate
press w to move up
press s to move down
press a to move left
press d to move right
press 0 to exit''')
while True:
    p=[random.randint(0, 3),random.randint(0,3)]
    k=[random.randint(0, 3),random.randint(0,3)]
    g=[random.randint(0, 3),random.randint(0,3)]
    if p[0]==k[0] and p[1]==k[1]:
        continue
    elif p[0]==g[0] and p[1]==g[1]:
        continue
    elif k[0]==g[0] and k[1]==g[1]:
        continue
    else:
        break
for i in range(4):
    for j in range(4):
        if i==p[1] and j==p[0]:
            print('p',end=" ")
        elif i==k[1] and j==k[0]:
            print('k',end=" ")
        elif i==g[1] and j==g[0]:
            print('g',end=" ")
        else:
            print("_",end=" ")
    print()
while True:
    p_input=input("move:")
    if p_input=="w":
        if p[1]>0:
            p[1]=p[1]-1
        else:
            print('out of map')
            continue
    elif p_input=="d":
        if p[0]<3:
            p[0]=p[0]+1
        else:
            print('out of map')
            continue
    elif p_input=="s":
        if p[1]<3:
            p[1]=p[1]+1
        else:
            print('out of map')
            continue
    elif p_input=="a":
        if p[0]>0:
            p[0]=p[0]-1
        else:
            print('out of map')
            continue
    elif p_input=="0":
        break
    else:
        print("error")
        continue
    for i in range(4):
        for j in range(4):
            if i==p[1] and j==p[0]:
                print('p',end=" ")
            elif i==k[1] and j==k[0]:
                print('k',end=" ")
            elif i==g[1] and j==g[0]:
                print('g',end=" ")
            else:
                print("_",end=" ")
        print()
    if p[0]==k[0] and p[1]==k[1]:
        k[0]=5
        k[1]=5
        print("get key")
    if p[0]==g[0] and p[1]==g[1]:
        if k[0]!=5 and k[1]!=5:
            print("forgot key")
            continue
        g[0]=5
        g[1]=5
        print("win")
        break
