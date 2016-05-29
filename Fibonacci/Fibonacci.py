def EvenFibonacci(x): 
   n = 1
   nplus = 2
   total = 0
   while nplus <= 4000000:
   	if nplus % 2 == 0:
	   total += nplus
        temp = nplus
        nplus = n + nplus
        n = temp
   
   return total

print EvenFibonacci(0)	
