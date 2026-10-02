#Passo a passo 
#titulo - sistema de vendas
#seção - cadastrar vendas
    #campo data
    #campo vendedor - ana, bruno,carla
    #campo produto - notebook,celular, fone
    #campo quantidade
    #campo valor
    #botão cadastar venda

#seção - vendas cadastradas
    #tabela com as vendas cadastradas
#dashboard
    #card/métrica - faturamento total
    #gráfico de barra/coluna - venda por vendedor
    #gráfico de pizza - venda por produto

import streamlit as st
import pandas as pd
import plotly.express as px

#carregar tabela de vendas
tabela_vendas = pd.read_csv("vendas.csv")

st.write("# Sistema de Vendas")

#seção de cadastro de vendas
st.sidebar.write("## Cadastrar Vendas")

st.write("## Cadastrar Vendas")
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor")
botao_cadastrar = st.sidebar.button("Cadastrar Venda") 

#logica de cadastro
if botao_cadastrar:
    nova_venda = [str(data), vendedor, produto, quantidade, valor]
    ultima_linha = len(tabela_vendas)
    tabela_vendas.loc[ultima_linha] = nova_venda
    tabela_vendas.to_csv("vendas.csv", index=False)
    st.success("Venda cadastrada com sucesso!")

#seção de visualizar vendas
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)

#seção de dashboard
st.write("## Dashboard")
#Faturamento total
faturamento = tabela_vendas["valor"].sum()  

#gráfico de barra/coluna - venda por vendedor
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico1)

#graáfico de pizza - venda por produto
grafico2 = px.pie(tabela_vendas, names="produto", values="valor")
st.plotly_chart(grafico2)

