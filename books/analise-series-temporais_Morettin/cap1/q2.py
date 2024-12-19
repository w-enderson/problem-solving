import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../../../data/ICV.csv", delimiter=",")
print(data.shape)

data["Data"] = pd.to_datetime(data["Mes/ano"], format="%m/%y")
print(data.describe()) 

plt.figure(figsize=(10,6))
plt.plot(data["Data"], data["ICV"])

plt.axhline(y=data["ICV"].mean(), color='r', linestyle='--', label=f'Média ICV = {data["ICV"].mean():.2f}')
plt.title("Variação do ICV ao longo do tempo")
plt.xlabel("Tempo")
plt.ylabel("ICV")
plt.grid()
plt.show()

# série não é estacionária
