import time
from data_ingestion.extract import extrair_dados_bitcoin
from data_ingestion.transform import transformar_dados_bitcoin
from data_ingestion.load import carregar_dados_bitcoin

if __name__ == "__main__":
    while True:
        print("Iniciando ciclo de coleta de dados...")
        dados_json = extrair_dados_bitcoin()
        if dados_json:
            dados_tratados = transformar_dados_bitcoin(dados_json)
            if dados_tratados:
                carregar_dados_bitcoin(dados_tratados)
        print("Aguardando 15 segundos para a próxima coleta...")
        time.sleep(15)