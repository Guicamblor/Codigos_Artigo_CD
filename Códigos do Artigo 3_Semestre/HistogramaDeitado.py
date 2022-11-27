import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

p = pd.read_excel("C:/Users/Guilherme/Downloads/Dados Formatados2_PI.xlsx")

labels = ['2018', '2019', '2020', '2021', '2022']
capital = p["Total das Ocorrências registradas na capital"]
demacro = p["Total das Ocorrências registradas na Demacro"]
interior = p["Total das Ocorrências registradas no Interior"]

x = np.arange(len(labels))
width = 0.15  # Tamanho das barras

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/0.65, capital, width, label='Capital', color="plum")
rects2 = ax.bar(x + width/2, demacro, width, label='Demacro', color="mediumpurple")
rects3 = ax.bar(x + width+0.2, interior, width, label='Interior', color="midnightblue")

for retangulo in rects1.patches: # for para cada retângulo
  # inserir texto na barra
  ax.text(retangulo.get_x() + retangulo.get_width() / 2, # posição x
          retangulo.get_height() + 400, # posição y
          '{:,}'.format(int(retangulo.get_height())).replace(',','.') + " Mil", ha = "center") # texto que queremos colocar

for retangulo in rects2.patches: # for para cada retângulo
  # inserir texto na barra
  ax.text(retangulo.get_x() + retangulo.get_width() / 2, # posição x
          retangulo.get_height() + 400, # posição y
          '{:,}'.format(int(retangulo.get_height())).replace(',','.') + " Mil", ha = "center") # texto que queremos colocar

for retangulo in rects3.patches: # for para cada retângulo
  # inserir texto na barra
  ax.text(retangulo.get_x() + retangulo.get_width() / 2, # posição x
          retangulo.get_height() + 400, # posição y
          '{:,}'.format(int(retangulo.get_height())).replace(',','.') + " Mil", ha = "center") # texto que queremos colocar


# Adicionando titulos e legendas
ax.set_ylabel('Quantidade de casos (em milhar)')
ax.set_title('Comparação de ocorrências registradas por região')
ax.set_xticks(x, labels)
ax.legend()

fig.tight_layout()

plt.show()