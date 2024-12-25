import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


column_names = ["preco"]
data = pd.read_csv("../../../data/D-PETRO.csv", delimiter=",", names=column_names)
data["data"] = pd.date_range(start="1995-01-03", periods=len(data["preco"]), freq="D")



# a) a série é estacionária? tem tendência?

plt.plot(data["data"], data["preco"])
plt.grid()
plt.show()

# Não é estacionária e possui tendência;

#
#

# b) a primeira diferença é estacionária?

data["first_diff"] = data["preco"].diff()

plt.plot(data["data"], data["first_diff"])
plt.grid()
plt.show()

# Não, a variância muda conforme o tempo passa;

#
#

# c) a transformaçao logarítma é estacionária?

data["log_transf"] = np.log(data["preco"])

plt.plot(data["data"], data["log_transf"])
plt.grid()
plt.show()

# Não é estacionário, há tendência;

#
#

# d) a primeira diferença da transformação logaritma é estacionária?

data["first_diff_log_transf"] = data["log_transf"].diff()

plt.plot(data["data"], data["first_diff_log_transf"])
plt.grid()
plt.show()

# é estacionária.

