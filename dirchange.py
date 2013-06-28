from os import listdir
from time import sleep

import config

from func import *

import sys
import os
import re

SHOWS = config.SHOWS
# ----------------------------------------------------------- OS Check   -----------------------------------------------------------
if (sys.platform == "win32") :
	print "Running on Windows"
	env = "win"
	DIR = config.DIRECTORY_WIN # directory to watch
	RAR = config.RAR_WIN # path to console winrar
	PSEP = "\\" # path separator
	EXTRACT_TO = config.EXTRACT_TO_WIN
	EXTRACT_TO_DEF = config.EXTRACT_TO_WIN_DEF
else:
	print "Running on a non-Windows OS"
	env = "unix"
	DIR = config.DIRECTORY_LIN
	RAR = "rar"
	EXTRACT_TO_DEF = config.EXTRACT_TO_LIN_DEF

	
print "Watching " + DIR +" for changes..."

while 1:

	dr = listdir(DIR)
	sleep(config.CHECK_EVERY)
	dr2 = listdir(DIR)

	
	if len(dr) < len(dr2):
		print "==ADDED: " 
		chlist_added = [i for i in dr2 if i not in dr]
		
		for new_entry in chlist_added:
			
			full_path_to_new_entry = os.path.join(DIR, new_entry);
			
			if os.path.isdir(full_path_to_new_entry) == True:
				print "  " + full_path_to_new_entry + " --- is a directory - analyzing..."
				
				# new_entry should be matched against the set of rules
				
				new_entry_listing = os.listdir(full_path_to_new_entry);
				
				if checkForRars(new_entry_listing) == True: 
					print "  Folder has rars!"
					
					# now matching with a show 
					
					show_found = None
				
					for show in SHOWS:
						regex = ".*"+show+".*"
						match = re.search(regex, new_entry)
						if match:
							show_found = show
							break;
							
					if show_found:
						print "  FOUND " + show_found
						EXTRACT_TO = os.path.join(EXTRACT_TO, getFolderName(show_found))
						
						print "  The folder is: " + EXTRACT_TO
						
					else:
						print "  No matches found."
						EXTRACT_TO = EXTRACT_TO_DEF
						print "  The folder is: " + EXTRACT_TO
							

					main_rar = os.path.join(full_path_to_new_entry, getMainRar(new_entry_listing))
					print "  " + main_rar
					#unrar(main_rar, RAR, EXTRACT_TO)

			
			
			else:
				print "  " + new_entry + " --- is a file (ignoring)"
		
		
	if len(dr) > len(dr2):
		chlist_removed = [i for i in dr if i not in dr2]
		print "==REMOVED: " 
		print chlist_removed
			

