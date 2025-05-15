import requests
from tinydb import TinyDB
from sqlalchemy import create_engine, Column, String, Float, Integer, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
from dotenv import load_dotenv
import os
import pandas as pd
import psycopg2
import streamlit as st
import time

load_dotenv()

db_base = os.getenv("DATA_BASE_URL")

def ler_dados(): 
    try:
        conn = psycopg2.connect(db_base)
        query = "SELECT * FROM bitcoin_dados ORDER BY timestamp DESC"
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Erro ao conectar no PostegreSQL: {e}")
        return pd.DataFrame()
    
def main():
    st.set_page_config(page_title="Dashboard de cripto", layout="wide")
    st.title("Dashboard bitcoin")
    st.write("Esse dashboard exibe dados do bitcoin atualizados a cada 15 segundos")

    df = ler_dados()

    if not df.empty:
        st.subheader("Dados recentes")
        st.dataframe(df)

        df['timestamp'] = pd.to_datetime(df["timestamp"])
        df = df.sort_values(by='timestamp')

        st.subheader("Evolução do bitcoin")
        st.line_chart(data=df, x='timestamp', y='valor', use_container_width=True)

        st.subheader("Estatisticas Gerais")
        col1, col2, col3 = st.columns(3)
        col1.metric("preço atual", f"${df['valor'].iloc[-1]:,.2f}")
        col2.metric("preço máximo", f"${df['valor'].max():,.2f}")
        col3.metric("preço minimo", f"${df['valor'].min():,.2f}")

    else:
        st.warning("Nenhum dados encontrado")

if __name__ == "__main__":
    main()