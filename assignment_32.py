#Name: Christopher Mena
#Email: christopher.mena66@myhunter.cuny.edu
#Date: October 21, 2019
#Reads data and plots a figure of fraction of homeless children

#Import libraries
import pandas as pd
import matplotlib.pyplot as plt


def plotHomeless(input_file, outout_file):
	#Read csv
	homeless = pd.read_csv(input_file)

	#Plotting
	homeless["Fraction Children"] = (homeless["Total Children in Shelter"] / (homeless["Total Adults in Shelter"] + homeless["Total Children in Shelter"]))
	homeless.plot(x="Date of Census", y="Fraction Children")

	fig = plt.gcf()
	fig.savefig(outout_file)


#Input
plotHomeless(input("Enter name of input file: "), input("Enter name of output file: "))

