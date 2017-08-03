import sys
import os 
import pdb




if len(sys.argv) == 1 :
	print ("Provide argumanet")
	print ("-a for append with string")
	print ("-v for display")
	sys.exit(1)

if len(sys.argv) >= 1:
	first = sys.argv[1]
	if (first == "-a"):
	     if not sys.argv[2]:
	 	print ("Give String")
	     else:
		string = sys.argv[2]
		file1=open("test.txt",'a') 
		file1.write(string + "\n")
		file1.close()
		print ("Done")
	elif (first == "-v"):
		f2=open("test.txt",'r')
		print (f2.read()) 
	else :
		print ("Give Correct Argument ")
		print ("-a for append with string")
		print ("-v for display")


# crete todo
# -a add
# -d delete
# -v display
# -u update task
# -t time track 
# -v version
# -tag tag to taks like [home,office, sport]
# https://etherpad.openstack.org/p/python_todo
# https://github.com/amolkhat/Python_Basics
# https://pymbook.readthedocs.io
#	
