import requests

def gerar_perfil_aleatorio():
    API_URL = "https://randomuser.me/api/"
    
    print("--- 🌍 Gerador de Perfil de Usuário Aleatório ---")
    
    try:
        response = requests.get(API_URL, timeout=(3, 8))
        response.raise_for_status() 
        dados = response.json()
        
        usuario = dados['results'][0]
        
        nome_titulo = usuario['name']['title']
        nome_primeiro = usuario['name']['first']
        nome_ultimo = usuario['name']['last']
        
        email = usuario['email']
        pais = usuario['location']['country']
        
        print("\n--- Perfil Gerado ---")
        print(f"**Nome Completo:** {nome_titulo}. {nome_primeiro} {nome_ultimo}")
        print(f"**E-mail:** {email}")
        print(f"**País:** {pais}")
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar à API: {e}")
    except (KeyError, IndexError, TypeError, ValueError):
        print("Erro: A estrutura de dados da API foi alterada ou o retorno está incompleto.")

if __name__ == "__main__":
    gerar_perfil_aleatorio()