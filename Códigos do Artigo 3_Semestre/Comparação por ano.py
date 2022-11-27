import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


p = pd.read_excel("C:/Users/Guilherme/Downloads/Dados Formatados2_PI.xlsx")

labels = ['2018', '2019', '2020', '2021', '2022']
total = p["Total das Ocorrências"]

np.random.seed(19680801)

plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
y_pos = np.arange(len(labels))
performance1 = total


error1 = len(labels)


graf1 = ax.barh(y_pos, performance1, align='center', color = 'mediumpurple')
ax.set_yticks(y_pos, labels)

ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Quantidade de casos')
ax.set_ylabel('Anos')
ax.set_title('Total de Ocorrências por ano ')

plt.show()