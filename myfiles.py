#=======================================================================================================================
#=== class MyFiles - stors paths to input and output directories with files you want to sort============================
#=======================================================================================================================
#=== Albert Ratajczak ==================================================================================================
#=== Last update: 2018-06-11 ===========================================================================================
#=======================================================================================================================

import os
import time
import shutil

class MyFiles:

	def __init__(self, inputPath, outputPath):
		self.inputPath = inputPath
		self.outputPath = outputPath
		#self.nFiles = 0
	
	
#=== Methodes ==========================================================================================================
	
	# methode renameDirs renames all directories in inputPath directory (no other subdirectories are renamed)
	# initial name hase to be in format: day.month.year
	# new name will be: year-mont-day
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
	
	
	
	# methode sortFiles sorts files (copy) from inputPath into outputPath
	def sortFiles(self, dirLevel = 0):
	
		# print name of current directory with some space in fron to mark its level (dirLevel)
		print(dirLevel * "     " + os.path.basename(self.inputPath))
	
		# table with content of current directory
		content = os.listdir(self.inputPath)
	
		# if directory is not empty
		if content:
			dirLevel += 1
			
			# for each element in directory, create new MyFiles object
			for piece in content:
				piecePath = MyFiles(self.inputPath + '/' + piece, self.outputPath)
			
				# if piecePath is directory, recursion of sorting methode sortFiles
				if os.path.isdir(piecePath.inputPath):
					piecePath.sortFiles(dirLevel)
				
				# if piecPath is file, get it extension and check if it is JPEG
				else: #os.path.isfile(piecePath.inputPath):
					fileExt = os.path.splitext(piecePath.inputPath)[1].lower()
					
					# if file is JPEG, set outpud directory name as file date of modification
					# if file is not JPEG - output directory "other"
					if ( fileExt == '.jpg' or fileExt == '.jpeg' or fileExt == '.jpe'):
						modificationTime = os.path.getmtime(piecePath.inputPath)
						modificationTime = time.strftime('%Y-%m-%d', time.localtime(modificationTime))
						outputDir = piecePath.outputPath + '/' + modificationTime
					else:
						outputDir = piecePath.outputPath + '/other' 
				
					# print file name with extension and mark dirLevel with space
					print(dirLevel * "     " + os.path.split(piece)[1], end = "")
					
					# check if output directory exists and, if not, create it
					if not os.path.exists(outputDir):
						os.makedirs(outputDir)
				
					# copy the file to new directory
					shutil.copy2(piecePath.inputPath, outputDir)
					print(" --> copied to: " + outputDir)
		
		# if current directory is empty - return
		else:
			return