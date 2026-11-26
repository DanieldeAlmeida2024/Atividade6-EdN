> **Referência histórica de 11/11/2026.** Consulte README, `docs/PLANO_TESTES.md` e CI vigentes. Os cenários planejados na origem não são prova de homologação funcional.

# Versionamento — Atividade6-EdN

**1.0.0**, 11/11/2026, base `d6c9a4595a52b24d26db1c3d777467b41e8f13ae`. Referências: [projeto](../projeto/ESPECIFICACAO.md), [UML](../uml/README.md), [testes](../testes/PLANO_DE_TESTES.md).

| Versão | Data | Alteração |
|---|---|---|
| 1.0.0 | 11/11/2026 | Inventário dos quatro exercícios, fluxos por fonte e critérios de teste separados |
| 1.0.1 | 26/11/2026 | README e plano de testes registram a validação de respostas do ViaCEP |

MAJOR para mudança incompatível das assinaturas/saídas; MINOR para novos exercícios; PATCH para ajustes editoriais. Evidências de testes vinculadas ao SHA.

## Revisão de reconciliação — 14/11/2026

Arquivos específicos da antiga modelagem de 11/11 preservados com identificação histórica, sem reverter testes ou código funcional da main. A evidência dos testes aprovados é obtida nas execuções atuais do CI.

## Evidência de 26/11/2026

Os testes reproduziram sucesso indevido para respostas incompletas ou divergentes antes da correção. No SHA `ce6cdc53347bb448b7220bcc3c3fd0125d7af629`, Python 3.11.9 executou `python -m unittest discover -s tests -p 'test_*.py' -v` com 16 testes aprovados e `python -m compileall -q 1 2 3 4 tests` sem erros. As respostas do provedor foram simuladas.
