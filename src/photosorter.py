#=======================================================================================================================
#=== photosorter - order and sort your photos ==========================================================================
#=======================================================================================================================
#=== Albert Ratajczak ==================================================================================================
#=== Last update: 2018-06-16 ===========================================================================================
#=======================================================================================================================
#=======================================================================================================================

from myfiles import *

# define input and outpup path
# input path has to exist, output will be created
inputPath = 'F:/tosort'
outputPath = 'F:/sorted'

# instance of class MyFiles with input and output path
myPhotos = MyFiles(inputPath, outputPath)

# adding extensions of files you want to sort
# methode takes set instance as input
myPhotos.addExt({'.jpg', '.jpeg', '.jpe'})

# sorting files according to date of modification
myPhotos.sortFiles()

#== end of file ========================================================================================================