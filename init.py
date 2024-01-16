from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk

root = ThemedTk(theme="yura")

class Funcs():


    def limpar_tela(self):
        self.resultado_campo.config(text="0")
        self.valor = ''
        self.valor1 = ''
        self.valor2 = ''
        self.novo_valor = ''
        self.sinal = ''

    def calcular_resultado(self):
        if self.sinal and self.valor1 and self.valor2:
            resultado = eval(f"{self.valor1}{self.sinal}{self.valor2}")
            self.limpar_tela()
            self.valor1 = str(resultado)
            self.valor = self.valor1
            self.resultado_campo.config(text=self.valor)
            print(f"O Resultado do Calculo foi {self.valor}")



    def adicionarTela(self, novo_valor=''):

        if novo_valor not in '-+/*':
            self.valor += novo_valor
            if not self.sinal:
                self.valor1 += novo_valor
            else:
                self.valor2 += novo_valor
        else:
            if not self.sinal:
                self.sinal = novo_valor
                self.valor += novo_valor
            else:
                # Se um sinal já estiver definido, calculamos o resultado e reiniciamos os valores
                self.calcular_resultado()
                self.sinal = novo_valor
                self.valor += novo_valor

        # Atualize o texto do campo resultado
        self.resultado_campo.config(text=self.valor)

        # Print para verificar os valores
        print(f"Valor: {self.valor}, Valor1: {self.valor1}, Valor2: {self.valor2}, Sinal: {self.sinal}")



class App(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frame_da_tela()
        self.resultado()
        self.valores()
        self.root.mainloop()

    def tela(self):
        self.root.title("Calculadora")

        self.root.geometry("520x6200")
        self.root.maxsize(width=520, height=620)
        self.root.minsize(width=520, height=620)

    def frame_da_tela(self):
        self.frame1 = Frame(self.root)
        self.frame1.place(relx=0, rely=0, relwidth=1, relheight=0.2)
        self.frame2 = Frame(self.root)
        self.frame2.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)


    def resultado(self):
        self.resultado_campo = Label(self.frame1, text="0", font=("Helvetica", 24), anchor=E, padx=20)
        self.resultado_campo.place(relx=0, rely=0, relwidth=1, relheight=1)

    def valores(self):
        self.valor = ''
        self.valor1 = ''
        self.valor2 = ''
        self.novo_valor = ''
        self.sinal = ''
        self.botao_C = ttk.Button(self.frame2, text="C", command=self.limpar_tela)
        self.botao_C.place(relx=0, rely=0, relwidth=0.75, relheight=0.2)
        self.botao_div = ttk.Button(self.frame2, text="/", command=lambda: self.adicionarTela('/'))
        self.botao_div.place(relx=0.75, rely=0, relwidth=0.25, relheight=0.2)

        self.botao_7 = ttk.Button(self.frame2, text="7", command=lambda: self.adicionarTela('7'))
        self.botao_7.place(relx=0, rely=0.2, relwidth=0.25, relheight=0.2)
        self.botao_8 = ttk.Button(self.frame2, text="8", command=lambda: self.adicionarTela('8'))
        self.botao_8.place(relx=0.25, rely=0.2, relwidth=0.25, relheight=0.2)
        self.botao_9 = ttk.Button(self.frame2, text="9", command=lambda: self.adicionarTela('9'))
        self.botao_9.place(relx=0.5, rely=0.2, relwidth=0.25, relheight=0.2)
        self.botao_multi = ttk.Button(self.frame2, text="x", command=lambda: self.adicionarTela('*'))
        self.botao_multi.place(relx=0.75, rely=0.2, relwidth=0.25, relheight=0.2)

        self.botao_4 = ttk.Button(self.frame2, text="4", command=lambda: self.adicionarTela('4'))
        self.botao_4.place(relx=0, rely=0.4, relwidth=0.25, relheight=0.2)
        self.botao_5 = ttk.Button(self.frame2, text="5", command=lambda: self.adicionarTela('5'))
        self.botao_5.place(relx=0.25, rely=0.4, relwidth=0.25, relheight=0.2)
        self.botao_6 = ttk.Button(self.frame2, text="6", command=lambda: self.adicionarTela('6'))
        self.botao_6.place(relx=0.5, rely=0.4, relwidth=0.25, relheight=0.2)
        self.botao_sub = ttk.Button(self.frame2, text="-", command=lambda: self.adicionarTela('-'))
        self.botao_sub.place(relx=0.75, rely=0.4, relwidth=0.25, relheight=0.2)

        self.botao_1 = ttk.Button(self.frame2, text="1", command=lambda: self.adicionarTela('1'))
        self.botao_1.place(relx=0, rely=0.6, relwidth=0.25, relheight=0.2)
        self.botao_2 = ttk.Button(self.frame2, text="2", command=lambda: self.adicionarTela('2'))
        self.botao_2.place(relx=0.25, rely=0.6, relwidth=0.25, relheight=0.2)
        self.botao_3 = ttk.Button(self.frame2, text="3", command=lambda: self.adicionarTela('3'))
        self.botao_3.place(relx=0.5, rely=0.6, relwidth=0.25, relheight=0.2)
        self.botao_mais = ttk.Button(self.frame2, text="+", command=lambda: self.adicionarTela('+'))
        self.botao_mais.place(relx=0.75, rely=0.6, relwidth=0.25, relheight=0.2)

        self.botao_0 = ttk.Button(self.frame2, text="0", command=lambda: self.adicionarTela('0'))
        self.botao_0.place(relx=0, rely=0.8, relwidth=0.75, relheight=0.2)
        self.botao_igual = ttk.Button(self.frame2, text='=', command=self.calcular_resultado)
        self.botao_igual.place(relx=0.75, rely=0.8, relwidth=0.25, relheight=0.2)


# Instanciando a aplicação
App()
