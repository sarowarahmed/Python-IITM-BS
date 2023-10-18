n = input()
a = False
if len(n)== 10 and int(n[0])>5 and n.isdigit():
    for i in range(10):
        if n.count(n[i])<8:
            a = True
            if n[i]*6 in n:
                a = False
                break
        else:
            break
if a:
    print('valid')  
else:
    print('invalid')              



            
