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

engine = create_engine(db_base)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class BitcoinDados(Base):
    __tablename__ = "bitcoin_dados"  # Correção aqui: dois underscores

    id = Column(Integer, primary_key=True)
    valor = Column(Float)
    criptomoeda = Column(String(10))
    moeda = Column(String(10))
    timestamp = Column(DateTime)

Base.metadata.create_all(engine)


def extrair():
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)
    return response.json()
 
def transformar(dados_json):
    valor = (dados_json['data']['amount'])
    criptomoeda = dados_json['data']['base']
    moeda = dados_json['data']['currency']

    dados_tratados = BitcoinDados(
        valor=valor,
        criptomoeda=criptomoeda,
        moeda=moeda,
        timestamp=datetime.now().isoformat()
    )
    return dados_tratados

def load(dados):
    with Session() as session:
        session.add(dados)
        session.commit()
        print("dados salvos com sucesso")

if __name__ == "__main__":
    while True:
        dados_json = extrair()
        dados_tratados = transformar(dados_json)

        print("Dados Tratados:")
       

        load(dados_tratados)
        print("aguardando 15 segundos...")
        time.sleep(15)
    