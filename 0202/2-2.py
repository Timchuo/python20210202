import random
n = random.randint(1,20)
counter = 0
while True:
    OMG = int(input('unmber'))
    if OMG>20 or OMG<0:
        print('在哭嗎')
        counter = counter +1
    else:
        if counter == 5:
            print('just 5 times')
            break 
        elif OMG>n:
            print('太大')
            counter =counter+1
        elif OMG<n:
            print('太小')
            counter =counter+1
        else:
            print('bingo!!!')
            counter =counter+1
            print('你猜對了'+str(counter)+'次就猜對了')
            break
        
            
            
            
            
            
            
            