def make_list_naturals(n):
    res = []    
    for i in range(n-1):
       res += [True] 
    return res 

def mark_multiples1(i,n,t):
    x = n 
    while x < len(t):
        t[i+x:i+x+1] = [False]
        x += n
    return  
    
def mark_multiples2(i,n,t):
    t[i+n:len(t):n] = [False]*len(t[i+n:len(t):n])
    return 

def filter1(n):
    primes = []
    t = make_list_naturals(n)
    i = 0
    x=2
    while i < (len(t)-1):
       if t[i] == True:
          mark_multiples1(i,x,t)
          primes += [x]
          i += 1
          x += 1
       else:
          i += 1
          x += 1   
    return primes 
    
def filter2(n):
    primes = []
    t = make_list_naturals(n)
    i = 0
    x=2
    while i < (len(t)-1):
       if t[i] == True:
          mark_multiples1(i,x,t)
          primes += [x]
          i += 1
          x += 1
       else:
          i += 1
          x += 1   
    return primes 

def sum_of_primes(n):
    x = n-1
    print sum(filter1(x))
    return sum(filter1(x))

def nthprime(n):
    x = 100*n
    t = filter(x)
    print t[n-1]

fout = open("primes.txt", "w")
primes = filter2(1000)
for element in primes:
	numb= str(element) + '\n'
	fout.write(numb)
fout.close()



         
