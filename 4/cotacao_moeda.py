import requests
import datetime
import re
import math

def consultar_cotacao(codigo_moeda: str):
    codigo_moeda = codigo_moeda.upper().strip()
    if not re.fullmatch(r'[A-Z]{3}', codigo_moeda):
        print('Erro: Informe um código ISO de moeda com três letras (ex: USD).')
        return
    API_URL = f"https://economia.awesomeapi.com.br/json/last/{codigo_moeda}-BRL"
    
    print(f"\n--- 🔎 Consultando Cotação: {codigo_moeda}/BRL ---")
    
    try:
        response = requests.get(API_URL, timeout=(3, 8))
        response.raise_for_status() 
        dados = response.json()
        
        chave_cotacao = f"{codigo_moeda}BRL"
        
        if chave_cotacao not in dados:
            print(f"Erro: Não foi possível encontrar a cotação para {codigo_moeda}. Verifique o código da moeda.")
            return
            
        cotacao = dados[chave_cotacao]
        
        if not isinstance(cotacao, dict):
            raise ValueError("Cotação não é um objeto")
        timestamp = int(cotacao.get('timestamp'))
        # UTC evita diferença de relógio local nos testes e em diferentes máquinas.
        data_hora = datetime.datetime.fromtimestamp(
            timestamp, tz=datetime.timezone.utc
        ).strftime('%d/%m/%Y %H:%M:%S UTC')
        bid, alta, baixa = (float(cotacao.get(k)) for k in ('bid', 'high', 'low'))
        if not all(math.isfinite(valor) and valor > 0 for valor in (bid, alta, baixa)):
            raise ValueError("Cotação deve ser positiva e finita")

        print("\n--- Resultados da Cotação ---")
        print(f"**Moeda Consultada:** {cotacao.get('name')}")
        print(f"**Valor Atual (Compra):** R$ {bid:.4f}")
        print(f"**Máximo (Alta):** R$ {alta:.4f}")
        print(f"**Mínimo (Baixa):** R$ {baixa:.4f}")
        print(f"**Data e Hora da Última Atualização:** {data_hora}")
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar à API: {e}")
    except (ValueError, TypeError, KeyError, AttributeError, OverflowError, OSError) as e:
        print(f"Erro: A API retornou cotação incompleta ou inválida: {e}")

def aplicacao_cotacao():
    print("--- 💸 Consulta de Cotação em Tempo Real ---")
    moeda_usuario = input("Digite o código da moeda estrangeira (ex: USD, EUR, JPY): ")
    
    consultar_cotacao(moeda_usuario)

if __name__ == "__main__":
    aplicacao_cotacao()