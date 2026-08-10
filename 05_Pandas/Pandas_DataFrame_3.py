import numpy as np
import pandas as pd

#DataFrame Methods
#value_counts(series and dataframe)
marks = pd.DataFrame([
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,70,14],
    [80,70,14],
],columns=['iq','marks','package'])

print(marks)
