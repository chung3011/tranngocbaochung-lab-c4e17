numbers = [1,2,3,1,5,54,4,1,64,4,4964,31,646,164,64,161,64,616,4]
num = int(input("Input integer: "))

# in
if num in numbers:
    print("Found in list")
else:
    print("Not found in list")

# count
n=numbers.count(num)
if n > 0:
    print("Found in list")
else:
    print("Not found in list")

# for
for i in numbers:
    if i == num:
        print("Exist")
        # i = 1
        break
else:
    print("None")
# if i != 1:
#     print("Not found")
