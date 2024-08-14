import requests
import streamlit as st
#para rodar o projeto >> streamlit run app.py

def buscador_letra(banda, musica):
    url = f"https://api.lyrics.ovh/v1/{banda}/{musica}"
    response = requests.get(url)
    letra = response.json()['lyrics'] if response.status_code == 200 else ""
    return letra



col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTh4wJTz2Nogvl5aJZm20mrnsHDD_-HC3NFeA&s")
    st.title("Letras de Músicas")
    banda = st.text_input("Digite o nome da banda: ", key='banda')
    musica = st.text_input("Qual música você quer? ", key='musica')
    pesquisar = st.button('>> PESQUISAR <<')

    if pesquisar:
        letra = buscador_letra(banda, musica)
        if letra:
            st.success("Encontramos a letra da sua música")
            st.text(letra)
        else:
            st.error("Infelizmente não encontramos essa música")
