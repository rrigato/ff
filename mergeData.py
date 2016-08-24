import pandas as pd
import numpy as np


class quarterBack:
	'''
		This class loads each year of data into memory and transforms
		the data 
		
		The outcome variable for quarterbacks is yards per game
		
		All quarterbacks must have a minimum of 200 pass attempts per season
	'''
	def __init__(self):
		self.loadData()
	def loadData(self):
		self.twenty15 = pd.read_csv("C:/Users/Punkiehome1/Downloads/qbResearch/qb2015.csv")
		self.twenty14 = pd.read_csv("C:/Users/Punkiehome1/Downloads/qbResearch/qb2014.csv")
		self.twenty13 = pd.read_csv("C:/Users/Punkiehome1/Downloads/qbResearch/qb2013.csv")
		self.twenty12 = pd.read_csv("C:/Users/Punkiehome1/Downloads/qbResearch/qb2013.csv")
		print("World")
		
	def changeName(self):

if __name__ == "__main__":
	qbObj = quarterBack()
	