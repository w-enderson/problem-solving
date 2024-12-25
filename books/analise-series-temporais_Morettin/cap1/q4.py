import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# data preprocessing

data = pd.read_csv("../../../data/energia.csv", delimiter=",")
data["Ano"] = data["Ano"].ffill().astype(int)

data["data"] = pd.to_datetime(data["Ano"].astype(str) + "-" + data["Mes"].astype(str))
print(data.head)


# a) a série é estacionária? tem tendência?

plt.plot(data["data"], data["Energia"])
plt.grid()
plt.show()

# Não é estacionária e possui tendência crescente;

#
#

# b) a primeira diferença é estacionária?

data["first_diff"] = data["Energia"].diff()

plt.plot(data["data"], data["first_diff"])
plt.grid()
plt.show()

# Não, a variância muda consideravelmente conforme o tempo passa;

#
#

# c) a transformaçao logarítma é estacionária?

data["log_transf"] = np.log(data["Energia"])

plt.plot(data["data"], data["log_transf"])
plt.grid()
plt.show()

# Não é estacionário, há uma tendência crescente;

#
#

# d) a primeira diferença da transformação logaritma é estacionária?

data["first_diff_log_transf"] = data["log_transf"].diff()

plt.plot(data["data"], data["first_diff_log_transf"])
plt.grid()
plt.show()

# é estacionária.
