theIndex = {'a':[1],'b':[98]}
def addword(word,pagenum):
	# theIndex.setdefault(word,pagenum)
	# else:
	# 	theIndex[word]=[pagenum]
	theIndex.setdefault(word,[]).append(pagenum)
addword('b',8)


print theIndex 
print 'gg'