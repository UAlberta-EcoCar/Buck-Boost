# -*- coding: utf-8 -*-

#This script analyses the data exported from "buck-boost.asc" ltspice model as a text file
#"buck-boost.asc" simulates the charging of a super capacitor through
#the lt8710 configured as a boost converter

import pandas as pd

df1=pd.read_csv("buck-boost.txt", sep='\t')

df1 = df1.iloc[range(0,len(df1),100),:]

import matplotlib.pyplot as plt

currentout=df1.loc[:,"I(R9)"]#+df1.loc[:,"I(C7)"]
#currentout = currentout.rolling(window=200,center=False).mean()
#plt.plot(df1.loc[:,"time"],currentout)
#plt.show()

powerout=df1.loc[:,"V(out)"]*currentout
powerout = powerout.rolling(window=250,center=False).mean()
plt.plot(df1.loc[:,"time"],powerout)
plt.ylabel('Power Out')
plt.show()

powerin=-1*df1.loc[:,"V(in)"]*df1.loc[:,"I(V1)"]
powerin = powerin.rolling(window=250,center=False).mean()
plt.plot(df1.loc[:,"time"],powerin)
plt.ylabel('Power In')
plt.show()

eff=powerout/powerin*100
plt.plot(df1.loc[:,"time"],eff)
plt.ylabel('Efficiency')
plt.show()