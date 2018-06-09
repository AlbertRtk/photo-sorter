from os import listdir
import os.path

class MyFiles:

	def __init__(self, inputPath, outputPath):
		self.inputPath = inputPath
		self.outputPath = outputPath
		#self.nFiles = 0
	
	
#=== Methodes ==========================================================================================================
	
	#
	def renameDirs():
		return
	
	
	# methode sortFiles sorts files (copy) from inputPath into outputPath
	def sortFiles(self, dirLevel = 0):
		# print name of current directory with some space in fron to mark its level (dirLevel)
		print(dirLevel * "     " + os.path.basename(self.inputPath))
	
		# table with content of current directory
		content = listdir(self.inputPath)
	
		# if directory is not empty
		if content:
			dirLevel += 1
			
			# for each element in directory 
			for piece in content:
				# create new MyFiles object
				piecePath = MyFiles(self.inputPath + '/' + piece, self.outputPath)
			
				# if piecePath is directory
				if os.path.isdir(piecePath.inputPath):
					# recursion of sorting methode sortFiles
					piecePath.sortFiles(dirLevel)
				
				# if piecPath is file
				elif os.path.isfile(piecePath.inputPath):
					# print file name with extension
					print(dirLevel * "     " + os.path.split(piece)[1])
					
					# if file is JPEG (if you want to change/add a type of sorted files,  
					# replace/add string defining the extension - eg. change '.jpe' to '.png')
					if (os.path.splitext(piecePath.inputPath)[1].lower() == '.jpg'
					or os.path.splitext(piecePath.inputPath)[1].lower() == '.jpeg'
					or os.path.splitext(piecePath.inputPath)[1].lower() == '.jpe'):
						# what to do?
						print('---> JPEG!!!')
				
					# if file is not JPEG (or other defined before)
					else:
						# what to do?
						print(os.path.splitext(piecePath.inputPath)[1])
				
				# if piecPath is neither directory nor file
				else:
				# what to do?
					print(folderLevel * "     " + split(piece)[1])
		
		# if current directory is empty - return
		else:
			return