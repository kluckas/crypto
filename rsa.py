from math import *
import os

alpha={'A':0, 'a':1, 'B':2, 'b':3, 'C':4, 'c':5, 'D':6, 'd':7, 'E':8, 'e':9, 'F':10, 'f':11, 'G':12, 'g':13, 'H':14, 'h':15, 'I':16, 'i':17, 'J':18, 'j':19, 'K':20, 'k':21, 'L':22, 'l':23, 'M':24, 'm':25, 'N':26, 'n':27, 'O':28, 'o':29, 'P':30, 'p':31, 'Q':32, 'q':33, 'R':34, 'r':35, 'S':36, 's':37, 'T':38, 't':39, 'U':40, 'u':41, 'V':42, 'v':43, 'W':44, 'w':45, 'X':46, 'x':47, 'Y':48, 'y':49, 'Z':50, 'z':51, '!':52, '?':53, '\n':54, '.':55, '0':56, '1':57, '2':58, '3':59, '4':60, '5':61, '6':62, '7':63, '8':64, '9':65, '=':66, ' ':67, '+':68, '-':69, ',':70, ':':71}
beta=['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', '!', '?', '\n', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '=', ' ', '+', '-', ',', ':']

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def input_mode():
	"""Declares if a file is used as input or a manual input"""
	mode=int(raw_input('If you want to enter a message manually press 1. If you want to input a .txt-file as message please press 2.\n'))
	if mode==1 or mode==2:
		os.system('clear')
		return mode 
	else:
		os.system('clear')
		print bcolors.FAIL + 'You are too dumb to read! Do it again!\n' + bcolors.ENDC
		return input_mode() 

ciphermode=input_mode()		
messagelist=list()
melist=list()

def input_message():
	message = raw_input('What message do you want to encrypt/decrypt?\n')
	messagelist.append(message)
	os.system('clear')
	return messagelist
	
def input_file():
	varfilename = raw_input('Please give the name of the file you want to input, as filename.txt\n')
	os.system('clear')
	fin = open(varfilename , 'r')
	finstring = fin.read()
	return finstring
	
if ciphermode==1:
	message=input_message()
	
else:
	message=input_file()
	
for word in message:
		for char in word:
			melist.append(char)
			
private_part=1373
public_part=1721
rsamodul=263713

def cipher():
	ciphered_message_int=[]
	for char in melist:
		cint = (int(alpha[char])**public_part) % rsamodul
		ciphered_message_int.append(cint)
	return ciphered_message_int

def decipher():
	deciphered_message_int=[]
	for char in melist:
		cint = (int(alpha[char])**private_part) % rsamodul
	return deciphered_message_int

fout = open("rsaoutput.txt", "w")
def job():
	output=cipher()
	for element in output:
		out=str(element)+" "
		fout.write(out)

job()
#TODO : Die Ausgabe des ciphers ist eine Reihe von Zahlen diese müssen jetzt noch sinnvoll in eine Liste gepackt werden beim wiedereinlesen zur entschluesselung.
#also aendern des einlese algorithmus in abhaengigkeit was gemacht werden soll.  sollte durch abfrage und wechsel zwischen delimiter "" und " " gehen.
fout.close()
