#!/usr/bin/python 
import os,string, sys


class Reductor():
	def __init__(self, gridListSource_p, coef_p ):
		self.__gridListSource = gridListSource_p
		self.__coef = coef_p

	def getReducedList(self) :
		listSize_l = len(self.__gridListSource)
		reducedList_l = []
		print "Reductor : list Size init %f" % listSize_l
		print "Reductor : coef %f" % self.__coef
		reducedList_l.append(self.__gridListSource[1])
		reducedListSize_l = len(reducedList_l)
		indexDisplayPct_l = 1
		#print "reducedListSize_l : %f" % reducedListSize_l
		for index_l in range(1, listSize_l) :
			sizeReducedList_l = len(reducedList_l)
			minDiff_l = 7
			pct_l =  index_l / listSize_l * 100
			if pct_l > indexDisplayPct_l :
				indexDisplayPct_l += 1
				print "%.0f pct" % pct_l
			for indexReducedList_l in range(0, sizeReducedList_l) :
				diff_l = self.__gridListSource[index_l].getDiff(reducedList_l[indexReducedList_l])

				if diff_l < minDiff_l :
					if minDiff_l >= self.__coef :
							minDiff_l = diff_l
							#print "Diff = %.0f" % minDiff_l
							#print "Grille 1 :"
							#print self.__gridListSource[index_l]
							#print "Grille 2 :"
							#print reducedList_l[indexReducedList_l]
			if minDiff_l >= self.__coef :
				reducedList_l.append(self.__gridListSource[index_l])
				#print self.__gridListSource[index_l]
		reducedListSize_l = len(reducedList_l)
		print "Reductor : final reduced list size %f" % reducedListSize_l
		return reducedList_l
