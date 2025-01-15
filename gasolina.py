# código de geração do gráfico

import seaborn as sns
import pandas as pd

# Geração do dataframe
gasolina_df = pd.read_csv('gasolina.csv', sep=',')

# Utiliza grades no fundo do gráfico
with sns.axes_style('whitegrid'):

# configuração dos dados no gráfico
  grafico = sns.lineplot(data=gasolina_df, x="dia", y="venda")
  grafico.set(title='Preço médio da gasolina - Julho de 2021', xlabel='DIA', ylabel='PREÇO');

# salvar o gráfico no arquivo gasolina.png
grafico.get_figure().savefig(f"gasolina.png")
