from os import listdir
from os.path import isdir, basename

def printTree(folder, folderLevel):
	print(folderLevel * "     " + basename(folder))
	content = listdir(folder)
	if not content:
		return
	else:
		folderLevel += 1
		for piece in content:
			piecePath = folder + '/' + piece
			if isdir(piecePath):
				printTree(piecePath, folderLevel)
			else:
				print(folderLevel * "     " + piece)

inputPath = '../../photosorterTEST'

printTree(inputPath, 0)