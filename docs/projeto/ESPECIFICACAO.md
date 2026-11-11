# APIs HTTP e geração aleatória

**Documentação v1.0.0**, 11/11/2026 · código auditado `d6c9a4595a52b24d26db1c3d777467b41e8f13ae` · implementação observada estaticamente.

## Escopo real
Quatro scripts independentes de aprendizagem Python, organizados em pastas numeradas. O repositório não contém servidor único nem banco; cada exercício tem seu contrato de entrada/saída e suas dependências próprias. As funções nomeadas abaixo foram encontradas nos arquivos e permitem testes diretos quando isoladas dos blocos de interface.

| Script | Função principal | Implementação e limites |
|---|---|---|
| `1/gerador_senha.py` | `gerar_senha_aleatoria` | Usa random.choice e random.shuffle; 1 caractere de 4 grupos obrigatórios, comprimento mínimo 4 |
| `2/perfil_aleatorio.py` | `gerar_perfil_aleatorio` | GET https://randomuser.me/api/, lê results[0].name/email/location.country |
| `3/consulta_cep.py` | `consultar_cep` | Remove . e -; exige 8 dígitos e consulta ViaCEP /ws/{cep}/json/ |
| `4/cotacao_moeda.py` | `consultar_cotacao` | GET awesomeapi /json/last/{MOEDA}-BRL, campos bid/high/low/timestamp |

## Regras de engenharia
random.Random não é gerador criptograficamente seguro: senhas desse exercício não devem proteger contas reais; substituição futura exige secrets. Requisições externas não definem timeout explícito e dependem do formato de APIs de terceiros. Para testes, mockar requests.get; não fazer chamadas reais em CI.

## Execução
```bash
python 3/consulta_cep.py
python -m unittest discover -s tests -v
```

Não alegar que a suíte de documentação verifica as funções. Identificar as integrações reais e isolar dependências de `input()`, tempo ou HTTP para testes unitários reproduzíveis.
