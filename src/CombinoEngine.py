#!/usr/bin/python 
import os,string, sys
import math
import copy
from Bet import Bet

betChoice = ['1', 'N', '2']

class CombinoEngine():

	def __init__(self, grille_p, returnRate_p, expectedEsperance_p, file_p, scndRankRate_p=0, thirdRankRate_p=0): 
		self.__grille = grille_p
		self.__combinoBets = []
		self.__nbTotBet = 0
		self.__nbGenBets = 0
		self.__indexDisplayPct = 0
		self.__currentBet = None
		self.__returnRate = returnRate_p
		self.__returnRate2 = scndRankRate_p
		self.__returnRate3 = thirdRankRate_p
		self.__expectedEsperance = expectedEsperance_p
		self.__file = file_p

	def generateCombinoBets(self):
		gridSize_l = self.__grille.getSize()
		self.__nbTotBet = math.pow(3, gridSize_l)
		#print "Taille Grille : ", gridSize_l
		self.__currentBet = Bet(self.__grille)
		self.__currentBet.setReturnRate2(self.__returnRate2)
		self.__currentBet.setReturnRate3(self.__returnRate3)
		self.genCombinoBetRecurcive(0, 0)
		self.genCombinoBetRecurcive(0, 1)
		self.genCombinoBetRecurcive(0, 2)

	def genCombinoBetRecurcive(self, numGame_p, unNDeux_p):
		self.__currentBet.setChoice(numGame_p, betChoice[unNDeux_p])
		if numGame_p == (self.__grille.getSize() - 1) : # fin de grille
			self.__currentBet.updateEsperanceAndProba()
			if self.__currentBet.getNetEsperance(self.__returnRate, self.__returnRate2, self.__returnRate3) >= self.__expectedEsperance :
				self.__file.write(str(self.__currentBet))
				#self.__combinoBets.append(copy.deepcopy(self.__currentBet))
			self.__nbGenBets += 1
			pct_l =  self.__nbGenBets / self.__nbTotBet * 100
			if pct_l > self.__indexDisplayPct :
				self.__indexDisplayPct += 1
				print "%.0f pct" % pct_l
		else :	
			self.genCombinoBetRecurcive(numGame_p + 1, 0)
			self.genCombinoBetRecurcive(numGame_p + 1, 1)
			self.genCombinoBetRecurcive(numGame_p + 1, 2)
		return
	
	def __str__(self):
		output_l = ""
		for index_l in range(0, len(self.__combinoBets)) :
			output_l = ''.join((output_l, str(self.__combinoBets[index_l])))

		return output_l
