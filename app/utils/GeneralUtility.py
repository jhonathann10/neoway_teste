import re

class GeneralUtility:
    """
        Classe responsável por definir as funções para transformação de arquivos.
    """

    @staticmethod
    def validate_cpf(cpf) -> bool:
        """Validate CPF function.

            # Entradas Corretas:
             - '95524361503'
             - '955.243.615-03'
             - 955 243 615 03'

        Returns:
            bool: Retorna True quando CPF é válido senão retorna False.
        """
        cpf = ''.join(re.findall('\d', str(cpf)))
        tam_cpf = len(cpf)

        if (not cpf) or (tam_cpf < 11) or (tam_cpf > 11):
            return False

        if tam_cpf == 11:
            return True

    @staticmethod
    def validate_cnpj(cnpj) -> bool:
        """Validate CNPJ.

            # Entradas Corretas:
                - '11222333000181'
                - '11.222.333/0001-81'
                - '11 222 333 0001 81'
        """
        cnpj = ''.join(re.findall('\d', str(cnpj)))
        tam_cnpj = len(cnpj)

        if (not cnpj) or (tam_cnpj < 14) or (tam_cnpj> 14):
            return False

        if tam_cnpj == 14:
            return True
