#Pandas exercise 

from sys import modules
import numpy as np
import pandas as pd
import statistics as st
from LoadCSV import CSVLoalder


csv = CSVLoalder("recife.csv")
def Q1():
    print("The mean of price is: R${:.2f}".format(csv.getMean("price")))
    print("The mean of area is:{:.2f}".format(csv.getMean("area")) , "m^2")

def Q2():
    print("IQR of area: {:.2f}".format(csv.IQR("area")))

def Q3():
    csv.CreatePriceMeter()
    print(csv.file.head())

def Q4():
    print("The mean of price/meter is: R${:.2f}".format(csv.PriceMeterOnlyApart()))
    
Q1()
Q2()
Q3()
Q4()


