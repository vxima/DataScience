from sys import modules
import numpy as np
import pandas as pd
import statistics as st

class CSVLoalder:
    def __init__(self , fileCSV):
        self.file = pd.read_csv(fileCSV)
    
    def getMean(self, column):
        return st.mean(self.file[column]) 
    
    def getMedian(self, column):
        return st.median(self.file[column]) 

    def getMode(self, column):
        return st.mode(self.file[column]) 

    def getVar(self, column):
        return st.var(self.file[column]) 
