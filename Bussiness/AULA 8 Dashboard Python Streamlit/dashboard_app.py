import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------
# FASE DE EXTRAÇÃO (E CORREÇÃO DE CODIFICAÇÃO)
# ----------------------------------------------

# Carrega os dados da pesquisa. CORREÇÃO: Usando 'latin-1' para resolver o UnicodeDecodeError.
df = pd.read_csv("consulta.csv" , encoding='latin-1', sep=';')
df.head()

# ----------------------------------------------
# FASE DE TRANSFORMAÇÃO (LIMPEZA E CÁLCULOS)
# ----------------------------------------------

# Troca todos '-' por '0'
df = df.replace('-', '0')
df.head(10)

# Converter colunas de ano para numérico, tratando a formatação brasileira (ponto como milhar, vírgula como decimal)
df.iloc[:, 1:] = df.iloc[:, 1:].apply(
    lambda col: pd.to_numeric(
        col.astype(str).str.replace('.', '', regex=False).str.replace(',', '.', regex=False),
        errors='coerce'
    )
)
df.head(10)

# Arredondar todas as colunas numéricas para 2 casas decimais
numeric_cols = df.select_dtypes(include=['float', 'int']).columns
df[numeric_cols] = df[numeric_cols].round(2)
                                    
                                    
# 1. Calcula a média dos investimentos por LINHA (Média por Localidade)
df["Md_Invest"] = df.iloc[:, 1:].mean(axis=1).round(2)


# ----------------------------------------------
# INSERÇÃO DA LINHA DE MÉDIA (OTIMIZAÇÃO LÓGICA)
# ----------------------------------------------

# 2. Calcula a média de CADA COLUNA (Média por Ano)
# Usamos .drop() para garantir que a coluna Md_Invest não seja usada no cálculo das médias anuais
valores_para_linha_media = df.iloc[:, 1:].drop(columns=['Md_Invest'], errors='ignore').mean().round(2)

# 3. Calcula a média da coluna Md_Invest (Média de todas as médias de localidade)
media_total_df = df['Md_Invest'].mean().round(2)

# 4. Cria a lista para a nova linha, incluindo a 'Média' como rótulo e o valor total na coluna Md_Invest
nova_linha = ["Média"] + valores_para_linha_media.tolist() + [media_total_df]

# 5. Converte a lista em um DataFrame com as mesmas colunas
linha_media = pd.DataFrame([nova_linha], columns=df.columns)

# 6. Concatena a nova linha ao DataFrame original (Fase de LOAD para o DataFrame)
df = pd.concat([df, linha_media], ignore_index=True)


# ----------------------------------------------
# FASE DE VISUALIZAÇÃO (DASHBOARD STREAMLIT)
# ----------------------------------------------

st.set_page_config(layout="wide")

st.title('Dashboard Financeiro - Pecuaria Goiais - 2014-2023')
st.write('Dashboard Financeiro - Tabela')

# Exibe o DataFrame já completo e formatado.
# (Não há mais o recalculo redundante da coluna Md_Invest aqui)
st.dataframe(df.style.format({'Md_Invest': '{:.2f}'}))
st.dataframe(df.head())