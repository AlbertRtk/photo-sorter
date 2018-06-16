#=======================================================================================================================
#=== functions supporting methodes of class MyFiles ====================================================================
#=======================================================================================================================
#=== Albert Ratajczak ==================================================================================================
#=== Last update: 2018-06-16 ===========================================================================================
#=======================================================================================================================

import os

# function prints text with defined number of tabs before (to mark the level of directory in the tree)
def printLeveled(text, level):
	print(level * "\t" + text)
	
#-----------------------------------------------------------------------------------------------------------------------

# function prints text with right alignment
def printR(text):
	print("{:>96}".format(text))
		
#-----------------------------------------------------------------------------------------------------------------------

# function renames file from format name.ext to name_xxx.ext (xxx in number)
def renameDuplicat(fileName, orderN):
	splitedName = os.path.splitext(fileName)
	newName = splitedName[0] + '_' + '{:03}'.format(orderN) + splitedName[1]
	printR("renaming to: " + newName)
	return newName
	
#=== end of file =======================================================================================================