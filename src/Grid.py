#!/usr/bin/python 
import os,string, sys
import time
import xlrd
import copy

class Grid():
	def __init__(self):
		self.__bet = ""
		self.__cells = []
		self.__counter = 0

	def setBet(self, bet_p):
		self.__bet = ""
		self.__bet = ''.join((self.__bet, bet_p))

	def setNextCell(self, cell_p, cellType_p) :
		if cellType_p == xlrd.XL_CELL_EMPTY:
			value_l = ""
		elif cellType_p == xlrd.XL_CELL_TEXT:
			value_l = cell_p
		elif cellType_p == xlrd.XL_CELL_NUMBER:
			valuef_l = float(cell_p)
			value_l = "%.8f" % valuef_l
		
		self.__cells.append(value_l)

	def getBet(self) :
		return self.__bet

	def getDiff(self, otherGrid_p) :
		size_l = len(self.__bet)
		otherBet_l = otherGrid_p.getBet()
		diff_l = 0
		try :
			for index_l in range(1, size_l) :
				if self.__bet[index_l] != otherBet_l[index_l] :
					diff_l += 1
		except :
			diff_l = -1

		return diff_l

	def __str__(self):
		output_l = ""
		output_l = ''.join((output_l, self.__bet))
		for index_l in range(0, len(self.__cells)) :
			output_l = ''.join((output_l, ";"))
			output_l = ''.join((output_l, self.__cells[index_l]))
		output_l = ''.join((output_l, "\n"))
		return output_l.replace(".", ",")



