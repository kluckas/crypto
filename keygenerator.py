from math import *
import os
import time
import random

fin = open("primes.txt" , "r")
primelist = fin.readlines()
fin.close()

length = len(primelist)-1 

p = int(primelist[random.randint(100,length)])

def find_p_q():
	q = int(primelist[random.randint(100,length)])
	if p==q:
		q = int(primelist[random.randint(100,length)])
	else:
		logdiff = abs(log(p,2) - log(q,2))
		if logdiff<30 and logdiff>0.1:
			return int(q)
		else:
			return find_p_q()

q = find_p_q()

N = p*q
phi = (p-1)*(q-1)

def no_common_divisors(n1,n2):
	while n1>sqrt(n2):
		if (float(n2)/float(n1))%1 == 0 :
			return False
		else : n1=n1-1
	return True

def find_e():
	e = int(primelist[random.randint(100,length)])
	if no_common_divisors(e,phi):
		return e
	else:
		return find_e()

e = find_e()


def mod_inverse(a, b):
    r = -1
    B = b
    A = a
    eq_set = []
    full_set = []
    mod_set = []

    #euclid's algorithm
    while r!=1 and r!=0:
        r = b%a
        q = b//a
        eq_set = [r, b, a, q*-1]
        b = a
        a = r
        full_set.append(eq_set)

    for i in range(0, 4):
        mod_set.append(full_set[-1][i])

    mod_set.insert(2, 1)
    counter = 0

    #extended euclid's algorithm
    for i in range(1, len(full_set)):
        if counter%2 == 0:
            mod_set[2] = full_set[-1*(i+1)][3]*mod_set[4]+mod_set[2]
            mod_set[3] = full_set[-1*(i+1)][1]

        elif counter%2 != 0:
            mod_set[4] = full_set[-1*(i+1)][3]*mod_set[2]+mod_set[4]
            mod_set[1] = full_set[-1*(i+1)][1]

        counter += 1

    if mod_set[3] == B:
        return mod_set[2]%B
    return mod_set[4]%B
d = mod_inverse(e,phi)

fout = open("temporary_key.txt", "w")
fout.write("RSA-module\n")
rsamodule=(str(N)+"\n")
fout.write(rsamodule)
publicpart=(str(e)+"\n")
fout.write("public part\n")
fout.write(publicpart)
privatepart=(str(d)+"\n")
fout.write("private part\n")
fout.write(privatepart)
fout.write(time.strftime("%c"))
fout.close()

print "RSA-Module: " + str(N) + " public part: " + str(e) + " private part: " + str(d) + " " + time.strftime("%c") + "\n"
