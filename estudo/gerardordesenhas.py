import string
import random

def gerar_senha(tamanho):
    if tamanho < 4:
        raise ValueError("O tamanho mínimo da senha deve ser 4 para incluir todos os tipos de caracteres.")

    # Conjuntos de caracteres
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    caracteres_especiais = string.punctuation

    # Garantir pelo menos um de cada tipo de caractere
    senha = [
        random.choice(letras_maiusculas),
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(caracteres_especiais),
    ]

    # Preencher o restante da senha com caracteres aleatórios
    todos_caracteres = letras_maiusculas + letras_minusculas + numeros + caracteres_especiais
    senha += random.choices(todos_caracteres, k=tamanho - 4)

    # Embaralhar a senha para não ficar previsível
    random.shuffle(senha)

    # Retornar a senha como uma string
    return ''.join(senha)

# Testando o gerador de senhas
print(gerar_senha(12))  # Saída: Uma senha aleatória, como "A1#b2C3$dE4!"
