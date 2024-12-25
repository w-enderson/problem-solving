import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')


data = pd.read_csv("../../../data/atmosfera.csv", delimiter=",")

data["data"] = pd.to_datetime(data["DATA"], format="%d de %b de %y")
print(data.head)


# a) a série é estacionária?

plt.plot(data["data"], data["temperatura"])
plt.title("Variação da temperatura ao longo do tempo")
plt.xlabel("Tempo")
plt.ylabel("temperatura")
plt.grid()
plt.show()

# Não, há uma tendência em determinados intervalos da série.

#
#

# b) a primeira e segunda diferença são estacionárias?

data["first_diff"] = data["temperatura"].diff()

plt.plot(data["data"], data["first_diff"])
plt.title("Variação da temperatura ao longo do tempo")
plt.xlabel("Tempo")
plt.ylabel("temperatura")
plt.grid()
plt.show()


data["second_diff"] = data["temperatura"].diff()

plt.plot(data["data"], data["second_diff"])
plt.title("Variação da temperatura ao longo do tempo")
plt.xlabel("Tempo")
plt.ylabel("temperatura")
plt.grid()
plt.show()

# sim, ambas são estacionárias.


