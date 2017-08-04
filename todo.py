#!/usr/bin/python3

import sys
import os
import pdb

def man():
	print ("=========  help page  ==========")
	print ("python3 todo.py [OPTION]...")
	print ("\t -a \"TASK\" \n\t\t Add task")
	print ("\t -v \n\t\t List all task")
	print ("\t -s \n\t\t Seek task")
	print ("\n=========  To DO App  ==========")
	sys.exit(1)
############ Append Function #############
def add():
	if len(sys.argv) != 3:
		print ("Add task")
		print ("\t e.g -  python3 todo.py -a \"TASK\"")
	else:
		task = sys.argv[2]
		if os.path.isfile("./task.txt"):
			f=open("./task.txt","a")
			f.write(task + "\n")
			f.close()
			print ("Task added")
		else:
			f=open("./task.txt","w")
			f.write(task + "\n")
			f.close()
			print ("Task added")
############ Display Function #############
def display():
	if os.path.isfile("task.txt"):
		f=open("task.txt","r")
		print (f.read())
		f.close()
	else:
		print ("File not exist \t Please add task first")

###### Main Function #########
def main():
	if len(sys.argv) <= 1 :
		man()
	elif len(sys.argv) >= 1 :
		if (sys.argv[1]=="-a"):
			add()
		elif (sys.argv[1]=="-v"):
			display()

main()
