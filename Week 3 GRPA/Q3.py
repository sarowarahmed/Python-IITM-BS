x = 0
y = 0
sequence = input()
while sequence != 'STOP':
    if sequence == 'UP':
        y+=1
    if sequence == 'DOWN':
        y-=1
    if sequence == 'RIGHT':
        x+=1
    if sequence == 'LEFT':
        x-=1   
    sequence = input()
distance = abs(x)+abs(y)
print(distance)
             


    
        

             
        