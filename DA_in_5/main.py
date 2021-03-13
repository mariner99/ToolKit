import pandas as pd 
from pandas_profiling import ProfileReport

df = pd.read_csv('Capm.csv')


print(df)


# Generate Report in 5 mins

profile = ProfileReport(df)

profile.to_file(output_file="capm.html")