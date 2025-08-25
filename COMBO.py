import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
ventana = tk.Tk()
ventana.title("Ejemplo Combobox")
ventana.geometry("900x1000")
etiqueta = tk.Label(ventana, text="Seleccione especialidad: ")
etiqueta.grid(row=0, column=0, padx=5, pady=5, sticky="w")
#CREAR COMBOBOX
opciones = ["Cardiologia", "Neurlogia", "Pediatria", "Dermatologia"]
combo = ttk.Combobox(ventana, values=opciones, state="readonly")
combo.current(0)     #seleccion primera opcion por defeo
combo.grid(row=0, column=1, padx=10, pady=10)
#funcion para mostrar la selecccion
def mostrar():
    seleccion = combo.get()
    tk.messagebox.showinfo("Seleccion", f"Has elegido:{seleccion}")
#BOTON PARA CONFIRMAT SELCCION
boton = tk.Button(ventana, text="Aceptar", command=mostrar)
boton.grid(row=1, column=0, columnspan=2, pady=10)



ventana.mainloop()



