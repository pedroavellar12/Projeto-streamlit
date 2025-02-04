import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(
    page_title="Cadastro de Clientes",
    page_icon="📙"
)

def gravar_dados(nome, dt_nasc, tipo):
    if nome and dt_nasc <= date.today():
        with open("Clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{nome}, {dt_nasc}, {tipo}\n")
        st.session_state["Sucesso!"] = True
    else:
        st.session_state["Sucesso!"] = False
    
    

st.title("Cadastro de Clientes")
st.divider()

nome = st.text_input("Nome do Cliente",
                     key="nome_cliente")
dt_nasc = st.date_input("Data Nascimento:",
                        format="DD/MM/YYYY")
tipo = st.selectbox("Tipo de Cliente",
                    ["Pessoa Física", "Pessoa Jurídica"])

btn_cadastrar = st.button("Cadastrar", 
                           on_click=gravar_dados,
                           args=[nome, dt_nasc, tipo])

if btn_cadastrar:
    if st.session_state["Sucesso!"]:
        st.success("Cliente cadastrado com sucesso!",
                   icon="✅")
    else:
        st.error("Houve algum problema no cadastro!",
                 icon="❌")
        



