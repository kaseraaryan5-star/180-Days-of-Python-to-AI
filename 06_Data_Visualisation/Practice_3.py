import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

batsman = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/06_Data_Visualisation/sharma-kohli.csv')
print(batsman)

#colors(hex) 
print(plt.plot(batsman['index'],batsman['V Kohli'],color='blue'))
print(plt.plot(batsman['index'],batsman['RG Sharma'],color='black'))

print(plt.title('Rohit Vs Kohli Carrer Comparison'))
print(plt.xlabel('Season'))
print(plt.ylabel('Runs Scored'))
print(plt.tight_layout())
print(plt.show())

#line(width and style)
print(plt.plot(batsman['index'],batsman['V Kohli'],color='blue',linestyle='dashed'))
print(plt.plot(batsman['index'],batsman['RG Sharma'],color='black',linestyle='dashed'))

print(plt.title('Rohit Vs Kohli Carrer Comparison'))
print(plt.xlabel('Season'))
print(plt.ylabel('Runs Scored'))
print(plt.tight_layout())
print(plt.show())

print(plt.plot(batsman['index'],batsman['V Kohli'],color='blue',linestyle='dotted'))
print(plt.plot(batsman['index'],batsman['RG Sharma'],color='black',linestyle='dotted'))

print(plt.title('Rohit Vs Kohli Carrer Comparison'))
print(plt.xlabel('Season'))
print(plt.ylabel('Runs Scored'))
print(plt.tight_layout())
print(plt.show())

print(plt.plot(batsman['index'],batsman['V Kohli'],color='blue',linestyle='dashdot'))
print(plt.plot(batsman['index'],batsman['RG Sharma'],color='black',linestyle='dashdot'))

print(plt.title('Rohit Vs Kohli Carrer Comparison'))
print(plt.xlabel('Season'))
print(plt.ylabel('Runs Scored'))
print(plt.tight_layout())
print(plt.show())

print(plt.plot(batsman['index'],batsman['V Kohli'],color='blue',linestyle='dashed',linewidth=6))
print(plt.plot(batsman['index'],batsman['RG Sharma'],color='black',linestyle='dashed',linewidth=4))

print(plt.title('Rohit Vs Kohli Carrer Comparison'))
print(plt.xlabel('Season'))
print(plt.ylabel('Runs Scored'))
print(plt.tight_layout())
print(plt.show())

