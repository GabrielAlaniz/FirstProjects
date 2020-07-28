from tkinter import *
import parser


#---------- VENTANA ----------
raiz = Tk()
raiz.title("Calculadora")
raiz.resizable(False,False)

#---------- FRAME ----------
miFrame = Frame(raiz)
miFrame.config(bd=20) #grosor del borde del frame
miFrame.config(relief="groove") # tipo de borde del frame
miFrame.config(cursor="hand2") # cursor

miFrame.pack()

#---------- PANTALLA ----------
pantalla = Entry(miFrame)
pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=6,sticky=W+E)
pantalla.config(bg="black",fg="#03f943",justify="right",font="32")


#---------- FUNCIONES ----------
i = 0 # indice de nums insertados

# funcion que concatena numeros en el display
def get_numeros(num):
	global i
	pantalla.insert(i,num)
	i+=1

def borrar_pantalla():
	pantalla.delete(0, END)

def borrar_caracter():
	get_pantalla =  pantalla.get()
	if len(get_pantalla): # si existe un numero, barra el ultimo caracter
		pantalla_sin_ult = get_pantalla[:-1]
		borrar_pantalla()
		pantalla.insert(0, pantalla_sin_ult)
	else: # si no hay numeros, resetea pantalla y da msj de error
		borrar_pantalla()
		pantalla.insert(0, "Error")

def get_operacion(operador):
	global i

	operador_length = len(operador)
	pantalla.insert(i,operador)
	i+=operador_length

def calcular():
	get_pantalla = pantalla.get()
	
	try:
		expresion = parser.expr(get_pantalla).compile()
		result = eval(expresion)
		borrar_pantalla()
		pantalla.insert(0,result)
	except Exception:
		borrar_pantalla()
		pantalla.insert(0,"Error")



#---------- FILA 1 ----------
Button(miFrame,font=32, text="%", width=6, command=lambda: get_operacion("%")).grid(row=2,column=1)
Button(miFrame,font=32, text="AC", width=6, command=lambda: borrar_pantalla()).grid(row=2,column=2)
Button(miFrame,font=32, text="⬅", width=6, command=lambda: borrar_caracter()).grid(row=2,column=3)
Button(miFrame,font=32, text="/", width=6, command=lambda: get_operacion("/")).grid(row=2,column=4)
# verticales
Button(miFrame,font=32, text="*", width=6, command=lambda: get_operacion("*")).grid(row=3,column=4)
Button(miFrame,font=32, text="+", width=6, command=lambda: get_operacion("+")).grid(row=4,column=4)
Button(miFrame,font=32, text="-", width=6, command=lambda: get_operacion("-")).grid(row=5,column=4)

Button(miFrame,font=32, text="=", width=8, command=lambda: calcular()).grid(row=6,column=4)

#---------- NUMEROS ----------
Button(miFrame,font=32, text="7", width=6, command=lambda: get_numeros(7)).grid(row=3,column=1)
Button(miFrame,font=32, text="8", width=6, command=lambda: get_numeros(8)).grid(row=3,column=2)
Button(miFrame,font=32, text="9", width=6, command=lambda: get_numeros(9)).grid(row=3,column=3)

Button(miFrame,font=32, text="4", width=6, command=lambda: get_numeros(4)).grid(row=4,column=1)
Button(miFrame,font=32, text="5", width=6, command=lambda: get_numeros(5)).grid(row=4,column=2)
Button(miFrame,font=32, text="6", width=6, command=lambda: get_numeros(6)).grid(row=4,column=3)

Button(miFrame,font=32, text="1", width=6, command=lambda: get_numeros(1)).grid(row=5,column=1)
Button(miFrame,font=32, text="2", width=6, command=lambda: get_numeros(2)).grid(row=5,column=2)
Button(miFrame,font=32, text="3", width=6, command=lambda: get_numeros(3)).grid(row=5,column=3)

Button(miFrame,font=32, text="0", width=6, command=lambda: get_numeros(0)).grid(row=6,column=2)
#Button(miFrame,text=",", width=6).grid(row=6,column=3)

raiz.mainloop()