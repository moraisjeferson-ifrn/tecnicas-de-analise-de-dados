import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pygwalker as pyw

st.title("Tarefa Online 5")

url = "https://raw.githubusercontent.com/tmedeirosb/tsi-ad-2025/refs/heads/main/dados/dados_workflow_ivan.csv"
df = pd.read_csv(url)

# filtro lateral
selected_sigla = st.sidebar.selectbox(
    "Selecione a Sigla do Campus:",
    df['sigla'].unique()
)

# filtrar dados
filtered_sigla_df = df[df['sigla'] == selected_sigla]

# tabela
st.write(f"Dados filtrados para a sigla: {selected_sigla}")
st.dataframe(filtered_sigla_df[["sigla","LnguaPortuguesaeLiteraturaI90H","MatemticaI120H"]])

# gráfico
st.subheader("Gráfico de Histograma")
fig, ax = plt.subplots()
sns.histplot(filtered_sigla_df['MatemticaI120H'], kde=True, ax=ax)
st.pyplot(fig)

st.write(f"Dataset bruto:")
st.write(df)

# dashboard interativo
st.subheader("Exploração interativa dos dados")
pyw.walk(df, env='Streamlit')