#!/usr/bin/python 
import string, sys
from Reductor import Reductor
from GridSource import GridSource


def main():
	if len(sys.argv) == 2 :
		if sys.argv[1] == "-h" :
			print "user help :"
			print "$ GridReductor.sh -s <source_data_file> -o <output_file> [-c <reducing_coef>]"
			exit()
	elif len(sys.argv) == 5 :
		sourceFile_l = sys.argv[2]
		outputFile_l = sys.argv[4]
		coef_l = 1
	elif len(sys.argv) == 7 :
		sourceFile_l = sys.argv[2]
		outputFile_l = sys.argv[4]
		coef_l = int(sys.argv[6])
	else :
		print "user help :"
		print "$ GridReductor.sh -s <source_data_file> -o <output_file> [-c <reducing_coef>]"
		exit()

	print "Lecture fichier Source"
	mySource_l = GridSource(sourceFile_l)
	myGrids_l = mySource_l.getGrids()
	myReductor_l = Reductor(myGrids_l, coef_l)
	print "Generation de la liste de grilles reduite"
	myReducedGrids_l = myReductor_l.getReducedList()
	f1=open(outputFile_l, 'w+')
	f1.write("")
	print "Fichier genere :", outputFile_l
	for index_l in range(0, len(myReducedGrids_l)) :
		f1.write(str(myReducedGrids_l[index_l]))
#	myBets.printFile(outputFile_l)
	
main()
