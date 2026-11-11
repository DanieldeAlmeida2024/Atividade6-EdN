import ast
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class TesteDocumentos(unittest.TestCase):
    def test_documentos(self):
        for nome in ('README.md','AGENTS.md','docs/REQUISITOS.md','docs/ARQUITETURA.md','docs/UML.puml','docs/PLANO_TESTES.md'):
            with self.subTest(nome=nome):self.assertTrue((ROOT/nome).is_file())
    def test_sintaxe(self):
        scripts=[p for p in ROOT.rglob('*.py') if 'tests' not in p.parts]
        self.assertTrue(scripts)
        for p in scripts:
            with self.subTest(p=p):ast.parse(p.read_text(encoding='utf-8-sig'))
