import config
import sys
import os

def getFileExt(s):
	mylist = s.split(".")
	lastpos = len(mylist) -1

	return mylist[lastpos]
	
		
def checkForRars(DIR_LISTING):
	for currentFile in DIR_LISTING:
		if getFileExt(currentFile) == "r01":
			return True;		

def getMainRar(DIR_LISTING):
	for currentFile in DIR_LISTING:
		if getFileExt(currentFile) == "rar":
			return currentFile;

def unrar(file_to_unrar, RAR, EXTRACT_TO):
	os.system(RAR + " e " + file_to_unrar + " "+ EXTRACT_TO)
	
def getFolderName(showname):
	return showname.replace("."," ").title()