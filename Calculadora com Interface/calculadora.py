import tkinter as tk
from tkinter import messagebox
import os

# Função para adicionar dois números
def adicionar(x, y):
    resultado = x + y
    return f'Resultado: {x:.0f} + {y:.0f} = {resultado:.0f}'

# Função para subtrair dois números
def subtrair(x, y):
    resultado = x - y
    return f'Resultado: {x:.0f} - {y:.0f} = {resultado:.0f}'

# Função para multiplicar dois números
def multiplicar(x, y):
    resultado = x * y
    return f'A multiplicacao dos números é: {x:.0f} x {y:.0f} = {resultado:.0f}'

# Função para dividir dois números, com verificação de divisão por zero
def dividir(x, y):
    if y != 0:
        resultado = x / y
        return f'Resultado: {x:.0f} ÷ {y:.0f} = {resultado}'
    else: 
        return 'Erro: Divisao por zero!'
    
# Função para calcular a operação escolhida na interface
def calcular_interface(operacao):
    x = float(entry1.get())
    y = float(entry2.get())

    # Verifica qual operação foi selecionada e chama a função correspondente
    if operacao == '1':
        resultado = adicionar(x, y)
    elif operacao == '2':
        resultado = subtrair(x, y)
    elif operacao == '3':
        resultado = multiplicar(x, y)
    elif operacao == '4':
        resultado = dividir(x, y)
    
    # Exibe o resultado em uma caixa de diálogo
    messagebox.showinfo('Resultado', f'{resultado}')

# Cria a janela principal da aplicação
app = tk.Tk()

# Define o título da janela
app.title("Calculadora")

# Obtém o diretório atual do arquivo .py em execução
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Constrói o caminho absoluto do ícone relativo ao diretório atual
caminho_icone = os.path.abspath(os.path.join(diretorio_atual, "../Calculadora com Interface/Icon.ico"))

# Verifica se o arquivo do ícone existe e define o ícone da aplicação
if os.path.exists(caminho_icone):
    print(f"Ícone encontrado: {caminho_icone}")
    app.iconbitmap(caminho_icone)
else:
    print(f"Arquivo de ícone não encontrado: {caminho_icone}")

# Cria um frame para organizar os widgets na janela
frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

# Cria e posiciona o rótulo e a entrada para o primeiro número
label1 = tk.Label(frame, text='Digite o primeiro número: ')
label1.grid(row=0, column=0, padx=5, pady=5)

entry1 = tk.Entry(frame)
entry1.grid(row=0, column=1, padx=5, pady=5)

# Cria e posiciona o rótulo e a entrada para o segundo número
label2 = tk.Label(frame, text='Digite o segundo número: ')
label2.grid(row=1, column=0, padx=5, pady=5)

entry2 = tk.Entry(frame)
entry2.grid(row=1, column=1, padx=5, pady=5)

# Cria e posiciona o rótulo para a escolha da operação
label3 = tk.Label(frame, text='Escolha a operação:')
label3.grid(row=2, column=0, padx=5, pady=5)

# Variável para armazenar a operação selecionada
var_operacao = tk.StringVar(value='1')

# Cria e posiciona os botões de rádio para as opções de operação
opcoes = ['1. Soma', '2. Subtrair', '3. Multiplicar', '4. Dividir']
for opcao in opcoes:
    rb = tk.Radiobutton(frame, text=opcao, variable=var_operacao, value=opcao[0])
    rb.grid(row=3 + opcoes.index(opcao), column=0, columnspan=2, padx=5, pady=2)

# Cria e posiciona o botão para realizar o cálculo
botao_calcular = tk.Button(frame, text='Calcular', command=lambda: calcular_interface(var_operacao.get()))
botao_calcular.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

# Inicia o loop principal da aplicação
app.mainloop()
