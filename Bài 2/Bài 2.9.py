print("Nguyễn Hồng Pháp")
print("MSSV: 235752020710006")
print("#####################")
str=input("Enter a String:")
dict = {}
for n in str:
    keys = dict.keys()
    if n in keys:
        dict[n] += 1
    else:
        dict[n] = 1
print (dict)
