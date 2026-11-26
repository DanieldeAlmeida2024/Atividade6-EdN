# Plano de testes

CT-01 Verificar arquivos e documentação.
CT-02 Analisar sintaxe Python sem executar os scripts.
CT-03 Exercitar casos normais, extremos e inválidos por atividade.
CT-04 Nas atividades externas, simular falha de conexão e resposta inválida.

A suíte `python -m unittest discover -s tests -v` executa testes estruturais, comportamentais e de respostas HTTP simuladas. Comportamento contra provedores reais depende de validação separada.

### CT-04 — respostas do ViaCEP

- Respostas sem objeto de endereço, sem cidade ou UF válidas ou com CEP divergente exibem erro de dados e não anunciam sucesso.
- CEP com cidade e UF válidas ainda exibe o endereço quando bairro e logradouro estão vazios.
- A resposta com `erro: true` informa que o CEP não foi encontrado.

Os casos executam `consultar_cep` em `tests/test_comportamento.py` com respostas simuladas.
