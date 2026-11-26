import re

import requests

def consultar_cep(cep: str):
    if not isinstance(cep, str):
        print("Erro: O CEP deve ser texto com exatamente 8 dígitos ASCII.")
        return
    cep_limpo = cep.replace('-', '').replace('.', '').strip()
    
    if len(cep_limpo) != 8 or not (cep_limpo.isascii() and cep_limpo.isdigit()):
        print("Erro: O CEP deve conter exatamente 8 dígitos numéricos.")
        return

    API_URL = f"https://viacep.com.br/ws/{cep_limpo}/json/"
    
    print(f"\n--- 🔎 Consultando CEP: {cep_limpo} ---")
    
    try:
        response = requests.get(API_URL, timeout=(3, 8))
        response.raise_for_status() 
        dados = response.json()

        if not isinstance(dados, dict):
            raise ValueError("O endereço retornado deve ser um objeto JSON.")
        if dados.get('erro'):
            print("Resultado: CEP não encontrado ou inválido.")
            return

        cep_recebido = dados.get('cep')
        cidade = dados.get('localidade')
        uf = dados.get('uf')
        logradouro = dados.get('logradouro', '')
        bairro = dados.get('bairro', '')
        if (
            not isinstance(cep_recebido, str)
            or cep_recebido.replace('-', '') != cep_limpo
            or not isinstance(cidade, str) or not cidade.strip()
            or not isinstance(uf, str) or not re.fullmatch(r'[A-Z]{2}', uf)
            or not isinstance(logradouro, str) or not isinstance(bairro, str)
        ):
            raise ValueError("O endereço deve conter CEP correspondente, cidade e UF válidas.")

        print("\n--- Endereço Encontrado ---")
        print(f"**CEP:** {cep_recebido}")
        print(f"**Logradouro:** {logradouro}")
        print(f"**Bairro:** {bairro}")
        print(f"**Cidade:** {cidade}")
        print(f"**Estado (UF):** {uf}")
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar à API ViaCEP: {e}")
    except (ValueError, TypeError, AttributeError) as e:
        print(f"Erro: A API retornou dados inválidos: {e}")

def aplicacao_consulta_cep():
    print("--- 🏠 Programa de Consulta de Endereço por CEP ---")
    cep_usuario = input("Digite o CEP para consulta (somente números ou com hífen): ")
    
    consultar_cep(cep_usuario)

if __name__ == "__main__":
    aplicacao_consulta_cep()
