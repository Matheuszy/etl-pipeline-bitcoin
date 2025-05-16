from agno.agent import Agent
from agno.tools.base import Tool
from dotenv import load_dotenv
import os
from agno.models.groq import Groq
from agent.agent_logic import obter_tabelas, executar_query, obter_cotacoes_bitcoin, analisar_dados

load_dotenv()

class DatabaseQueryTool(Tool):
    name = "database_query"
    description = "Useful for executing SQL queries and fetching data from the database."

    def _run(self, query: str) -> str:
        results, keys = executar_query(query)
        if results:
            return "Resultados: " + str([dict(zip(keys, row)) for row in results])
        else:
            return "Nenhum resultado encontrado."

class ListTablesTool(Tool):
    name = "list_database_tables"
    description = "Useful for listing all tables available in the database."

    def _run(self) -> str:
        tables, _ = obter_tabelas()
        return "Tabelas no banco de dados: " + ", ".join([t[0] for t in tables])

class FetchBitcoinDataTool(Tool):
    name = "fetch_bitcoin_data"
    description = "Useful for fetching the latest bitcoin quotes."

    def _run(self) -> str:
        cotacoes, colunas = obter_cotacoes_bitcoin()
        if cotacoes:
            return "Últimas cotações de Bitcoin: " + str([dict(zip(colunas, row)) for row in cotacoes[:5]])
        else:
            return "Nenhuma cotação de Bitcoin encontrada."

class AnalyzeBitcoinDataTool(Tool):
    name = "analyze_bitcoin_data"
    description = "Useful for performing complex analysis on the fetched bitcoin data."

    def _run(self) -> str:
        cotacoes, _ = obter_cotacoes_bitcoin()
        return analisar_dados(cotacoes)

# Initialize tools
database_tool = DatabaseQueryTool()
list_tables_tool = ListTablesTool()
fetch_bitcoin_tool = FetchBitcoinDataTool()
analyze_bitcoin_tool = AnalyzeBitcoinDataTool()

# Create an agent with the tools
agent = Agent(model=Groq(id="llama-3.3-70b-versatile"),
              tools=[database_tool, list_tables_tool, fetch_bitcoin_tool, analyze_bitcoin_tool])

agent.print_response("Fale todas as tabelas do banco de dados", markdown=True)

agent.print_response("""
Faça uma query para pegar todas as cotações de bitcoin
""", markdown=True)

agent.print_response("""
Faça uma analise complexa dos dados que forem obtidos
""", markdown=True)