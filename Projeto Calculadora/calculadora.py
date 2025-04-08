# Importação das bibliotecas 

import tkinter as tk
from tkinter import ttk, messagebox
import math

# Função para calcular a expressão
def calcular():
    try:
        expressao = entrada.get()
        resultado = eval(expressao)  # Avalia a expressão matemática
        entrada.delete(0, tk.END)   # Limpa a entrada
        entrada.insert(0, str(resultado))  # Mostra o resultado
        adicionar_historico(f"{expressao} = {resultado}")
    except Exception as e:
        messagebox.showerror("Erro", "Expressão inválida!")

# Função para adicionar texto na entrada
def adicionar_texto(texto):
    entrada.insert(tk.END, texto)

# Função que limpa a entrada de dados
def limpar():
    entrada.delete(0, tk.END)

# Função para adicionar ao histórico
def adicionar_historico(item):
    historico.insert(tk.END, item)

# Calculos de funções avançadas
def calcular_avancado(funcao):
    try:
        valor = float(entrada.get())
        if funcao == "seno":
            resultado = math.sin(math.radians(valor))
        elif funcao == "cosseno":
            resultado = math.cos(math.radians(valor))
        elif funcao == "tangente":
            resultado = math.tan(math.radians(valor))
        elif funcao == "log":
            resultado = math.log10(valor)
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
        adicionar_historico(f"{funcao}({valor}) = {resultado}")
    except Exception as e:
        messagebox.showerror("Erro", "Valor inválido!")

# Janela Principal
janela = tk.Tk()
janela.title("Calculadora Avançada")
janela.geometry("400x600")
janela.configure(bg="#2D2D2D")  # Fundo escuro

# Estilo com ttk
style = ttk.Style()
style.theme_use("clam")  # Tema moderno
style.configure("TButton", font=("Calibri", 12), padding=10, relief="flat", background="#4E4E4E", foreground="white")
style.map("TButton", background=[("active", "#6C6C6C")])
style.configure("TEntry", font=("Calibri", 18), padding=5, relief="flat", fieldbackground="#1E1E1E", foreground="white")

# Campo de entrada
entrada = ttk.Entry(janela, justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Painel de histórico
historico_label = ttk.Label(janela, text="Histórico", font=("Calibri", 10), background="#2D2D2D", foreground="white")
historico_label.grid(row=1, column=0, columnspan=4, pady=5)

historico = tk.Listbox(janela, height=8, bg="#1E1E1E", fg="white", font=("Calibri", 10))
historico.grid(row=2, column=0, columnspan=4, padx=10, pady=5, sticky="nsew")

# Botões da calculadora
botoes = [
    ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("/", 3, 3),
    ("4", 4, 0), ("5", 4, 1), ("6", 4, 2), ("*", 4, 3),
    ("1", 5, 0), ("2", 5, 1), ("3", 5, 2), ("-", 5, 3),
    ("C", 6, 0), ("0", 6, 1), ("=", 6, 2), ("+", 6, 3),
]

for (texto, linha, coluna) in botoes:
    if texto == "=":
        botao = ttk.Button(janela, text=texto, command=calcular)
    elif texto == "C":
        botao = ttk.Button(janela, text=texto, command=limpar)
    else:
        botao = ttk.Button(janela, text=texto, command=lambda t=texto: adicionar_texto(t))
    botao.grid(row=linha, column=coluna, padx=5, pady=5, sticky="nsew")

botoes_avancados = [
    ("seno", 7, 0), ("cosseno", 7, 1), ("tangente", 7, 2), ("log", 7, 3),
]

for (texto, linha, coluna) in botoes_avancados:
    botao = ttk.Button(janela, text=texto, command=lambda t=texto: calcular_avancado(t))
    botao.grid(row=linha, column=coluna, padx=5, pady=5, sticky="nsew")

# Ajustar as proporções das colunas e linhas
for i in range(8):  # 8 linhas (0 a 7)
    janela.grid_rowconfigure(i, weight=1)
for j in range(4):  # 4 colunas (0 a 3)
    janela.grid_columnconfigure(j, weight=1)

# Suporte para entrada pelo teclado
def pressionar_tecla(event):
    tecla = event.char
    if tecla.isnumeric() or tecla in "+-*/.()":
        adicionar_texto(tecla)
    elif tecla == "\r":  # Enter
        calcular()
    elif tecla == "\x08":  # Backspace
        entrada.delete(len(entrada.get()) - 1, tk.END)

janela.bind("<Key>", pressionar_tecla)

janela.mainloop()
