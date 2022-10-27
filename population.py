
# Population 

start = 2 

for i in range(1,11) : # using loop to loop over 10 day
    
    if i == 1:
        increasement = 2
    else :
        increasement = start * 0.3
        start += increasement 
    print(f'population in day {i} is {start}')
    
    