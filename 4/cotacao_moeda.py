import requests
import datetime

def consultar_cotacao(codigo_moeda: str):
    codigo_moeda = codigo_moeda.upper().strip()
    API_URL = f"https://economia.awesomeapi.com.br/json/last/{codigo_moeda}-BRL"
    
    print(f"\n--- 🔎 Consultando Cotação: {codigo_moeda}/BRL ---")
    
    try:
        response = requests.get(API_URL)
        response.raise_for_status() 
        dados = response.json()
        
        chave_cotacao = f"{codigo_moeda}BRL"
        
        if chave_cotacao not in dados:
            print(f"Erro: Não foi possível encontrar a cotação para {codigo_moeda}. Verifique o código da moeda.")
            return
            
        cotacao = dados[chave_cotacao]
        
        timestamp = int(cotacao.get('timestamp'))
        data_hora = datetime.datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S')
        
        print("\n--- Resultados da Cotação ---")
        print(f"**Moeda Consultada:** {cotacao.get('name')}")
        print(f"**Valor Atual (Compra):** R$ {float(cotacao.get('bid')):.4f}")
        print(f"**Máximo (Alta):** R$ {float(cotacao.get('high')):.4f}")
        print(f"**Mínimo (Baixa):** R$ {float(cotacao.get('low')):.4f}")
        print(f"**Data e Hora da Última Atualização:** {data_hora}")
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar à API: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

def aplicacao_cotacao():
    print("--- 💸 Consulta de Cotação em Tempo Real ---")
    moeda_usuario = input("Digite o código da moeda estrangeira (ex: USD, EUR, JPY): ")
    
    consultar_cotacao(moeda_usuario)

if __name__ == "__main__":
    aplicacao_cotacao()