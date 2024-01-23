import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sb

df=pd.read_csv(r"C:\Users\Admin\Desktop\etc\faculdade-cruzeiro-do-sul\visualizacao-da-informacao\export.csv")
df.head()

plt.rcParams.update({
    "figure.facecolor":  (0.1, 0.1, 0.1, 0.05),
})
cm = sb.color_palette("plasma", 100) 
cm2 = sb.color_palette("flare", 100)

tier=df['TIER'].value_counts()

def fmt(x):
    return '{:.1f}%\n{:.0f}'.format(x, int(tier.values.sum())*x/100)
plt.figure("Gráfico 01 - Proporção dos jogadores entre os maiores elos")
plt.pie(x=tier, 
        labels=tier.index, 
        autopct=fmt, 
        colors=['#66b3ff','#ff9999','#99ff99','#ffcc99'])
plt.show()

regions=df['REQUEST_REGION'].value_counts()
regions_filtered = {"NOME": ["Europa Oriental", "Brasil", "República da Coreia", "Estados Unidos", "Europa Ocidental", "América Latina Norte", "América Latina Sul", "Turquia", "Oceânia", "Rússia", "Japão"], 
                    "LOCALIZACAO": ["GER","BRA", "KOR", "USA", "NLD", "MEX", "CHL", "TUR", "AUS", "RUS", "JPN"], 
                    "VALUES": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
for i,z in enumerate(regions):
    regions_filtered["VALUES"][i] += z

dframe = pd.DataFrame(regions_filtered)

fig = px.scatter_geo(dframe, locations="LOCALIZACAO", size="VALUES", color="NOME", hover_name="NOME", size_max=55)
fig.update_layout(title_text = 'Gráfico 02 - Quantia total de jogadores por servidor (região)')
fig.show()

plt.figure("Gráfico 04 - Total de vitórias entre os jogadores")
plot = sb.histplot(df['WINS'])
plt.ylabel('Número de Jogadores')
plt.xlabel('Quantidade de Vitórias')

for bin_,i in zip(plot.patches,cm):
    bin_.set_facecolor(i)
plt.xlim(0, 1000)
plt.show()

plt.figure("Gráfico 05 - Total de derrotas entre os jogadores")
plot = sb.histplot(df['LOSSES'])
plt.ylabel('Número de Jogadores')
plt.xlabel('Quantidade de Derrotas')

for bin_,i in zip(plot.patches,cm2):
    bin_.set_facecolor(i)
plt.xlim(0, 1000)
plt.show()