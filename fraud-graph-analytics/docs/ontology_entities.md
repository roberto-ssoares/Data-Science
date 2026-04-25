# Ontologia Inicial do Domínio Antifraude

| entidade     | descricao                                                                  | exemplo_atributos                                             | papel_no_grafo                                                    |
|:-------------|:---------------------------------------------------------------------------|:--------------------------------------------------------------|:------------------------------------------------------------------|
| Cliente      | Pessoa física ou perfil cadastral associado a uma ou mais contas.          | cliente_id, idade, segmento, data_cadastro, score_cadastral   | Nó principal para análise de comportamento e relacionamento.      |
| Conta        | Conta transacional utilizada para envio ou recebimento de valores.         | conta_id, cliente_id, data_abertura, status_conta, tipo_conta | Nó central para análise de transações e conexões suspeitas.       |
| Transacao    | Evento financeiro realizado entre origem e destino.                        | transacao_id, valor, data_hora, tipo_transacao, canal, status | Evento que conecta conta, beneficiário, dispositivo, IP e regras. |
| Beneficiario | Conta, pessoa ou entidade que recebe uma transação.                        | beneficiario_id, tipo_beneficiario, banco_destino, chave_pix  | Nó usado para detectar concentração de recebimentos.              |
| Dispositivo  | Aparelho ou identificador técnico utilizado para realizar transações.      | device_id, tipo_device, sistema_operacional, fingerprint      | Nó crítico para detectar compartilhamento entre múltiplas contas. |
| IP           | Endereço ou faixa de rede de origem da operação.                           | ip_id, ip, cidade, uf, pais, tipo_rede                        | Nó auxiliar para identificar origens comuns de acesso.            |
| Cartao       | Cartão físico ou virtual associado a operações financeiras.                | cartao_id, tipo_cartao, data_emissao, status_cartao           | Nó complementar para análise de uso compartilhado ou atípico.     |
| Regra        | Regra antifraude acionada por comportamento suspeito.                      | regra_id, nome_regra, severidade, descricao                   | Nó explicativo conectado às transações suspeitas.                 |
| Comunidade   | Grupo de nós fortemente conectados por relações transacionais ou técnicas. | comunidade_id, tamanho, score_risco, qtd_alertas              | Agrupamento usado para investigação de redes coordenadas.         |
