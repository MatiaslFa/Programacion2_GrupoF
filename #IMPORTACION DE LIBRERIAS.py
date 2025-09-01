#IMPORTACION DE LIBRERIAS
import tkinter as tk
from tkinter import ttk
#crear vent principal
ventana_principal =tk.Tk()
ventana_principal.title("Registro de Pacientes y Doctores")
ventana_principal.geometry("400x600")
#rear contenedor notebook PESTAÑA
pestañas = ttk.Notebook(ventana_principal)
#crear frames 1 por pestaña
frame_pacientes = ttk.Frame(pestañas)
#agregar pestaña a notebook
pestañas.add(frame_pacientes, text="Pacientes")
#mostrar las pestañas en las ventanas
pestañas.pack(expand=True, fill="both")
#PESTAÑA DOCTOR
frame_doctores = ttk.Frame(pestañas)
pestañas.add(frame_doctores, text="Doctores")
#                                                                  NOMBRE
labelNombre=tk.Label(frame_pacientes, text="Nombre Completo")
labelNombre.grid(row=0, column=0, padx=5, pady=5, sticky="w")
nombreP=tk.Entry(frame_pacientes)
nombreP.grid(row=0, column=1, padx=5, pady=5, sticky="w")
#        FECHA DE NACIMIENTO
labelFecha=tk.Label(frame_pacientes, text="Fecha de Nacimiento")
labelFecha.grid(row=1, column=0, padx=5, pady=5, sticky="w")
fechaN=tk.Entry(frame_pacientes)
fechaN.grid(row=1, column=1, padx=5, pady=5, sticky="w")
#         EDAD readonly
labelEdad=tk.Label(frame_pacientes, text="Edad: ")
labelEdad.grid(row=2, column=0, padx=5, pady=5, sticky="w")
edadP=tk.Entry(frame_pacientes, state="readonly")
edadP.grid(row=2, column=1, padx=5, pady=5, sticky="w")
#              GENERO
labelGenero=tk.Label(frame_pacientes, text="Genero: ")
labelGenero.grid(row=3, column=0, padx=5, pady=5, sticky="w")
genero=tk.StringVar()
genero.set("Masculino")         
#         VALOR POR DEFECTO
radioMasculino=ttk.Radiobutton(frame_pacientes, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, padx=5, sticky="w")

radioFemenino=ttk.Radiobutton(frame_pacientes, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=4, column=1, padx=5, sticky="w")
#GRUPO SANGUINEO
labelGrupoSanguineo=tk.Label(frame_pacientes, text="Grupo Sanguineo: ")
labelGrupoSanguineo.grid(row=5, column=0, padx=5, pady=5, sticky="w")
entryGrupoSanguineo=tk.Entry(frame_pacientes)
entryGrupoSanguineo.grid(row=5, column=1, padx=5, pady=5, sticky="w")
#       TIPO D SEGURO
labelTipoSeguro=tk.Label(frame_pacientes, text="Tipo de Seguro: ")
labelTipoSeguro.grid(row=6, column=0, padx=5, pady=5, sticky="w")
tipo_seguro=tk.StringVar()
tipo_seguro.set("Publico")         #VALOR POR DEFECTO
comboTipSeguro=ttk.Combobox(frame_pacientes, values=["Publico", "Privado", "Ninguno"], textvariable=tipo_seguro)
comboTipSeguro.grid(row=6, column=1, padx=5, pady=5, sticky="w")
#CENTRO MEDICO
labelCentroMedico=tk.Label(frame_pacientes, text="Centro de Salud: ")
labelCentroMedico.grid(row=7, column=0, padx=5, pady=5, sticky="w")
centro_medico=tk.StringVar()
centro_medico.set("Hospital Central")         #VALOR POR DEFECTO
comboCentroMedico=ttk.Combobox(frame_pacientes, values=["Hospital Central", "Clinica Norte", "Centro Sur"], textvariable=centro_medico)
comboCentroMedico.grid(row=7, column=1, padx=5, pady=5, sticky="w")

#NOMBRE DOCTOR

labelNombre=tk.Label(frame_doctores, text="Nombre Completo")
labelNombre.grid(row=0, column=0, padx=5, pady=5, sticky="w")
nombreP=tk.Entry(frame_doctores)
nombreP.grid(row=0, column=1, padx=5, pady=5, sticky="w")

#        FECHA DE NACIMIENTO
labelFecha=tk.Label(frame_doctores, text="Fecha de Nacimiento")
labelFecha.grid(row=1, column=0, padx=5, pady=5, sticky="w")
fechaN=tk.Entry(frame_doctores)
fechaN.grid(row=1, column=1, padx=5, pady=5, sticky="w")
#         EDAD readonly
labelEdad=tk.Label(frame_doctores, text="Edad: ")
labelEdad.grid(row=2, column=0, padx=5, pady=5, sticky="w")
edadP=tk.Entry(frame_doctores, state="readonly")
edadP.grid(row=2, column=1, padx=5, pady=5, sticky="w")
#              GENERO
labelGenero=tk.Label(frame_doctores, text="Genero: ")
labelGenero.grid(row=3, column=0, padx=5, pady=5, sticky="w")
genero=tk.StringVar()
genero.set("Masculino")

radioMasculino=ttk.Radiobutton(frame_doctores, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, padx=5, sticky="w")

radioFemenino=ttk.Radiobutton(frame_doctores, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=4, column=1, padx=5, sticky="w")


#       TIPO D SEGURO
labelTipoSeguro=tk.Label(frame_doctores, text="Tipo de Seguro: ")
labelTipoSeguro.grid(row=6, column=0, padx=5, pady=5, sticky="w")
tipo_seguro=tk.StringVar()
tipo_seguro.set("Publico")         #VALOR POR DEFECTO
comboTipSeguro=ttk.Combobox(frame_doctores, values=["Publico", "Privado", "Ninguno"], textvariable=tipo_seguro)
comboTipSeguro.grid(row=6, column=1, padx=5, pady=5, sticky="w")
#CENTRO MEDICO
labelCentroMedico=tk.Label(frame_doctores, text="Centro de Salud: ")
labelCentroMedico.grid(row=7, column=0, padx=5, pady=5, sticky="w")
centro_medico=tk.StringVar()
centro_medico.set("Hospital Central")         #VALOR POR DEFECTO
comboCentroMedico=ttk.Combobox(frame_doctores, values=["Hospital Central", "Clinica Norte", "Centro Sur"], textvariable=centro_medico)
comboCentroMedico.grid(row=7, column=1, padx=5, pady=5, sticky="w")









ventana_principal.mainloop()