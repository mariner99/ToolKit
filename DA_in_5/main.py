import pandas as pd 
from pandas_profiling import ProfileReport

df = pd.read_csv('Capm.csv')


#print(df)


#Generate Report

profile = ProfileReport(df)

profile.to_file(output_file="capm.html")