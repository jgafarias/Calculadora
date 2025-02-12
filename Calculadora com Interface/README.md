# Calculadora com Interface Gráfica

Esta é uma calculadora simples com uma interface gráfica criada usando a biblioteca Tkinter do Python. Ela permite realizar operações básicas de adição, subtração, multiplicação e divisão.

## Funcionalidades

- Adição de dois números
- Subtração de dois números
- Multiplicação de dois números
- Divisão de dois números (com verificação de divisão por zero)
- Interface gráfica para entrada de dados e exibição de resultados

## Como Usar

1. Clone este repositório para o seu ambiente local.
2. Certifique-se de ter o Python instalado.
3. Execute o arquivo Python (`calculadora.py`) para iniciar a interface gráfica.

### Exemplo de Uso

1. Digite o primeiro número no campo correspondente.
2. Digite o segundo número no campo correspondente.
3. Selecione a operação desejada (soma, subtração, multiplicação ou divisão) usando os botões de rádio.
4. Clique no botão "Calcular" para ver o resultado em uma caixa de diálogo.

## Estrutura do Código

- **Funções de Operações**:
  - `adicionar(x, y)`: Retorna a soma de `x` e `y`.
  - `subtrair(x, y)`: Retorna a subtração de `x` menos `y`.
  - `multiplicar(x, y)`: Retorna a multiplicação de `x` e `y`.
  - `dividir(x, y)`: Retorna a divisão de `x` por `y` (com verificação de divisão por zero).

- **Função `calcular_interface(operacao)`**:
  - Obtém os valores dos campos de entrada.
  - Verifica qual operação foi selecionada.
  - Chama a função correspondente para calcular o resultado.
  - Exibe o resultado em uma caixa de diálogo.

- **Interface Gráfica**:
  - Criada usando a biblioteca Tkinter.
  - Inclui campos de entrada para os números, botões de rádio para a seleção da operação e um botão para calcular o resultado.

## Personalização

Você pode personalizar esta calculadora adicionando novas funcionalidades ou melhorando a interface gráfica conforme sua necessidade.

## Contribuição

Sinta-se à vontade para contribuir com este projeto. Você pode abrir issues para relatar bugs ou sugerir melhorias, e enviar pull requests para adicionar novas funcionalidades.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE). Veja o arquivo LICENSE para mais detalhes.

## Contato

Para mais informações, entre em contato com o autor:

- **Nome:** João Gabriel
- **GitHub:** [jgafarias](https://github.com/jgafarias)