#====== CURRENCY CONVERTER ======

import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk

class ConversorMoneda():
	def __init__(self,url):
		self.data = requests.get(url).json() # importo json con valores actuales
		self.monedas = self.data['rates'] # almacena valores en el atributo

	def convertir(self, valor_from, valor_to, monto):
		monto_inicial = monto
		if valor_from != 'USD':
			monto = monto /self.monedas[valor_from]

		# Redondeo a 4 decimales
		monto = round(monto * self.monedas[valor_to], 4)
		return monto

class App(tk.Tk):
	def __init__(self,conversor):
		tk.Tk.__init__(self)
		self.title = 'Conversor de Divisas'
		self.conversor_divisas = conversor

		# Aspecto ventana
		self.geometry("500x230")
		self.configure(bg='lightblue')

		# Etiqueta Titulo
		self.titulo_label = Label(self, text='Conversor de Divisas en Tiempo Real', fg='black', relief=tk.RIDGE, borderwidth=3, bg='lavender')
		self.titulo_label.config(font=('Verdana',15,'bold'))
		self.titulo_label.place(x=40, y=20)

		# Etiqueta valores de referencia
		self.valores_label = Label(self, text=f"1 Peso Argentino = {self.conversor_divisas.convertir('ARS','USD',1)} u$s \nAl dia : {self.conversor_divisas.data['date']}", relief=tk.GROOVE, borderwidth=3)
		self.valores_label.place(x=160, y=70)

		# Dropdown
		self.menu_from = StringVar(self)
		self.menu_from.set("ARS") # valor por defecto
		self.menu_to = StringVar(self)
		self.menu_to.set("USD") # valor por defecto

		font = ("Verdana", 12, "bold")
		self.option_add('*TCombobox*Listbox.font', font)
		self.menu_from_valor = ttk.Combobox(self, textvariable=self.menu_from, values=list(self.conversor_divisas.monedas.keys()), font=font, state='readonly', width=12, justify=tk.CENTER)
		self.menu_from_valor.place(x = 20, y= 140)
		self.menu_to_valor = ttk.Combobox(self, textvariable=self.menu_to, values=list(self.conversor_divisas.monedas.keys()), font=font, state='readonly', width=12, justify=tk.CENTER)
		self.menu_to_valor.place(x = 320, y= 140)

		# Entrada de texto
		valido = (self.register(self.restrictNumberOnly), '%d', '%P')
		self.input_monto = Entry(self,bd=3, relief=tk.RIDGE, justify=tk.CENTER, validate='key', validatecommand=valido)
		self.input_monto.place(x = 36, y = 180)

		# Etiqueta resultado
		self.result_label = Label(self, text='', fg='black', bg='white', relief=tk.RIDGE, justify=tk.CENTER, width=17, borderwidth=3)
		self.result_label.place(x = 336, y = 180)

		# Boton convertir
		self.btn_convertir = Button(self, text='Convertir', fg='black', command=self.perform, bg='lightgrey')
		self.btn_convertir.config(font=('Verdana',10,'bold'))
		self.btn_convertir.place(x=205, y=140)

	def perform(self):
		monto = float(self.input_monto.get())
		val_from = self.menu_from.get()
		val_to = self.menu_to.get()

		monto_result = self.conversor_divisas.convertir(val_from,val_to,monto)
		monto_result = round(monto_result, 2)

		self.result_label.config(text=str(monto_result))

	def restrictNumberOnly(self, action, string):
		regex = re.compile(r"[0-9]*?(\.)?[0-9]*$")
		result = regex.match(string)
		return(string == "" or (string.count('.') <= 1 and result is not None))



if __name__ == '__main__':
	url = 'https://api.exchangerate-api.com/v4/latest/USD'
	conversor = ConversorMoneda(url)

	App(conversor)
	mainloop()