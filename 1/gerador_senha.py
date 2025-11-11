import random
import string

def gerar_senha_aleatoria(comprimento: int) -> str:
    """
    Gera uma senha aleatória de um dado comprimento.

    Args:
        comprimento (int): O número de caracteres que a senha deve ter.

    Returns:
        str: A senha aleatória gerada.
    """
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    caracteres_especiais = '!@#$%^&*()_+-=[]{}|;:,.<>?'

    todos_caracteres = letras_maiusculas + letras_minusculas + numeros + caracteres_especiais

    if comprimento < 4:
        raise ValueError("O comprimento da senha deve ser de pelo menos 4 para garantir a diversidade de caracteres.")

    senha = [
        random.choice(letras_maiusculas),
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(caracteres_especiais)
    ]

    for _ in range(comprimento - 4):
        senha.append(random.choice(todos_caracteres))
    random.shuffle(senha)

    return "".join(senha)

def aplicacao_gerador_senha():
    """Ponto de entrada da aplicação."""
    print("--- 🔑 Gerador de Senhas Aleatórias ---")
    
    try:
        comprimento = int(input("Digite o comprimento desejado para a senha (ex: 12): "))
        
        if comprimento <= 0:
            print("Erro: O comprimento da senha deve ser um número positivo.")
            return

        senha_gerada = gerar_senha_aleatoria(comprimento)
        
        print("\n--- Resultado ---")
        print(f"Comprimento da Senha: {comprimento}")
        print(f"**Senha Gerada:** {senha_gerada}")
        
    except ValueError as e:
        print(f"Erro: {e}. Certifique-se de digitar um número inteiro válido e que seja >= 4.")

if __name__ == "__main__":
    aplicacao_gerador_senha()