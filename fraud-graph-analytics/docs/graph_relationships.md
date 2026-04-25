# Modelo Inicial de Relações do Knowledge Graph

| origem    | relacao                     | destino      | descricao                                                         | exemplo                                           |
|:----------|:----------------------------|:-------------|:------------------------------------------------------------------|:--------------------------------------------------|
| Cliente   | POSSUI                      | Conta        | Cliente possui uma ou mais contas transacionais.                  | (:Cliente)-[:POSSUI]->(:Conta)                    |
| Conta     | REALIZOU                    | Transacao    | Conta originou uma transação financeira.                          | (:Conta)-[:REALIZOU]->(:Transacao)                |
| Transacao | ENVIOU_PARA                 | Beneficiario | Transação foi enviada para um beneficiário.                       | (:Transacao)-[:ENVIOU_PARA]->(:Beneficiario)      |
| Transacao | USOU                        | Dispositivo  | Transação foi realizada a partir de um dispositivo.               | (:Transacao)-[:USOU]->(:Dispositivo)              |
| Transacao | ORIGINOU_DE                 | IP           | Transação teve origem em um IP ou faixa de rede.                  | (:Transacao)-[:ORIGINOU_DE]->(:IP)                |
| Transacao | UTILIZOU                    | Cartao       | Transação utilizou cartão físico ou virtual.                      | (:Transacao)-[:UTILIZOU]->(:Cartao)               |
| Transacao | ACIONOU                     | Regra        | Transação acionou uma regra antifraude.                           | (:Transacao)-[:ACIONOU]->(:Regra)                 |
| Conta     | COMPARTILHA_DISPOSITIVO_COM | Conta        | Contas diferentes utilizaram o mesmo dispositivo.                 | (:Conta)-[:COMPARTILHA_DISPOSITIVO_COM]->(:Conta) |
| Conta     | ENVIOU_VALOR_PARA           | Conta        | Conta enviou valor para outra conta ou beneficiário interno.      | (:Conta)-[:ENVIOU_VALOR_PARA]->(:Conta)           |
| Conta     | PERTENCE_A                  | Comunidade   | Conta pertence a uma comunidade detectada por algoritmo de grafo. | (:Conta)-[:PERTENCE_A]->(:Comunidade)             |
