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
    
def Q5():
    print("O bairro mais barato é:", csv.cheapestSuburb()[0] , "com preço por m^2:" , csv.cheapestSuburb()[1])
    print("O bairro mais caro é:", csv.expensivestSururb()[0] , "com preço por m^2:" , csv.expensivestSururb()[1])
def Q6():
    print("A variavel mais correleta com o preço é a:" , csv.corrSpearman("price"))
#Q1()
#Q2()
#Q3()
#Q4()
Q5()
#Q6()



