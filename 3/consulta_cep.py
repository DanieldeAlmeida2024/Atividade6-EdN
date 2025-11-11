import requests

def consultar_cep(cep: str):
    cep_limpo = cep.replace('-', '').replace('.', '').strip()
    
    if len(cep_limpo) != 8 or not cep_limpo.isdigit():
        print("Erro: O CEP deve conter exatamente 8 dígitos numéricos.")
        return

    API_URL = f"https://viacep.com.br/ws/{cep_limpo}/json/"
    
    print(f"\n--- 🔎 Consultando CEP: {cep_limpo} ---")
    
    try:
        response = requests.get(API_URL)
        response.raise_for_status() 
        dados = response.json()
        
        if dados.get('erro'):
            print("Resultado: CEP não encontrado ou inválido.")
            return
            
        print("\n--- Endereço Encontrado ---")
        print(f"**CEP:** {dados.get('cep')}")
        print(f"**Logradouro:** {dados.get('logradouro')}")
        print(f"**Bairro:** {dados.get('bairro')}")
        print(f"**Cidade:** {dados.get('localidade')}")
        print(f"**Estado (UF):** {dados.get('uf')}")
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar à API ViaCEP: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

def aplicacao_consulta_cep():
    print("--- 🏠 Programa de Consulta de Endereço por CEP ---")
    cep_usuario = input("Digite o CEP para consulta (somente números ou com hífen): ")
    
    consultar_cep(cep_usuario)

if __name__ == "__main__":
    aplicacao_consulta_cep()