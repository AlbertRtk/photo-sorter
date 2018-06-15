#=======================================================================================================================
#=== class MyFiles - stors paths to input and output directories with files you want to sort============================
#=======================================================================================================================
#=== Albert Ratajczak ==================================================================================================
#=== Last update: 2018-06-15 ===========================================================================================
#=======================================================================================================================

import os
import time
import shutil

class MyFiles:

	# nFiles - counting total number of sorted files
	# nDuplicats - counting number of duplicats
	nFiles = int()
	nDuplicats = int()
	
	def __init__(self, inputPath, outputPath):
		assert (os.path.exists(inputPath)), "Input directory does NOT exist!"
		self.inputPath = inputPath
		self.outputPath = outputPath
	
	
#=== Methodes ==========================================================================================================
	
	# empty methode
	def emptyFunc(self):
		return
	
#-----------------------------------------------------------------------------------------------------------------------	
	
	# methode dirsTree lists the tree of directories in inputPath
	# if fullTree is True, files will be listed too
	# if you want to do any operations on files, set fullTree = True and give function func
	def dirsTree(self, dirLevel = 0, fullTree = False, func = emptyFunc):
		
		# print name of current directory with some space in fron to mark its level (dirLevel)
		print(dirLevel * "\t" + os.path.basename(self.inputPath))
	
		# table with content of current directory
		content = os.listdir(self.inputPath)
	
		# if directory is not empty
		if content:
			dirLevel += 1
			
			# for each element in directory, create new MyFiles object
			for piece in content:
				piecePath = MyFiles(os.path.join(self.inputPath, piece), self.outputPath)
				
				# if piecePath is directory, recursion of sorting methode sortFiles
				if os.path.isdir(piecePath.inputPath):
					piecePath.dirsTree(dirLevel, fullTree, func)
				
				# if piecePath is not directory, but fullTree = True
				elif fullTree:
					print(dirLevel * "\t" + os.path.split(piece)[1])
					func(piecePath)
				else:
					continue
		
		# if directory is empty
		else:
			return
	
#-----------------------------------------------------------------------------------------------------------------------
	
	# methode sortFile sorts (copies) file from inputPath to directory named by its modification date in outputPath
	def sortFile(self):
	
		# get the file extension in lowercase amd file name
		fileExt = os.path.splitext(self.inputPath)[1].lower()
		fileName = os.path.basename(self.inputPath)
		
		sortExt = ['.jpg', '.jpeg', '.jpe']
					
		# if file is JPEG, set outpud directory name as file date of modification
		# if file is not JPEG - output directory "other"
		if any([fileExt == e for e in sortExt]):
			modificationTime = os.path.getmtime(self.inputPath)
			outputDir = time.strftime('%Y-%m-%d', time.localtime(modificationTime))	
		else:
			outputDir = 'other' 
		
		# path to outputDir and full path - dstName - copy destination file
		outputDirPath = os.path.join(self.outputPath, outputDir)
		dstName = os.path.join(outputDirPath, fileName)

		# checking for duplicats, if file already exists in destination directory, change outputDir and the name of file
		if os.path.exists(dstName):
			MyFiles.nDuplicats += 1
			outputDir = 'duplicats'
			outputDirPath = os.path.join(self.outputPath, outputDir)
			fileName = '{:03}'.format(MyFiles.nDuplicats) + '_' + fileName
			dstName = os.path.join(outputDirPath, fileName)
			
		# check if output directory exists and, if not, create it
		if not os.path.exists(outputDirPath):
			os.makedirs(outputDirPath)
		
		# copy the file to new destination
		shutil.copy2(self.inputPath, dstName)
		MyFiles.nFiles += 1
		print("{:>96}".format("copied to: " + outputDir))
	
#-----------------------------------------------------------------------------------------------------------------------	
	
	# methode sortFiles sorts files (copy) from inputPath and all sub-directories into outputPath
	def sortFiles(self):
		print("\n{:=^96}".format(' Sorting your files '))
		self.dirsTree(fullTree = True, func = MyFiles.sortFile)
		print(96 * "=")
		print("\n{} files sorted in total, incuding {} duplicat(s)\n".format(MyFiles.nFiles, MyFiles.nDuplicats))
		MyFiles.nFile = 0
		MyFiles.nDuplicats = 0
	
#-----------------------------------------------------------------------------------------------------------------------
	
	# methode renameDirs renames all directories in inputPath directory (no other subdirectories are renamed)
	# initial name hase to be in format: day.month.year
	# new name will be: year-month-day
	def renameDirs(self):
	
		# print name of current directory
		print('Current directory: ' + os.path.basename(self.inputPath))
		
		# table with content of current directory
		content = os.listdir(self.inputPath)
		
		# if directory is not empty
		if content:
		
			# for each element in directory
			for piece in content:
			
				# if element is directory, print its current name and split it (dmy - from: day.month.year)
				if os.path.isdir(self.inputPath + '/' + piece):
					print(piece, end = "")
					dmy = piece.split('.')
					
					# if dmy has 3 parts, create new name in form y-m-d and rename the directory
					# if dmy doesn't have 3 parts, don't change the name
					if len(dmy) == 3:
						newName = dmy[2] + '-' + dmy[1] + '-' + dmy[0]
						os.rename(self.inputPath + '/' + piece, self.inputPath + '/' + newName)
						print(" - new name: " + newName)
					else:
						print(" - not changed")
						
		# if directory is empty
		else:
			print('The directory is empty.')
	
#=== end of file =======================================================================================================	