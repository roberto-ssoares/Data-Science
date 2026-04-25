# Taxonomia Inicial de Fraudes

| categoria                    | descricao                                                                        | sinais_esperados                                                                         | prioridade_mvp   |
|:-----------------------------|:---------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|:-----------------|
| Fraude transacional          | Movimentação financeira suspeita realizada por canais digitais ou transacionais. | Valor alto, frequência incomum, horário atípico, beneficiário suspeito.                  | Alta             |
| Conta laranja / mule account | Conta usada para receber, intermediar ou pulverizar valores suspeitos.           | Muitos recebimentos, muitos envios, baixa idade da conta, conexões com múltiplos grupos. | Alta             |
| Beneficiário concentrador    | Recebedor que concentra valores oriundos de diversas contas.                     | Alto grau de entrada, alta recorrência, origem pulverizada.                              | Alta             |
| Dispositivo compartilhado    | Mesmo dispositivo utilizado por várias contas diferentes.                        | Múltiplas contas por device_id, acessos em sequência, transações relacionadas.           | Alta             |
| Rede coordenada              | Grupo de entidades conectadas atuando com padrão semelhante ou complementar.     | Comunidade densa, alta repetição de relações, padrões temporais próximos.                | Alta             |
| Conta nova com alto valor    | Conta recém-criada realizando movimentações acima do esperado.                   | Baixa idade cadastral, valor elevado, ausência de histórico.                             | Média            |
| Transações em rajada         | Muitas transações realizadas em curto intervalo de tempo.                        | Alta frequência em janela curta, valores fracionados, destinos repetidos.                | Média            |
| Conta ponte                  | Conta que conecta comunidades ou fluxos financeiros distintos.                   | Alta intermediação, conexão entre grupos, movimentação de entrada e saída.               | Média            |
