str1=input()
str2=input()
merge_str=str1+str2
new_str=''
num='0123456789'
for i in range(len(num)):
    for j in range(len(merge_str)):
        if merge_str[j]==num[i]:
            new_str+=num[i]
print(new_str)