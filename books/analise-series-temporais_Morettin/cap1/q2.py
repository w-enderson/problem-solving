import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("../../../data/ICV.csv", delimiter=",")
print(data.shape)

data["data"] = pd.to_datetime(data["Mes/ano"], format="%m/%y")
print(data.describe()) 

# a ) A série é estacionária?

plt.figure(figsize=(10,6))
plt.plot(data["data"], data["ICV"])
plt.title("Variação do ICV ao longo do tempo")
plt.xlabel("Tempo")
plt.ylabel("ICV")
plt.grid()
plt.show()

# série não é estacionária, a tendência crescente é facilmente percebida.

#
#

# b) A primeira diferença é estacionária?

data["first_diff"] = data["ICV"].diff()

plt.figure(figsize=(10,6))
plt.plot(data["data"], data["first_diff"])
plt.title("Variação do ICV ao longo do tempo (primeira diferença)")
plt.xlabel("Tempo")
plt.ylabel("ICV")
plt.grid()
plt.show()

# Não é estacionária. Uma tendência crescente ainda é notável, na série.

#
#

# c) a segunda diferença é estacionária?

data["second_diff"] = data["first_diff"].diff()

plt.figure(figsize=(10,6))
plt.plot(data["data"], data["second_diff"])
plt.title("Variação do ICV ao longo do tempo (primeira diferença)")
plt.xlabel("Tempo")
plt.ylabel("ICV")
plt.grid()
plt.show()

# Não é estacionária. Há mudança na variância conforme o tempo passa.



