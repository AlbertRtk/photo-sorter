# photosorter
# by Albert Ratajczak
# Last update: 2018-06-09

Program helps to sort files in directories according to the date of modification. Intentionaly written to deal with photos (JPEG files).
Projects consists of two files:

	#1	photosorter.py
		Main file of the project.
	
	#2	myfiles.py
		The file with class MyFiles which stors the path to input and output directories.
		The class MyFiles has methodes:
		
		renameDirs(self) - Part of my old photos I stored in directories named dd.mm.yyyy (dmy). Currently, I prefere to name directories in form yyyy-mm-dd (ymd). This methodes renames directories in input directory from form dmy to form ymd. If you worry about your files, make safty copy before using renameDirs.
		
		sortFiles(self, dirLevel = 0) - working on it