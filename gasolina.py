# código de geração do gráfico

import seaborn as sns
import pandas as pd
import matplotlib.ticker as ticker  # formatação do gráfico

# Geração do dataframe
gasolina_df = pd.read_csv('gasolina.csv', sep=',')

# Utiliza grades no fundo do gráfico
with sns.axes_style('whitegrid'):

  # configuração dos eixos do gráfico
  grafico = sns.lineplot(data=gasolina_df, x="dia", y="venda")

  # formata o eixo Y para exibir vírgulas no lugar de pontos
  grafico.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x:,.2f}'.replace(",", "X").replace(".", ",").replace("X", ".")))

  grafico.set(title='Preço Médio da Gasolina - São Paulo (SP) - Julho de 2021', xlabel='DIA', ylabel='PREÇO (R$)');

# salvar o gráfico no arquivo gasolina.png
grafico.get_figure().savefig(f"gasolina.png") 
