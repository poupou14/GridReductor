#!/usr/bin/python 
import os,string, sys
import copy
#import chardet
#### SPECIFIC IMPORT #####
sys.path.append("../Import/xlrd-0.7.1")
sys.path.append("../Import/xlwt-0.7.2")
sys.path.append("../Import/pyexcelerator-0.6.4.1")

from pyExcelerator import *
import xlrd
import xlwt
import Grid
from xlrd import open_workbook
from xlwt import Workbook,easyxf,Formula,Style
from Grid import Grid

def onlyascii(char):
    if ord(char) <= 0 or ord(char) > 127: 
	return ''
    else: 
	return char

def isnumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

class GridSource():

	def __init__(self, fileName_p): 
    		self.__workbook = open_workbook(fileName_p)
    		self.__grids = None
		self.__worksheet = self.__workbook.sheet_by_name('Grid')
		
	def getGrids(self) :
		self.__grids = []
		nbRows_l = self.__worksheet.nrows - 1
		nbCols_l = self.__worksheet.ncols - 1
		currRow_l = -1 # start at first line
		while currRow_l < nbRows_l:
			grid_l = Grid()
			currRow_l += 1
			row_l = self.__worksheet.row(currRow_l)
#print 'Row:', currRow_l
			if self.__worksheet.cell_type(currRow_l, 0) != 0 : # not emty cell
				currCol_l = -1 # first col
				while currCol_l < nbCols_l:
					currCol_l += 1
					# Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
					cellType_l = self.__worksheet.cell_type(currRow_l, currCol_l)
					cellValue_l = self.__worksheet.cell_value(currRow_l, currCol_l)
#print '	', cellType_l, ':', cellValue_l
					if currCol_l == 0 :
						grid_l.setBet(cellValue_l)
					else :
						grid_l.setNextCell(cellValue_l, cellType_l)

				self.__grids.append(copy.deepcopy(grid_l))

			else :
				nbRows_l = currRow_l
		
		return self.__grids




def open_excel_sheet():
    """ Opens a reference to an Excel WorkBook and Worksheet objects """
    workbook = Workbook()
    worksheet = workbook.add_sheet("Sheet 1")
    return workbook, worksheet

def write_excel_header(worksheet, title_cols):
    """ Write the header line into the worksheet """
    cno = 0
    for title_col in title_cols:
        worksheet.write(0, cno, title_col)
        cno = cno + 1
    return

def write_excel_row(worksheet, rowNumber, columnNumber):
    """ Write a non-header row into the worksheet """
    cno = 0
    for column in columns:
        worksheet.write(lno, cno, column)
        cno = cno + 1
    return

def save_excel_sheet(workbook, output_file_name):
    """ Saves the in-memory WorkBook object into the specified file """
    workbook.save(output_file_name)
    return

