import csv
import pandas as pd

class Leitura:

    @staticmethod
    def read_file(path: str, file_name: str, method: str = None, extension: str = 'txt', delimiter: str = ',',
                  header: bool = None, header_names: list = None) -> pd.DataFrame:
        """
            Função para ler o arquivo e criar um pandas DataFrame.
        """

        file_path = f"{path}/{file_name}.{extension}"
        pdf = pd.read_csv(file_path, sep=delimiter, delimiter=delimiter, header=0, skiprows=1,
                          names=header_names)
        return pdf