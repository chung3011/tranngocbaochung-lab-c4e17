print('''Let's play!
| or - : player, E: enemy , S: island
press w to move up
press s to move down
press a to move left
press d to move right
press d to fire
press 0 to exit''')
print()

p=[1,2]
e=[[3,0],[3,3]]
s=[2,2]
m='|'

for i in range(5):
    for j in range(5):
        if i==p[1] and j==p[0]:
            print(m,end=" ")
        elif i==s[1] and j==s[0]:
            print('S',end=" ")
        elif i==e[0][1] and j==e[0][0]:
            print('E',end=" ")
        elif i==e[1][1] and j==e[1][0]:
            print('E',end=" ")
        else:
            print("x",end=" ")
    print()
check=0
while True:
    p_input=input("move:").lower()
    if p_input=="w":
        m='|'
        if p[1]>0:
            p[1]=p[1]-1
            if p[0]==s[0]and p[1]==s[1]:
                print("cant move")
                p[1]=p[1]+1
                continue
            for ei in e:
                if ei[1]<p[1]:
                    if ei[1]<4:
                        ei[1]=ei[1]+1
                    else:
                        ei[1]=ei[1]
                else:
                    if ei[1]>0:
                        ei[1]=ei[1]-1
                    else:
                        ei[1]=ei[1]
        else:
            print('out of map')
            continue
    elif p_input=="d":
        m='-'
        if p[0]<4:
            p[0]=p[0]+1
            if p[0]==s[0]and p[1]==s[1]:
                print("cant move")
                p[0]=p[0]-1
                continue
            for ei in e:
                if ei[0]>p[0]:
                    if ei[0]>0:
                        ei[0]=ei[0]-1
                    else:
                        ei[0]=ei[0]
                else:
                    if ei[0]<4:
                        ei[0]=ei[0]+1
                    else:
                        ei[0]=ei[0]
        else:
            print('out of map')
            continue
    elif p_input=="s":
        m='|'
        if p[1]<4:
            p[1]=p[1]+1
            if p[0]==s[0]and p[1]==s[1]:
                print("cant move")
                p[1]=p[1]-1
                continue
            for ei in e:
                if ei[1]>p[1]:
                    if ei[1]>0:
                        ei[1]=ei[1]-1
                    else:
                        ei[1]=ei[1]
                else:
                    if ei[1]<4:
                        ei[1]=ei[1]+1
                    else:
                        ei[1]=ei[1]
        else:
            print('out of map')
            continue
    elif p_input=="a":
        m='-'
        if p[0]>0:
            p[0]=p[0]-1
            if p[0]==s[0]and p[1]==s[1]:
                print("cant move")
                p[0]=p[0]+1
                continue
            for ei in e:
                if ei[0]<p[0]:
                    if ei[0]<4:
                        ei[0]=ei[0]+1
                    else:
                        ei[0]=ei[0]
                else:
                    if ei[0]>0:
                        ei[0]=ei[0]-1
                    else:
                        ei[0]=ei[0]
        else:
            print('out of map')
            continue
    elif p_input=="f":
        if m=='-':
            if e[0][0]==p[0]:
                e[0][0]=10
                e[0][1]=10
                check = check + 1
            if e[1][0]==p[0]:
                e[1][0]=10
                e[1][1]=10
                check = check + 1
        if m=='|':
            if e[0][1]==p[1]:
                e[0][0]=10
                e[0][1]=10
                check = check + 1
            if e[1][1]==p[1]:
                e[1][0]=10
                e[1][1]=10
                check = check + 1

    elif p_input=="0":
        break
    else:
        print("error")
        continue
    if (e[1][0]==e[0][0] and e[1][1]==e[0][1]):
        e[0][0]=100000
        e[0][1]=100000
        e[1][0]=100000
        e[1][1]=100000
        for i in range(5):
            for j in range(5):
                if i==p[1] and j==p[0]:
                    print(m,end=" ")
                elif i==s[1] and j==s[0]:
                    print('S',end=" ")
                elif i==e[0][1] and j==e[0][0]:
                    print('E',end=" ")
                elif i==e[1][1] and j==e[1][0]:
                    print('E',end=" ")
                else:
                    print("x",end=" ")
            print()
        print("win")
        break
    for i in range(5):
        for j in range(5):
            if i==p[1] and j==p[0]:
                print(m,end=" ")
            elif i==s[1] and j==s[0]:
                print('S',end=" ")
            elif i==e[0][1] and j==e[0][0]:
                print('E',end=" ")
            elif i==e[1][1] and j==e[1][0]:
                print('E',end=" ")
            else:
                print("x",end=" ")
        print()

    if (p[0]==e[0][0] and p[1]==e[0][1]) or (p[0]==e[1][0] and p[1]==e[1][1]):
        print("lose")
        break

    if e[0][0]==s[0] and e[0][1]==s[1]:
        e[0][0]=100000
        e[0][1]=100000
        check = check + 1
    if e[1][0]==s[0] and e[1][1]==s[1]:
        e[1][0]=100000
        e[1][1]=100000
        check = check + 1
    if check == 1:
        print("one enemy die")
    if check == 2:
        print("win")
        break
