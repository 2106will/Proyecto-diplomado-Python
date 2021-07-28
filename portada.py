from tkinter import *
import operaciones

#Funciones para los botones

def comando_visualizar():
    lista.delete(0, END)
    lista_libros = operaciones.visualizar()
    for libro in lista_libros:
        lista.insert(END, libro)

def comando_buscar():
    lista.delete(0, END)
    lista_libros = operaciones.buscar(titulo.get(), autor.get(), year.get(), isbn.get())
    for libro in lista_libros:
        lista.insert(END, libro)

def comando_insertar():
    operaciones.insertar(titulo.get(), autor.get(), year.get(), isbn.get()),lista.delete(0, END)
    lista.insert(END, (titulo.get(), autor.get(),year.get(), isbn.get()))

def recoger_fila_seleccionada(event):
    try:
        global libro_seleccionado
        indice = lista.curselection()[0]
        libro_seleccionado = lista.get(indice)

        entrada1.delete(0, END)
        entrada1.insert(END, libro_seleccionado[1])

        entrada2.delete(0, END)
        entrada2.insert(END, libro_seleccionado[2])

        entrada3.delete(0, END)
        entrada3.insert(END, libro_seleccionado[3])

        entrada4.delete(0, END)
        entrada4.insert(END, libro_seleccionado[4])
    
    except IndexError:
        pass

def comando_actualizar():
    operaciones.actualizar(titulo.get(), autor.get(), 
    year.get(), isbn.get(), libro_seleccionado[0])
    lista.delete(0, END)
    lista.insert(END, "Libro actualizado correctamente") 

def comando_borrar():
    operaciones.borrar(libro_seleccionado[0])
    lista.delete(0, END)
    lista.insert(END, "Libro borrado correctamente") 

def comando_cerrar():
    ventana.destroy()


#Ventana de la aplicacion

ventana = Tk()
ventana.iconbitmap("letra_b.ico")
imagen = PhotoImage(file= "andina6.png")
fondo = Label(ventana, image=imagen, height=40, width=200).place(x=300, y=7)

#Etiquetas de texto

etiqueta1 = Label(ventana, text="Titulo", font=("Comic Sans MS", 11))
etiqueta1.grid(row=0, column= 0)

etiqueta2 = Label(ventana, text="Autor", font=("Comic Sans MS", 11))
etiqueta2.grid(row=0, column= 2)

etiqueta3 = Label(ventana, text="Año", font=("Comic Sans MS", 11))
etiqueta3.grid(row=1, column= 0)

etiqueta4 = Label(ventana, text="ISBN", font=("Comic Sans MS", 11))
etiqueta4.grid(row=1, column= 2)


#Entrada de texto
titulo = StringVar()
entrada1 = Entry(ventana, textvariable= titulo)
entrada1.grid(row=0, column=1)
entrada1.config(bd=2)

autor = StringVar()
entrada2 = Entry(ventana, textvariable= autor)
entrada2.grid(row=0, column=3)
entrada2.config(bd=2)

year = StringVar()
entrada3 = Entry(ventana, textvariable= year)
entrada3.grid(row=1, column=1)
entrada3.config(bd=2)

isbn = StringVar()
entrada4 = Entry(ventana, textvariable= isbn)
entrada4.grid(row=1, column=3)
entrada4.config(bd=2)

#Pantalla y scrollbar

lista = Listbox(ventana, height=12, width=50)
lista.grid(row=2, column=0, rowspan=6, columnspan=7)
lista.config(bd=2)

scrollbar = Scrollbar(ventana)
scrollbar.grid(row=2, column=6, rowspan=6, sticky="nsew")
lista.config(yscrollcommand=scrollbar.set)

lista.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=lista.yview)

#Incluimos un evento a la lista

lista.bind('<<ListboxSelect>>', recoger_fila_seleccionada)

#Botones

boton1 = Button(ventana, text="Visualizar", width=12, command=comando_visualizar)
boton1.grid(row=2, column=7, padx= 4, pady=4)

boton2 = Button(ventana, text="Buscar", width=12, command= comando_buscar)
boton2.grid(row=3, column=7, padx= 4, pady=4)

boton3 = Button(ventana, text="Añadir", width=12, command=comando_insertar)
boton3.grid(row=4, column=7, padx= 4, pady=4)

boton4 = Button(ventana, text="Actualizar", width=12, command=comando_actualizar)
boton4.grid(row=5, column=7, padx= 4, pady=4)

boton5 = Button(ventana, text="Borrar", width=12, command= comando_borrar)
boton5.grid(row=6, column=7, padx= 4, pady=4)

boton6 = Button(ventana, text="Cerrar", width=12, command= comando_cerrar)
boton6.grid(row=7, column=7, padx= 4, pady=4)


ventana.title("Bookapp")
ventana.mainloop()


