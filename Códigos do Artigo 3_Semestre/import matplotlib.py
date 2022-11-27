# importing library
import pandas as pd
import matplotlib.pyplot as plt
import math

colore = {'mediumpurple', 'midnightblue'}

fig, ax = plt.subplots()
#importando a planilha
p = pd.read_excel("C:/Users/Guilherme/Downloads/Dados Formatados2_PI.xlsx")
    
    # creating data on which bar chart will be plot
D = p["Ocorrências registradas no Interior"]
E = p["Total das Ocorrências registradas no Interior"]
valoresIE = []

for val in E:
    valoresIE.append(str(val))

grafico2 = plt.bar(D, E, color='mediumpurple', width=0.50)    
for retangulo in grafico2.patches: # for para cada retângulo
  # vamos inserir um texto no Axes
  ax.text(retangulo.get_x() + retangulo.get_width() / 2, # posição x
          retangulo.get_height() + 400, # posição y
          '{:,}'.format(int(retangulo.get_height())).replace(',','.') + " Mil", ha = "center") # texto que queremos colocar

ax.set_frame_on(False)
plt.title("Ocorrências registradas no Interior")
      
# visualizing the plot
plt.show()