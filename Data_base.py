import sys
i=0
import PASSWORD
print("Welcome to SD setup")
print("Enter your preset password")
INPUT=input("")
if INPUT==PASSWORD.PASSfunc["password"]:
	print("acsess granted")
	i=5
else:sys.exit()

def Open(file,mode):
	f=open(file, mode)
	print(f.read())
	return
INPUT2=0
while i>0:
	INPUT=input("type mkdir to make a new file or open to open a file type cmd for all commands:")
	if INPUT=="open":
		INPUT2==input("Enter mode type r for reading a for editing and w for writing a new file:")
		INPUT=input("Enter file name:")
		print("sorry this has been disabled")		
	if INPUT=="exit":
		sys.exit()

	if INPUT=="cmd":
		print("type 'exit' for exiting the program, dir to view all files")

	#if INPUT=="dir":	
		