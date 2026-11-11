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

A suíte acrescentada verifica documentação e sintaxe dos scripts; **não** comprova respostas corretas nem disponibilidade das APIs externas.

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
