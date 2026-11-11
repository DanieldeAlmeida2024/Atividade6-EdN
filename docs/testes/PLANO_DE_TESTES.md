# Matriz de testes — Atividade6-EdN

**Documentação v1.0.0**, 11/11/2026 · código auditado `d6c9a4595a52b24d26db1c3d777467b41e8f13ae` · implementação observada estaticamente.

| ID | Programa/função | Cenário verificável | Estado |
|---|---|---|---|
| N-T1 | `1/gerador_senha.py` / `gerar_senha_aleatoria` | Comprimento 3 recusa; comprimento 12 contém as 4 classes | Planejado; falta execução |
| N-T2 | `2/perfil_aleatorio.py` / `gerar_perfil_aleatorio` | Simular HTTP 200 e falha/JSON incompleto | Planejado; falta execução |
| N-T3 | `3/consulta_cep.py` / `consultar_cep` | CEP 123 inválido não acessa rede; API com erro true mostra não encontrado | Planejado; falta execução |
| N-T4 | `4/cotacao_moeda.py` / `consultar_cotacao` | Resposta sem moeda informa erro; timestamp e valores formatados | Planejado; falta execução |

## Testes de falha
- N01: ausência de entrada, valores vazios ou tipo incompatível.
- N02: limites inferiores/superiores e valores negativos nas funções matemáticas.
- N03: repetir a operação e verificar que não há estado compartilhado inesperado.
- N04: se houver I/O, mockar `requests`, tempo ou aleatoriedade; evitar rede real em CI.

## Evidências
Criar funções de teste `test_*.py` específicas de cada arquivo, usando `unittest.mock` quando pertinente. Registrar Python version, SHA, fixtures, resultado e exceção observada. A suíte existente `tests/test_documentacao.py` não é prova dos cenários de comportamento.
