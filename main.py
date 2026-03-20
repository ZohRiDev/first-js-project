
for n in range(1, 100):
    n2 = bin(n)[2:] 
   
    if len(n2) < 2:
        continue

    
    if n2.count("1") % 2 == 0:
       
        s = "10" + n2[2:] + "0"
    else:
       
        s = "11" + n2[2:] + "11"
        
    r = int(s, 2) 
    
    if r < 99:
       ans = n
       print(ans) # Сегодня выходной