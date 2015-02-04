from math import *
from time import *
import getpass
import os
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


os.system('clear')

def input_code():
	code = raw_input('What schall your code be?\n')
	os.system('clear')
	codelist=[]
	for char in code:
		codelist.append(char)
	return codelist

def input_mode():
	mode=int(raw_input('If you want to enter a message manually press 1. If you want to input a .txt-file as message please press 2.\n'))
	if mode==1 or mode==2:
		os.system('clear')
		return mode 
	else:
		os.system('clear')
		print bcolors.FAIL + 'You are too dumb to read! Do it again!\n' + bcolors.ENDC
		return input_mode() 
		
messagelist=list()

def input_message():
	message = raw_input('What message do you want to encrypt/decrypt?\n')
	messagelist.append(message)
	os.system('clear')
	return messagelist
	
cwlist = input_code()
ciphermode=input_mode()
melist=list()

def input_file():
	varfilename = raw_input('Please give the name of the file you want to input, as filename.txt\n')
	os.system('clear')
	fin = open(varfilename , 'r')
	finstring = fin.read()
	return finstring
def get_output_mode():
	mode=int(raw_input('If you want to get the output message in terminal press 1. If you want to print it to a file press 2.\n'))
	if mode==1 or mode==2:
		os.system('clear')
		return mode
	else:
		os.system('clear')
		print bcolors.FAIL + 'You are too dumb to read! Do it again!\n' + bcolors.ENDC
		return get_output_mode()
		
if ciphermode==1:
	message=input_message()
	
else:
	message=input_file()

outputmode = get_output_mode()
if outputmode==2:
	outfilename=raw_input('Please give the name of the output file\n')
	os.system('clear')

for word in message:
		for char in word:
			melist.append(char)

#delt=0
#mlen=len(melist)

#def delete_chars(t):
	#if melist[t].islower():
		#del melist[t]
		#t=t+1
		#if t<=(len(melist)-1):
			#return delete_chars(t)
		#else:
			#return melist
	#else:
		#t=t+1
		#if t<=(len(melist)-1):
			#return delete_chars(t)
		#else:
			#return melist
	
alpha={'A':0, 'a':1, 'B':2, 'b':3, 'C':4, 'c':5, 'D':6, 'd':7, 'E':8, 'e':9, 'F':10, 'f':11, 'G':12, 'g':13, 'H':14, 'h':15, 'I':16, 'i':17, 'J':18, 'j':19, 'K':20, 'k':21, 'L':22, 'l':23, 'M':24, 'm':25, 'N':26, 'n':27, 'O':28, 'o':29, 'P':30, 'p':31, 'Q':32, 'q':33, 'R':34, 'r':35, 'S':36, 's':37, 'T':38, 't':39, 'U':40, 'u':41, 'V':42, 'v':43, 'W':44, 'w':45, 'X':46, 'x':47, 'Y':48, 'y':49, 'Z':50, 'z':51, '!':52, '?':53, '\n':54, '.':55, '0':56, '1':57, '2':58, '3':59, '4':60, '5':61, '6':62, '7':63, '8':64, '9':65, '=':66, ' ':67, '+':68, '-':69, ',':70, ':':71}
beta=['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', '!', '?', '\n', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '=', ' ', '+', '-', ',', ':']

def cipher_parameter():
	print 'If you want to cipher your message, press 1. If you want to decipher it, press 2.\n'
	cip = int(raw_input())
	if cip == 1 or cip == 2:
		os.system('clear')
		return cip
	else:
		os.system('clear')
		print bcolors.FAIL + 'You are too dumb to read. Do it again!\n' + bcolors.ENDC
		return cipher_parameter()

cpar=cipher_parameter()

def cipher_parameter2():
	print 'If you want to use the autokeysystem, press 1. If you do not want to use it, press 2\n'
	cip =int(raw_input())
	if cip == 1 or cip == 2:
		os.system('clear')
		return cip
	else:
		os.system('clear')
		print bcolors.FAIL + 'You are too dumb to read. Do it again!\n' + bcolors.ENDC
		return cipher_parameter2()
		
cpar2=cipher_parameter2()

def cipher():
	clen = len(cwlist)
	ciphered_message_int=[]
	ciphered_message_list=[]
	ct=0
	for char in melist:
		cint = int(alpha[char])+int(alpha[cwlist[ct]])
		ct = (ct+1) % clen
		ciphered_message_int.append(cint)
	for integer in ciphered_message_int:
		cint = integer % 72
		ciphered_message_list.append(beta[cint])
	delimiter=''
	ciphered_message = delimiter.join(ciphered_message_list)
	return ciphered_message

def cipher_autokey():
	clen = len(cwlist)
	mlen = len(melist)
	ciphered_message_int=[]
	ciphered_message_list=[]
	ct=0
	for char in melist:
		if ct<clen:
			cint = int(alpha[char])+int(alpha[cwlist[ct]])
			ct = (ct+1) 
			ciphered_message_int.append(cint)
		else:
			mt = (ct-clen) % mlen
			cint = int(alpha[char])+int(alpha[melist[mt]])
			ciphered_message_int.append(cint)
	for integer in ciphered_message_int:
		cint = integer % 72
		ciphered_message_list.append(beta[cint])
	delimiter=''
	ciphered_message = delimiter.join(ciphered_message_list)
	return ciphered_message
		
def decipher():
	clen = len(cwlist)
	deciphered_message_int=[]
	deciphered_message_list=[]
	dt=0
	for char in melist:
		dint = int(alpha[char])-int(alpha[cwlist[dt]])
		dt = (dt+1) % clen
		deciphered_message_int.append(dint)
	for integer in deciphered_message_int:
		dint = integer % 72
		deciphered_message_list.append(beta[dint])
	delimiter=''
	deciphered_message = delimiter.join(deciphered_message_list)
	return deciphered_message	
	
def decipher_autokey():
	clen = len(cwlist)
	mlen = len(melist)
	deciphered_message_int=[]
	deciphered_message_list=[]
	dt=0
	for char in melist:
		if dt<clen:
			cint = int(alpha[char])-int(alpha[cwlist[dt]])
			dt = (dt+1) 
			deciphered_message_int.append(cint)
		else:
			mt = (dt-clen) % mlen
			dint = int(alpha[char])-int(alpha[melist[mt]])
			deciphered_message_int.append(dint)
	for integer in deciphered_message_int:
		cint = integer % 72
		deciphered_message_list.append(beta[cint])
	delimiter=''
	deciphered_message = delimiter.join(deciphered_message_list)
	return deciphered_message
	
	
def job():
	if cpar==1 and cpar2==1:
		return cipher_autokey()
	elif cpar==1 and cpar2==2:
		return cipher()
	elif cpar==2 and cpar2==1:
		return decipher_autokey()
	elif cpar==2 and cpar2==2:
		return decipher()
	else:
		return 'Something went terribly wrong!'

def job_output():
	if outputmode==1:
		print job()
	else:
		fout=open(outfilename , 'w')
		fout.write(job())
		fout.close()	

job_output()
