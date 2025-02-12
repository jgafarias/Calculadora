def adicionar(x, y):
    resultado = x + y
    print(f'A soma dos números é: {x:.0f} + {y:.0f} = {resultado:.0f}')

def subtrair(x, y):
    resultado = x - y
    print(f'A subtracao dos números é: {x:.0f} - {y:.0f} = {resultado:.0f}')

def multiplicar(x, y):
    resultado = x * y
    print(f'A multiplicacao dos números é: {x:.0f} * {y:.0f} = {resultado:.0f}')

def dividir(x, y):
    if y != 0:
        resultado = x / y
        print(f'A divisao dos números é: {x:.0f} / {y:.0f} = {resultado}')
    else: 
        return 'Erro: Divisao por zero!'
    
def calcular():

    print('Selecione uma opcao: ')
    print('---------------------')
    print('1. Soma')
    print('2. Subtrair')
    print('3. Multiplicar')
    print('4. Dividir')

    escolha = input('Digite o número corresponde a sua escolha: ')

    x = float(input('Digite o primeiro número: '))
    y = float(input('Digite o segundo número: '))

    if escolha == '1':
        adicionar(x, y)
    elif escolha == '2': 
        subtrair(x, y)
    elif escolha == '3':
        multiplicar(x, y)
    elif escolha == '4':
        dividir(x, y)
    else: 
        print('Por favor escolha uma opcao')
        
if __name__ == "__main__":
    calcular()
    
while True:
    resposta = input("Você quer continuar? (s/n): ").strip().lower()
    if resposta == 's':
        calcular()
        break
    elif resposta == 'n':
        print("Encerrando o programa. Até a próxima!")
        break
    else:
        print("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")
            

            