import streamlit as st
import pandas as pd

def hora_em_minutos(hora):
    h, m = map(int, hora.split(":"))
    return h * 60 + m

def esta_disponivel(intervalos, hora_minutos):
    for intervalo in str(intervalos).split(","):
        try:
            inicio, fim = intervalo.strip().split("-")
            if hora_em_minutos(inicio) <= hora_minutos <= hora_em_minutos(fim):
                return True
        except:
            continue
    return False

def verificar_disponibilidade(df, dia, hora):
    hora_min = hora_em_minutos(hora)
    disponiveis = []
    ocupados = []
    for _, row in df.iterrows():
        horarios_dia = str(row[dia]).strip()
        if horarios_dia and esta_disponivel(horarios_dia, hora_min):
            disponiveis.append(f"{row['Nome']} ({row['Setor']})")
        else:
            ocupados.append(f"{row['Nome']} ({row['Setor']})")
    return disponiveis, ocupados

st.title("Verificador de Disponibilidade de Horários")
df = pd.read_csv("horarios.csv")
dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
dia = st.selectbox("Dia da semana:", dias)
hora = st.time_input("Horário desejado:")
if st.button("Verificar"):
    hora_formatada = hora.strftime("%H:%M")
    disponiveis, ocupados = verificar_disponibilidade(df, dia, hora_formatada)
    st.subheader(f"Disponibilidade para {dia} às {hora_formatada}:")
    if disponiveis:
        st.success("Disponíveis:")
        for pessoa in disponiveis:
            st.markdown(f"- {pessoa}")
    else:
        st.warning("Ninguém disponível")
    if ocupados:
        st.error("Ocupados:")
        for pessoa in ocupados:
            st.markdown(f"- {pessoa}")
    else:
        st.info("Ninguém ocupado")