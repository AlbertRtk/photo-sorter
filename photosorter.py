from os import listdir
import os.path
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
		
def sortFiles(folder, folderLevel):
	print(folderLevel * "     " + os.path.basename(folder))
	
	content = listdir(folder)
	
	if content:
		folderLevel += 1
		
		for piece in content:
			piecePath = folder + '/' + piece
			
			if os.path.isdir(piecePath):
				sortFiles(piecePath, folderLevel)
			
			elif os.path.isfile(piecePath):
				print(folderLevel * "     " + os.path.split(piece)[1])
				
				if (os.path.splitext(piecePath)[1].lower() == '.jpg'
				or os.path.splitext(piecePath)[1].lower() == '.jpeg'
				or os.path.splitext(piecePath)[1].lower() == '.jpe'):
					print('---> JPEG!!!')
				
				else:
					print(os.path.splitext(piecePath)[1])
			
			else:
				print(folderLevel * "     " + split(piece)[1])
	
	else:
		return

		
#=======================================================================================================================

inputPath = '../../photosorterTEST'

#printTree(inputPath, 0)
print('running...')
sortFiles(inputPath, 0)