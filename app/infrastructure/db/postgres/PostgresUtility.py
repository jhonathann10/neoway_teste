import os
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

class PostgresUtility():
    """
        Classe resposável pela conexão e interface com a base de dados postgres.
    """
    def __init__(self):
        self.connection_string = f"postgresql+psycopg2://{os.environ.get('POSTGRES_URL')}"

    def get_pg_connection(self, retry: bool = True):
        """
            Função para criar conexão com o postgres
            retry: Tenta mais uma vez
        """
        try:
            conexao_url = create_engine(self.connection_string, pool_recycle=3600)
            print(f"Conectou em {self.connection_string}.")
            return conexao_url.connect()
        except Exception as err:
            if retry:
                print(f"Não conseguiu conectar com o postgres: {err}.")
                self.get_pg_connection(retry=False)
            raise err

    def escrever_df_postgres(self, df: pd.DataFrame, table_name: str) -> bool:
        """
            Escrever DataFrame Pandas para o banco de dados.
            df: O DataFrame que será escrito no banco.
            table_name: Nome da tabela a ser escrita no banco

            Return: Retorna True quando for sucesso ou lança um erro quando não funciona.
        """

        conn = self.get_pg_connection()

        try:
            print(f"Escrevendo {table_name} no banco de dados.")
            df.to_sql(table_name, conn, if_exists='fail')
            return True
        except Exception as err:
            print(f"Não conseguiu inserir na base de dados: {err}.")
        finally:
            conn.close()
