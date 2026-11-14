"""Testes comportamentais com HTTP simulado, sem acesso a APIs externas."""
import contextlib
import importlib.util
import io
import pathlib
import re
import unittest
from unittest.mock import Mock, patch

ROOT = pathlib.Path(__file__).resolve().parents[1]

def carregar(nome, caminho):
    spec = importlib.util.spec_from_file_location(nome, ROOT / caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo

senha = carregar("gerador_senha", "1/gerador_senha.py")
perfil = carregar("perfil_aleatorio", "2/perfil_aleatorio.py")
cep = carregar("consulta_cep", "3/consulta_cep.py")
cotacao = carregar("cotacao_moeda", "4/cotacao_moeda.py")


class SenhasTestes(unittest.TestCase):
    def test_tem_todas_as_quatro_classes_e_tamanho_correto(self):
        for tamanho in (4, 12, 36, 64):
            with self.subTest(tamanho=tamanho):
                resultado = senha.gerar_senha_aleatoria(tamanho)
                self.assertEqual(tamanho, len(resultado))
                self.assertRegex(resultado, r"[A-Z]")
                self.assertRegex(resultado, r"[a-z]")
                self.assertRegex(resultado, r"[0-9]")
                self.assertRegex(resultado, r"[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]")

    def test_tamanhos_invalidos_e_booleanos_rejeitados(self):
        for tamanho in (True, False, 3, 0, -1, 4097, "12", 5.5):
            with self.subTest(tamanho=tamanho):
                with self.assertRaises(ValueError):
                    senha.gerar_senha_aleatoria(tamanho)

    def test_nao_usa_gerador_aleatorio_nao_criptografico(self):
        self.assertIsNotNone(senha.secrets)
        self.assertEqual("secrets", senha.secrets.__name__)


class ApiTestes(unittest.TestCase):
    def test_perfil_usa_timeout_e_exibe_dados(self):
        resposta = Mock()
        resposta.json.return_value = {
            "results": [{"name": {"title": "Sr", "first": "Carlos", "last": "Lima"},
                         "email": "exemplo@example.com", "location": {"country": "Brazil"}}]
        }
        with patch.object(perfil.requests, "get", return_value=resposta) as get, io.StringIO() as buffer, contextlib.redirect_stdout(buffer):
            perfil.gerar_perfil_aleatorio()
            saida = buffer.getvalue()
        get.assert_called_once_with("https://randomuser.me/api/", timeout=(3, 8))
        self.assertIn("Carlos Lima", saida)

    def test_perfil_sem_results_nao_crasha(self):
        resposta = Mock()
        resposta.json.return_value = {"results": []}
        with patch.object(perfil.requests, "get", return_value=resposta), io.StringIO() as buffer, contextlib.redirect_stdout(buffer):
            perfil.gerar_perfil_aleatorio()
            saida = buffer.getvalue()
        self.assertIn("estrutura de dados", saida)

    def test_cep_invalido_nao_consulta_api(self):
        with patch.object(cep.requests, "get") as get:
            cep.consultar_cep("00<script>")
        get.assert_not_called()

    def test_cep_valido_usa_timeout(self):
        resposta = Mock()
        resposta.json.return_value = {"cep": "74000-000", "logradouro": "Rua A",
                                       "bairro": "Centro", "localidade": "Goiânia", "uf": "GO"}
        with patch.object(cep.requests, "get", return_value=resposta) as get, io.StringIO() as buffer, contextlib.redirect_stdout(buffer):
            cep.consultar_cep("74000-000")
            saida = buffer.getvalue()
        get.assert_called_once_with("https://viacep.com.br/ws/74000000/json/", timeout=(3, 8))
        self.assertIn("Goiânia", saida)

    def test_moeda_invalida_nao_consulta_api(self):
        with patch.object(cotacao.requests, "get") as get:
            cotacao.consultar_cotacao("USD/../SECRET")
        get.assert_not_called()

    def test_moeda_valida_usa_timeout(self):
        resposta = Mock()
        resposta.json.return_value = {"USDBRL": {
            "name": "Dólar/Real", "timestamp": "1700000000",
            "bid": "5.15", "high": "5.20", "low": "5.10"
        }}
        with patch.object(cotacao.requests, "get", return_value=resposta) as get, io.StringIO() as buffer, contextlib.redirect_stdout(buffer):
            cotacao.consultar_cotacao(" usd ")
            saida = buffer.getvalue()
        get.assert_called_once_with("https://economia.awesomeapi.com.br/json/last/USD-BRL", timeout=(3, 8))
        self.assertIn("5.1500", saida)


if __name__ == "__main__":
    unittest.main()
