import re



def validate(cpf) -> bool:
    cpf = ''.join(re.findall('\d', str(cpf)))
    tam_cpf = len(cpf)

    if (not cpf) or (tam_cpf < 11) or (tam_cpf > 11):
        return False

    if (len(cpf) == 11):
        return True

print(validate('102.432 13: 13'))