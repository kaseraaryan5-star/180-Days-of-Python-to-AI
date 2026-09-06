import pandas as pd
df = pd.read_csv('/Users/aryankasera/Desktop/100-Days-AI/07_Machine_learning.py/train.csv')
print(df.head())

from ydata_profiling import ProfileReport
prof = ProfileReport(df)
prof.to_file(output_file='output.html')