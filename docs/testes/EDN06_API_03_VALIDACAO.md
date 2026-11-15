# EDN06-API-03 — Validação de respostas externas

14/11/2026 · Consulta CEP ViaCEP e cotação AwesomeAPI.

## Defeitos
- `str.isdigit()` aceita numerais Unicode como １２３４５６７８, que não são os dígitos decimais ASCII esperados pelo endpoint /ws/{cep}/json/. Tipos não texto geravam AttributeError.
- A cotação externa podia fornecer `NaN`, `Infinity`, valores negativos e timestamps fora do intervalo. O programa imprimia cotações falsas ou estourava exceção sem tratamento.

## Contratos
- CEP aceita apenas oito dígitos ASCII, com separadores de entrada já previstos; tipos incorretos são rejeitados antes de qualquer chamada HTTP.
- Valores bid/high/low devem ser positivos e finitos antes de serem exibidos.
- Timestamp é interpretado em UTC e erros de intervalo são tratados sem traceback.
- Testes unittest com requests mockados cobrem casos adversariais; não há consultas reais aos provedores na CI.

## Limites
A verificação de formato não certifica veracidade, licença, disponibilidade ou oportunidade temporal dos dados do provedor. Serviços externos podem alterar contratos.
