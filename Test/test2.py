num = [1,4,1,64,2,128,5,4,7,32]
print("Trong dãy số: ")
print(*num,sep=', ')
print("Có những cặp số có tích bằng 64 là:")
for i in range (len(num)):
    for j in range (len(num)-1,i,-1):
        if num[i]*num[j] == 64:
            print("{0} và {1} tại vị trí {2} và {3}".format(num[i],num[j],i+1,j+1))
