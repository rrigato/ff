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
		self.twenty12 = pd.read_csv("C:/Users/Punkiehome1/Downloads/qbResearch/qb2012.csv")
		self.twenty11 = pd.read_csv("C:/Users/Punkiehome1/Downloads/qbResearch/qb2011.csv")
		self.twenty10 = pd.read_csv("C:/Users/Punkiehome1/Downloads/qbResearch/qb2010.csv")
		
	def changeName(self):
		print(self.twenty15.shape)
		print(self.twenty14.shape)
		print(self.twenty13.shape)
		print(self.twenty12.shape)
		print(self.twenty11.shape)
		print(self.twenty10.shape)

if __name__ == "__main__":
	qbObj = quarterBack()
	qbObj.changeName()
	