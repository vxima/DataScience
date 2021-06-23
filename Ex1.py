#Pandas exercise 

from LoadCSV import CSVLoalder


csv = CSVLoalder("recife.csv")
print("The mean of price is: R${:.2f}".format(csv.getMean("price")))
print("The mode of area is:" , csv.getMode("area") , "m^2")

