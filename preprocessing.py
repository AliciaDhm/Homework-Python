import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

main_path = "C:/Users/HP/OneDrive/Bureau/M1 Eco Stat/S2/Python - ML"
cars_path = main_path + "/used_cars_data.csv"
df = pd.read_csv(cars_path, sep=",")

# garder seulement la première moitié
df = df.iloc[:len(df)//2].copy()

# sauvegarder le CSV réduit dans le même dossier
csv_path = main_path + "/used_cars_data_shorter.csv"
df.to_csv(csv_path, index=False)