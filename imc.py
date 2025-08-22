import tkinter as tkinter 
from tkinter import messagebox
def imc_calc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc = peso /(altura*altura)
        messagebox.showinfo("Resultdo",f"seu IMC é{imc:.2f}")
    except ValueError:
        messagebox.showinfo("Erro", "Por Favor insira numeros válidos")

# Janela Principal
janela = tk.Tk()
janela.title("Calculadora IMC")
janela.geometry("300x200")

# Rótulos e entradas
label_peso = tk.Label(janela, text="Peso (kg):")
label_peso.pack(pady=5)
entry_peso = tk.Entry(janela)
entry_peso.pack()

label_altura = tk.Label(janela, text="Altura (m):")
label_altura.pack(pady=5)
entry_altura = tk.Entry(janela)
entry_altura.pack()

# Botão calcular
botao = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
botao.pack(pady=20)

# Iniciar programa
janela.mainloop()