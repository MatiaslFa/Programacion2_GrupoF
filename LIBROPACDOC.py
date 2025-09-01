import tkinter as tk
from tkinter import ttk
#crear vent principal
ventana_principal =tk.Tk()
ventana_principal.title("Registro de Pacientes y Doctores")
ventana_principal.geometry("800x800")
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

#Nombre
labelNombre=tk.Label(frame_pacientes,text="Nombre Completo: ")
labelNombre.grid(row=0,column=0,sticky="w",padx=5,pady=5)
nombreP=tk.Entry(frame_pacientes)
nombreP.grid(row=0,column=1,sticky="w",padx=5,pady=5)

#Fecha de nacimiento
labelFechaN=tk.Label(frame_pacientes,text="Fecha de Nacimiento: ")
labelFechaN.grid(row=1,column=0,sticky="w",padx=5,pady=5)
fechaN=tk.Entry(frame_pacientes)
fechaN.grid(row=1,column=1,sticky="w",padx=5,pady=5)

#Edad(readonly)
labelEdad=tk.Label(frame_pacientes,text="Edad: ")
labelEdad.grid(row=2,column=0,sticky="w",padx=5,pady=5)
edadP=tk.Entry(frame_pacientes,state="readonly")
edadP.grid(row=2,column=1,sticky="w",padx=5,pady=5)

#Género
labelGenero=tk.Label(frame_pacientes,text="Género: ")
labelGenero.grid(row=3,column=0,sticky="w",padx=5,pady=5)
genero=tk.StringVar()
genero.set("Masculino") #Valor por defecto
radioMasculino=ttk.Radiobutton(frame_pacientes,text="Masculino",variable=genero,value="Masculino")
radioMasculino.grid(row=3,column=1,sticky="w",padx=5)
radioFemenino=ttk.Radiobutton(frame_pacientes,text="Femenino",variable=genero,value="Femenino")
radioFemenino.grid(row=4,column=1,sticky="w",padx=5)

#Grupo Sanguíneo
labelGrupoSanguineo=tk.Label(frame_pacientes,text="Grupo Sanguíneo: ")
labelGrupoSanguineo.grid(row=5,column=0,sticky="w",padx=5,pady=5)
grupoSanguineo=tk.Entry(frame_pacientes,text="Grupo Sanguíneo")
grupoSanguineo.grid(row=5,column=1,padx=5,pady=5,sticky="w")

#Tipo de Seguro
labelTipoSeguro=tk.Label(frame_pacientes,text="Tipo de seguro: ")
labelTipoSeguro.grid(row=6,column=0,sticky="w",padx=5,pady=5)
tipo_seguro=tk.StringVar()
tipo_seguro.set("Público")#Valor por defecto
comboTipoSeguro=ttk.Combobox(frame_pacientes,values=["Público","Privado","Ninguno"],textvariable=tipo_seguro)
comboTipoSeguro.grid(row=6,column=1,sticky="w",padx=5,pady=5)

#Centro Médico
labelCentroMedico=tk.Label(frame_pacientes,text="Centro de salud: ")
labelCentroMedico.grid(row=7,column=0,sticky="w",padx=5,pady=5)
centro_medico=tk.StringVar()
centro_medico.set("Hospital Central") #Valos por defecto
comboCentroMedico=ttk.Combobox(frame_pacientes,values=["Hospital Central","Clínica Norte","Centro Sur"],textvariable=centro_medico)
comboCentroMedico.grid(row=7,column=1,sticky="w",padx=5,pady=5)

#Frame para los botones
btn_frame=tk.Frame(frame_pacientes)
btn_frame.grid(row=12,column=0,columnspan=2,pady=5,sticky="w")

#Botón Registrar
btn_registrar=tk.Button(btn_frame,text="Registrar",command="")
btn_registrar.grid(row=0,column=0,padx=5)
btn_registrar.configure(bg="LightGreen")

#Botoón eliminar
btn_eliminar=tk.Button(btn_frame,text="Eliminar",command="")
btn_eliminar.grid(row=0,column=1,padx=5)
btn_eliminar.configure(bg="Red")

#Crear TreeView para mostrar pacientes
treeview=ttk.Treeview(frame_pacientes,columns=("Nombre","FechaN","Edad","Genero","GrupoS","TipoS","CentroM"),show="headings")

#Definir encabezados
treeview.heading("Nombre",text="Nombre Completo")
treeview.heading("FechaN",text="Fecha Nacimiento")
treeview.heading("Edad",text="Edad")
treeview.heading("Genero",text="Género")
treeview.heading("GrupoS",text="Grupo Sanguíneo")
treeview.heading("TipoS",text="Tipo de Seguro")
treeview.heading("CentroM",text="Centro de Salud")

#                                                         Definir ancho de columnas
treeview.column("Nombre",width=120)
treeview.column("FechaN",width=120)
treeview.column("Edad",width=50,anchor="center")
treeview.column("Genero",width=60,anchor="center")
treeview.column("GrupoS",width=100,anchor="center")
treeview.column("TipoS",width=100,anchor="center")
treeview.column("CentroM",width=120)

#Indicar el TreeView en la cuadrícula
treeview.grid(row=10,column=0,columnspan=2,sticky="nsew",padx=5,pady=10)

#Scrolibar vertical
scroll_y=ttk.Scrollbar(frame_pacientes,orient="vertical",command=treeview.yview)
treeview.configure(yscrollcommand=scroll_y.set)
scroll_y.grid(row=10,column=2,sticky="w")




















#NOMBRE DOCTOR

labelNombre=tk.Label(frame_doctores, text="Nombre Completo")
labelNombre.grid(row=0, column=0, padx=5, pady=5, sticky="w")
nombreP=tk.Entry(frame_doctores)
nombreP.grid(row=0, column=1, padx=5, pady=5, sticky="w")

#Especialidad
labelEspecialidad=tk.Label(frame_doctores,text="Especialidad: ")
labelEspecialidad.grid(row=2,column=0,sticky="w",padx=5,pady=5)
especialidad=tk.StringVar()
especialidad.set("Pediatria")#Valor por defecto
comboEspecialidad=ttk.Combobox(frame_doctores,values=["Pediatria","Neurología","Cardiología","Traumatología"],textvariable=especialidad)
comboEspecialidad.grid(row=2,column=1,sticky="w",padx=5,pady=5)

#Edad
def mostrarEdad():
    tk.messagebox.showinfo("Edad",f"La edad seleccionada es:{spin.get()}")
labelEdad=tk.Label(frame_doctores,text="Edad: ")
labelEdad.grid(row=3,column=0,padx=5,pady=5,sticky="w")
spin=tk.Spinbox(frame_doctores,from_=1,to=80)
spin.grid(row=3,column=1,padx=5,pady=5,sticky="w")

#Teléfono
labelTelefono=tk.Label(frame_doctores,text="Teléfono: ")
labelTelefono.grid(row=4,column=0,sticky="w",padx=5,pady=5)
telefonoD=tk.Entry(frame_doctores)
telefonoD.grid(row=4,column=1,sticky="w",padx=5,pady=5)

#Frame para los botones
btn_frame=tk.Frame(frame_doctores)
btn_frame.grid(row=10,column=0,columnspan=2,pady=5,sticky="w")

#Botón Registrar
btn_registrar=tk.Button(btn_frame,text="Registrar",command="")
btn_registrar.grid(row=10,column=0,padx=5)
btn_registrar.configure(bg="LightGreen")

#Botoón eliminar
btn_eliminar=tk.Button(btn_frame,text="Eliminar",command="")
btn_eliminar.grid(row=10,column=1,padx=5)
btn_eliminar.configure(bg="Red")

treeview=ttk.Treeview(frame_doctores,columns=("Nombre","Especialidad","Edad","Teléfono"),show="headings")
#Definir encabezados
treeview.heading("Nombre",text="Nombre Completo")
treeview.heading("Especialidad",text="Especialidad")
treeview.heading("Edad",text="Edad")
treeview.heading("Teléfono",text="Teléfono")
#Definir ancho de columnas
treeview.column("Nombre",width=120)
treeview.column("Especialidad",width=120)
treeview.column("Edad",width=60,anchor="center")
treeview.column("Teléfono",width=120,anchor="center")
#Indicar el TreeView en la cuadrícula
treeview.grid(row=7,column=0,columnspan=2,sticky="nsew",padx=5,pady=10)








ventana_principal.mainloop()