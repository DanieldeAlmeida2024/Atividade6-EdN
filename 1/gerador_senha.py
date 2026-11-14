import secrets
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

    if type(comprimento) is not int or not 4 <= comprimento <= 4096:
        raise ValueError("Informe um comprimento inteiro entre 4 e 4096 caracteres.")

    senha = [
        secrets.choice(letras_maiusculas),
        secrets.choice(letras_minusculas),
        secrets.choice(numeros),
        secrets.choice(caracteres_especiais)
    ]

    for _ in range(comprimento - 4):
        senha.append(secrets.choice(todos_caracteres))
    secrets.SystemRandom().shuffle(senha)

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