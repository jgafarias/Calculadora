# Calculadora Simples

Este é um programa de calculadora simples escrito em Python que pode realizar as quatro operações básicas: soma, subtração, multiplicação e divisão. Após cada operação, o programa pergunta ao usuário se ele deseja continuar, e se sim, reinicia o processo.

## Funcionalidades

- Soma
- Subtração
- Multiplicação
- Divisão

## Como usar

1. Clone ou faça o download deste repositório.
2. Execute o arquivo Python `calculadora.py`.
3. Escolha a operação desejada digitando o número correspondente:
    - 1. Soma
    - 2. Subtração
    - 3. Multiplicação
    - 4. Divisão
4. Insira os dois números que deseja calcular.
5. O resultado será exibido no console.
6. O programa perguntará se você deseja continuar. Digite 's' para sim ou 'n' para não.
7. Se 's' for selecionado, o programa reiniciará. Se 'n' for selecionado, o programa será encerrado.

## Estrutura do Código

O código consiste nas seguintes funções:

- `adicionar(x, y)`: Realiza a soma de `x` e `y` e imprime o resultado.
- `subtrair(x, y)`: Realiza a subtração de `y` de `x` e imprime o resultado.
- `multiplicar(x, y)`: Realiza a multiplicação de `x` e `y` e imprime o resultado.
- `dividir(x, y)`: Realiza a divisão de `x` por `y` e imprime o resultado (verifica se `y` não é zero).
- `calcular()`: Função principal que solicita a entrada do usuário para escolher a operação e os números, e chama a função apropriada para realizar o cálculo.

## Exemplo de Uso

```python
adicionar(5, 3)
# Saída: A soma dos números é: 5 + 3 = 8

subtrair(10, 4)
# Saída: A subtracao dos números é: 10 - 4 = 6

multiplicar(2, 7)
# Saída: A multiplicacao dos números é: 2 * 7 = 14

dividir(20, 4)
# Saída: A divisao dos números é: 20 / 4 = 5.0
``` 

## Requisitos
- Python 3.x
- 
## Contato

Para mais informações, entre em contato com o autor:

- **Nome:** João Gabriel
- **GitHub:** [jgafarias](https://github.com/jgafarias)
