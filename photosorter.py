#from os import listdir
#import os.path
from myfiles import *

'''
def printTree(folder, folderLevel):
	print(folderLevel * "     " + os.path.basename(folder))
	content = listdir(folder)
	if content:
		folderLevel += 1
		for piece in content:
			piecePath = folder + '/' + piece
			if os.path.isdir(piecePath):
				printTree(piecePath, folderLevel)
			else:
				print(folderLevel * "     " + os.path.split(piece)[1])
	else:
		return
'''
		
#=======================================================================================================================

inputPath = '../../photosorterTEST'
outputPath = ''

print('running...')
myPhotos = MyFiles(inputPath, outputPath)
myPhotos.sortFiles()

