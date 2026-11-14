# Atividade6-EdN — atividades Python

Exercícios de senha aleatória e consumo de APIs públicas (perfil, CEP e câmbio).

## Execução
Requer Python 3.10+:

```bash
python 1/gerador_senha.py
```

**Scripts:** 1/gerador_senha.py, 2/perfil_aleatorio.py, 3/consulta_cep.py, 4/cotacao_moeda.py. As atividades são independentes.

## Testes
```bash
python -m unittest discover -s tests -v
```

A suíte inclui testes com mocks para os serviços externos e validações dos scripts, sem depender da disponibilidade real dos provedores.


## Validações e segurança

- **Senhas:** a geração usa `secrets` (fonte criptograficamente apropriada), com embaralhamento seguro, garantia de letras maiúsculas/minúsculas, números e símbolo. Os tamanhos válidos são de 4 a 4096 caracteres; para contas reais, prefira 12 ou mais. O módulo `secrets` fornece a fonte de aleatoriedade apropriada ao exercício de geração de senhas.
- **APIs externas:** Random User, ViaCEP e AwesomeAPI têm limites de conexão/leitura de 3/8 segundos, em vez de bloquear indefinidamente. Códigos de moeda só aceitam três letras. Estruturas inválidas são tratadas sem encerrar o processo por exceções não tratadas.
- **Testes reais:** `python -m pip install -r requirements.txt && python -m unittest discover -s tests -p 'test_*.py' -v`; os testes usam mocks e **não dependem de servidores externos nem atestam disponibilidade dessas APIs**.

## Atenção
As atividades dependentes de APIs exigem conexão e disponibilidade externa; evitar salvar dados pessoais reais. Para senhas reais, revisar uso de geração criptográfica.

Documentos complementares: [requisitos](docs/REQUISITOS.md), [estrutura](docs/ARQUITETURA.md), [UML](docs/UML.puml), [plano de testes](docs/PLANO_TESTES.md), [guia IA](AGENTS.md).

---

## Enunciados originais

## Atividade Prática 06
O enunciado das atividades estão nos slides da Aula 10.


1. Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória.

2. Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'. O programa deve exibir o nome, email e país do usuário gerado.

3. Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.

4. Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da AwesomeAPI para obter os dados de cotação.

## Documentação específica da atividade

[Especificação dos scripts](docs/projeto/ESPECIFICACAO.md) · [Matriz histórica de testes](docs/testes/PLANO_DE_TESTES.md) · [UML](docs/uml/README.md) · [Versionamento](docs/controle/VERSIONAMENTO.md).

A documentação original é preservada como referência de estudo. Os critérios vigentes e os resultados de CI atualizados estão no plano de testes principal e no GitHub Actions.
