# data_ingestion/transform.py
from datetime import datetime
from models.bitcoin_model import BitcoinDados

def transformar_dados_bitcoin(dados_json):
    if dados_json and 'data' in dados_json and 'amount' in dados_json['data']:
        valor = float(dados_json['data']['amount'])
        criptomoeda = dados_json['data']['base']
        moeda = dados_json['data']['currency']

        dados_tratados = BitcoinDados(
            valor=valor,
            criptomoeda=criptomoeda,
            moeda=moeda,
            timestamp=datetime.now()
        )
        return dados_tratados
    else:
        print("Formato de dados JSON inválido para transformação.")
        return None