import xlrd
import sys,getopt
from plistlib import *


def readExls(sh):
	'''
	try to open workbook and read it to get info 
       return as a list  
	'''
	nrows = sh.nrows
	return [ sh.row_values(i) for i in range(nrows)]

def main():
	'''\n---------------------------------
turn EXLs 2 Plist 
-i : input the target file
-o : output the target file
-s : input the numbers of sheets this workbook has
-h : get help
enjoy~ 
---------------------------------
	'''
	Plist_name = ''
	Exls_name = ''
	Sheet_num = 1
	opt ,args = getopt.getopt(sys.argv[1:],'hi:o:n:')  #h

	for op,values in opt :
		if op =='-i':
			Exls_name = values
		elif op =='-o':
			Plist_name = values
		elif op =='-n':
			Sheet_num = int (values)
		elif op =='-h':
			print main.__doc__
			return
	try:
		wb = xlrd.open_workbook(Exls_name)
	except IOError:
		print 'there is not exits this file'
		return

	pl = [] 
	for Index in range(Sheet_num):
		sh = wb.sheet_by_index(Index)
		result = readExls(sh)
		plist = dict(map(lambda item: (str(item[0]),item[1]),result))
		print plist
		plname = '%sSheet%s.plist' %(Exls_name.split('.')[0],Index+1)
		pl.append(plname)
		writePlist(plist, plname)
	print 'output files:\n%s' %'\n'.join(pl)
	#print main.__doc__	

if __name__ == '__main__':	
	main()