from tkinter import *

ventana = Tk()
ventana.title("CALCULADORA") #nombre de la pagina
ventana.configure(bg="silver")  #color de la ventana 
i = 0

#entrada
e_texto = Entry(ventana, font= ("Arial 15")) #tipo de texto y tamaño de palabras y numeros
e_texto.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5) #parte donde se muestra las operaciones, sumas o restas

# funciones
def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1

def borrar():
    e_texto.delete(0, END)
    i = 0

def eliminar():
    global i 
    texto_actual = e_texto.get()  
    texto_nuevo = texto_actual[:-1] 
    e_texto.delete(0, END)
    e_texto.insert(0, texto_nuevo)
    i -= 1  

def hacer_operacion():
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete(0, END)
    e_texto.insert(0, resultado)
    i = 0

#FUNCION DE BOTONES 
boton1 = Button(ventana, text="1", width=14, height=4, command=lambda: click_boton(1),bg="grey", relief="groove", font=("Arial",12))
boton2 = Button(ventana, text="2", width=14, height=4, command=lambda: click_boton(2),relief="groove",bg="grey", font=("20"))
boton3 = Button(ventana, text="3", width=14, height=4, command=lambda: click_boton(3),relief="groove",bg="grey", font=("15"))
boton4 = Button(ventana, text="4", width=14, height=4, command=lambda: click_boton(4),relief="groove",bg="grey", font=("15"))
boton5 = Button(ventana, text="5", width=14, height=4, command=lambda: click_boton(5),relief="groove",bg="grey", font=("15"))
boton6 = Button(ventana, text="6", width=14, height=4, command=lambda: click_boton(6),relief="groove",bg="grey", font=("15"))
boton7 = Button(ventana, text="7", width=14, height=4, command=lambda: click_boton(7),relief="groove",bg="grey", font=("15"))
boton8 = Button(ventana, text="8", width=14, height=4, command=lambda: click_boton(8),relief="groove",bg="grey", font=("15"))
boton9 = Button(ventana, text="9", width=14, height=4, command=lambda: click_boton(9),relief="groove",bg="grey", font=("15"))
boton0 = Button(ventana, text="0", width= 14, height=4, command=lambda: click_boton(0),relief="groove",bg="grey", font=("15"))

boton_eliminar = Button(ventana, text="BS", width=14, height=4, command=eliminar, relief="groove", bg="blue", font=(15))
boton_borrar = Button(ventana, text="AC", width=14, height=4, command=lambda: borrar(),relief="groove",bg="blue", font=("15"))
boton_punto = Button(ventana, text=".", width=14, height=4, command=lambda: click_boton("."),  relief="groove",bg="blue", font=("15"))

boton_div = Button(ventana, text="/", width=14, height=4, command=lambda: click_boton("/"),  relief="groove",bg="blue", font=("15"))
boton_mult = Button(ventana, text="*", width=14, height=4, command=lambda: click_boton("*"),  relief="groove",bg="blue", font=("15"))
boton_sum = Button(ventana, text="+", width=14, height=4, command=lambda: click_boton("+"),  relief="groove",bg="blue" ,font=("15"))
boton_rest = Button(ventana, text="-", width=14, height=4, command=lambda: click_boton("-"),  relief="groove",bg="blue", font=("15"))
boton_igual = Button(ventana, text="=", width=14, height=4, command=lambda: hacer_operacion(),relief="groove", bg="blue", font=("15"))

# Agregar botones en pantalla.
boton_eliminar.grid(row=5,column=0, padx=5,pady=5 )
boton_borrar.grid(row=1, column=0, padx=5, pady=5)
boton_div.grid(row=1, column=3, padx=5, pady=5)

boton7.grid(row=2, column=1, padx=5, pady=5)
boton8.grid(row=2, column=0 , padx=5, pady=5)
boton9.grid(row=2, column=2, padx=5, pady=5)
boton_mult.grid(row=2, column=3, padx=5, pady=5)

boton4.grid(row=3, column=0, padx=5, pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
boton_sum.grid(row=3, column=3, padx=5, pady=5)

boton1.grid(row=4, column=0, padx=5, pady=5)
boton2.grid(row=4, column=1, padx=5, pady=5)
boton3.grid(row=4, column=2, padx=5, pady=5)
boton_rest.grid(row=4, column=3, padx=5, pady=5)

boton0.grid(row=5, column=0, columnspan=3, padx=5, pady=5)
boton_punto.grid(row=5, column=2, padx=5, pady=5)
boton_igual.grid(row=5, column=3, padx=5, pady=5)




ventana.mainloop()