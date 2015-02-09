from math import *
from time import *
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


privatepart=1373
publicpart=1721
rsamodul=263713


alpha={'A':0, 'a':1, 'B':2, 'b':3, 'C':4, 'c':5, 'D':6, 'd':7, 'E':8, 'e':9, 'F':10, 'f':11, 'G':12, 'g':13, 'H':14, 'h':15, 'I':16, 'i':17, 'J':18, 'j':19, 'K':20, 'k':21, 'L':22, 'l':23, 'M':24, 'm':25, 'N':26, 'n':27, 'O':28, 'o':29, 'P':30, 'p':31, 'Q':32, 'q':33, 'R':34, 'r':35, 'S':36, 's':37, 'T':38, 't':39, 'U':40, 'u':41, 'V':42, 'v':43, 'W':44, 'w':45, 'X':46, 'x':47, 'Y':48, 'y':49, 'Z':50, 'z':51, '!':52, '?':53, '\n':54, '.':55, '0':56, '1':57, '2':58, '3':59, '4':60, '5':61, '6':62, '7':63, '8':64, '9':65, '=':66, ' ':67, '+':68, '-':69, ',':70, ':':71}
beta=['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', '!', '?', '\n', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '=', ' ', '+', '-', ',', ':']

print bcolors.FAIL + "Please notice that every output will be written in a new file named 'output.txt'. Be sure to have no file with the same name in the directory because it will be deleted\n" + bcolors.ENDC
time.sleep(5)

def cipher_mode():
	os.system('clear')
	cm = int(raw_input("If you want to cipher a message please press 1. If you want to decipher please press 2.\n"))
	if cm==1 or cm==2:
		return cm 
	else:
		print "Apparently you are not able to read carefully. You dumbf*ck ! Please try again.\n"
		time.sleep(5)
		return cipher_mode()

ciphermode=cipher_mode()

def input_mode():
	os.system('clear')
	im = int(raw_input("If you want to input manually please press 1. If you want to input a file please press 2.\n"))
	if im==1 or im==2:
		return im 
	else:
		os.system('clear')
		print "Apparently you are not able to read carefully. You Dumbf*ck. Please try again.\n"
		time.sleep(5)
		return input_mode()

inputmode=input_mode()

def input_list():
	inlist = []
	if ciphermode==1 and inputmode==1:
		instring = raw_input("Please give the message you want to cipher\n")
		for char in instring:
			inlist.append(alpha[char])
			return inlist			
	elif ciphermode==1 and inputmode==2:
		infilevar = raw_input("Please give the name of the file you want to cipher as 'name.txt'\n")
		fin = open(infilevar, "r")
		instring = fin.read()
		for char in instring:
			inlist.append(alpha[char])
			return inlist
	elif ciphermode==2 and inputmode==1:
		instring = raw_input("Please give the message you want to decipher as '1234:5678' and so on.\n")
		delimiter = ":"
		inlist = instring.split(delimiter)
		return inlist
	elif ciphermode==2 and inputmode==2:
		infilevar= raw_input("Please give the name of the file you want to decipher as 'name.txt' Be sure that the file is written in RSA-Standard e.g. '1234:5678'. Do not use linebreaks!\n")
		fin = open(infilevar , "r")
		instring = fin.read()
		fin.close()
		delimiter = ":"
		prelist = instring.split(delimiter)
		for element in prelist:
			return inlist

inputlist = input_list()

def cipher():
	outputlist=[]
	for element in inputlist:
		outelement=(element**publicpart) % rsamodul
		outputlist.append(outelement)
	return outputlist

def decipher():
	outputlist=[]
	for element in inputlist:
		outelement = (element**privatepart) % rsamodul
		outputlist.append(beta[outelement])
	return outputlist

def output():
	fout = open("output.txt" , "w")
	if ciphermode==1:
		ol = cipher()
		delimiter = ":"
		outstring = delimiter.join(ol)
		fout.write(outstring)
	if ciphermode==2:
		ol=decipher()
		delimiter = ""
		outstring = delimiter.join(ol)
		fout.write(outstring)
	fout.close()	
		
output()
