from sys import modules
import numpy as np
import pandas as pd
import statistics as st

class CSVLoalder:
    def __init__(self , fileCSV):
        self.file = pd.read_csv(fileCSV).fillna(0)#fill missing data with 0
        self.CreatePriceMeter()
    
    def getMean(self, column):
        return st.mean(self.file[column]) 
    
    def getMedian(self, column):
        return st.median(self.file[column]) 

    def getMode(self, column):
        return st.mode(self.file[column]) 

    def getVar(self, column):
        return st.var(self.file[column]) 

    def IQR(self, column):
        arr = np.array(self.file[column])
        #get the quartils
        q1 = np.percentile(arr , 25 , interpolation='midpoint')
        q3 = np.percentile(arr , 75 , interpolation='midpoint')
        return q3 - q1
    
    def CreatePriceMeter(self):
        self.file["Price/Meter"] = round(self.file["price"]/self.file["area"], 2)

    def PriceMeterOnlyApart(self):
        return st.mean(self.file[self.file["type"] == "apart"]["Price/Meter"])
    
    def cheapestSuburb(self):
        GS = self.file.groupby("suburb")["Price/Meter"].min()
        return (GS.idxmin() , GS.min() )
    def expensivestSururb(self):
        GS = self.file.groupby("suburb")["Price/Meter"].max()
        return (GS.idxmax() , GS.max() )
    def corrSpearman(self, column):
        return self.file.corr(method='spearman')[self.file.corr(method='spearman')['price'] < 1.0]["price"].idxmax()
        
        
        