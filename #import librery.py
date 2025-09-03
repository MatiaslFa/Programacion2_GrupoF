#importamos librerias
import tkinter as tk
from tkinter import ttk
from datetime import datetime
 
#Crear ventana principal
ventana_principal=tk.Tk()
ventana_principal.title("Registro de Pacientes y Doctores")
ventana_principal.geometry("700x900")
 
#Crear contenedor Notebook (pestañas)
pestañas=ttk.Notebook(ventana_principal)
 
#Crear frames (uno por pestaña)
frame_pacientes=ttk.Frame(pestañas)
 
#Agregar pestañas añl Notebook
pestañas.add(frame_pacientes, text="Pacientes")
 
#Mostrar las pestañas en las ventanas
pestañas.pack(expand=True, fill="both")    #fill rellena los espacios

#Funcion para enmascarar fecha
def enmascarar_fecha(texto):
   limpio = "".join(filter(str.isdigit, texto))
   formato_final = ""
   if len(limpio) > 8:
       limpio = limpio[:8]
   if len(limpio) > 4:
       formato_final = f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
   elif len(limpio) > 2:
       formato_final = f"{limpio[:2]}-{limpio[2:]}"
   else:
       formato_final = limpio
   if FechaX.get()!=formato_final:
       FechaX.delete(0,tk.END)
       FechaX.insert(0,formato_final)
   if len(FechaX.get())==10:
       fecha_actual=datetime.now().date()
       fecha_nacimiento=datetime.strptime(FechaX.get(),"%d-%m-%Y").date()
       
       edad=fecha_actual.year-fecha_nacimiento.year 
       edadVar.set(edad)
   else:
       edadVar.set("")
   return True

#Nombre
labelNombre=tk.Label(frame_pacientes, text="Nombre Completo: ")
labelNombre.grid(row=0, column=0, padx=5, pady=5, sticky="w")
nombreX=tk.Entry(frame_pacientes)
nombreX.grid(row=0, column=1, sticky="w", padx=5, pady=5)
 
#Fecha de nacimiento
labelFecha=tk.Label(frame_pacientes, text="Escribir su fecha de nacimiento (DD/MM/AAAA): ")
labelFecha.grid(row=1, column=0, padx=5, pady=5, sticky="w")
validacion_fecha=ventana_principal.register(enmascarar_fecha)
FechaX=ttk.Entry(frame_pacientes,validate="key",validatecommand=(validacion_fecha,"%P")) #esto es para validar los datos,se usa una libreria mas
FechaX.grid(row=1, column=1, sticky="w", padx=5, pady=5)
 
#Edad (READONLY)
labelEdad=tk.Label(frame_pacientes, text="Edad: ")
labelEdad.grid(row=2, column=0, sticky="w", pady=5, padx=5)
edadVar=tk.StringVar()
edadX=tk.Entry(frame_pacientes,textvariable=edadVar, state="readonly")
edadX.grid(row=2, column=1, sticky="w",pady=5,padx=5)
 
#Genero
labelGenero=tk.Label(frame_pacientes, text="Genero: ")
labelGenero.grid(row=3, column=0, sticky="w", pady=5, padx=5)
genero=tk.StringVar()
genero.set("Masculino")    #Valor por defecto
radioMasculino=ttk.Radiobutton(frame_pacientes, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3,column=1, sticky="w", padx=5)
radioFemenino=ttk.Radiobutton(frame_pacientes, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=4, column=1, sticky="w", padx=5)
 
#Grupo Sanguineo
labelGrupSan=tk.Label(frame_pacientes, text="Grupo Sanguineo: ")
labelGrupSan.grid(row=5, column=0, sticky="w", pady=5, padx=5)
entryGrupSan=tk.Entry(frame_pacientes)
entryGrupSan.grid(row=5, column=1, sticky="w", pady=5, padx=5)
 
#Tipo de Seguro (combobox)
labelTipSeg=tk.Label(frame_pacientes, text="Tipo de seguro: ")
labelTipSeg.grid(row=6, column=0, pady=5,padx=5, sticky="w")
tipo_seguro=tk.StringVar()
tipo_seguro.set("Publico")   #valor por defecto
comboTipSeg=ttk.Combobox(frame_pacientes, values=["Publico", "Privado", "Ninguno"], textvariable=tipo_seguro)
comboTipSeg.grid(row=6, column=1, pady=5, padx=5, sticky="w")
 
#Centro medico
labelCentMed=tk.Label(frame_pacientes, text="Centro de Salud: ")
labelCentMed.grid(row=7, column=0, pady=5,padx=5, sticky="w")
centro_medico=tk.StringVar()
centro_medico.set("Hospital Central")   #valor por defecto
comboCentMed=ttk.Combobox(frame_pacientes, values=["Hospital Central", "Clinica Norte", "Centro Sur"], textvariable=centro_medico)
comboCentMed.grid(row=7, column=1, pady=5, padx=5, sticky="w")
 
#Frame para los botones
btn_frame = tk.Frame(frame_pacientes)
btn_frame.grid(row=8, column=0, columnspan=2, pady=5, sticky="w")

# Botón Registrar
btn_registrar = tk.Button(btn_frame,
text="Registrar", command="", bg="green", fg="white")
btn_registrar.grid(row=0, column=0, padx=5)

# Botón Eliminar
btn_eliminar = tk.Button(btn_frame,
text="Eliminar", command="", bg="pink", fg="white")
btn_eliminar.grid(row=0, column=1, padx=5)

#CREAR TREEVIEW PARA MOSTRAR PACIENTES
treeview=ttk.Treeview(frame_pacientes,columns=("Nombre", "FechaN", "Edad", "Genero", "GrupoS","TipoS", "CentroM"), show="headings")
treeview.heading("Nombre", text="Nombre Completo")
treeview.heading("FechaN", text="Fecha de Nacimiento")
treeview.heading("Edad", text="Edad")
treeview.heading("Genero", text="Genero")
treeview.heading("GrupoS", text="Grupo Sanguineo")
treeview.heading("TipoS", text="Tipo Sangiuineo")
treeview.heading("CentroM", text="Centro Medico")
 
#DEFINIR ANCHOS DE COLUMNAS
treeview.column("Nombre", width=120) 
treeview.column("FechaN", width=120) 
treeview.column("Edad", width=50, anchor="center") 
treeview.column("Genero", width=60, anchor="center") 
treeview.column("GrupoS", width=100, anchor="center") 
treeview.column("TipoS", width=100, anchor="center") 
treeview.column("CentroM", width=120)
 
#UBICAR EL TREEVIEW EN LA CUADRICULA
treeview.grid(row=10, column=0, columnspan=2, padx=5, pady=10, sticky="nsew")

#SCROLBAR VERTICAL
scroll_y=ttk.Scrollbar(frame_pacientes, orient="vertical", command=treeview.yview)
scroll_y.grid(row=10, column=2, sticky="ns")
#Mostrar las pestañas en las ventanas
pestañas.pack(expand=True, fill="both")    #fill rellena los espacios
 
#DOCTORES

#frame
frame_doctores=ttk.Frame(pestañas)
pestañas.add(frame_doctores, text="Doctores")
 
#titulo registro de pacientes
tituloLabel=tk.Label(frame_doctores,text="Registro Doctores",font=("Candara",18,"bold"))
tituloLabel.grid(row=0, column=1, padx=10, pady=10)

#Nombre
labelNombre=tk.Label(frame_doctores, text="Nombre: ")
labelNombre.grid(row=1, column=0, padx=5, pady=5, sticky="w")
nombreX=tk.Entry(frame_doctores)
nombreX.grid(row=1, column=1, sticky="w", padx=5, pady=5)
 
#especialidad (combobox)
labelEspecialidad=tk.Label(frame_doctores, text="Especialidad: ")
labelEspecialidad.grid(row=2, column=0, pady=5,padx=5, sticky="w")
especialidad=tk.StringVar()
especialidad.set("Cardiologia")   #valor por defecto
comboEspecialidad=ttk.Combobox(frame_doctores, values=["Cardiologia", "Neurologia", "Pediatria", "Traumatologia"], textvariable=especialidad)
comboEspecialidad.grid(row=2, column=1, pady=5, padx=5, sticky="w")
 
#Edad
edadLabel=tk.Label(frame_doctores,text="Edad:")
edadLabel.grid(row=3,column=0,sticky="w",padx=5,pady=5)
spin=tk.Spinbox(frame_doctores,from_=1,to=99)
spin.grid(row=3,column=1,padx=5,pady=5, sticky="w")
 
#Telefono

labelTelefono=tk.Label(frame_doctores, text="Telefono: ")
labelTelefono.grid(row=4, column=0, padx=5, pady=5, sticky="w")
telefonoX=tk.Entry(frame_doctores)
telefonoX.grid(row=4, column=1, sticky="w", padx=5, pady=5)
#Frame para los botones
btn_frame = tk.Frame(frame_doctores)
btn_frame.grid(row=6, column=0, columnspan=2, pady=5, sticky="w")

# Botón Registrar

btn_registrar = tk.Button(btn_frame,
text="Registrar", command="", bg="green", fg="white")
btn_registrar.grid(row=7, column=0, padx=5)
# Botón Eliminar

btn_eliminar = tk.Button(btn_frame,
text="Eliminar", command="", bg="red", fg="white")
btn_eliminar.grid(row=7, column=2, padx=5)

#CREAR TREEVIEW PARA MOSTRAR DOCTORES

treeview=ttk.Treeview(frame_doctores,columns=("Nombre", "Especialidad", "Edad", "Telefono"), show="headings")
treeview.heading("Nombre", text="Nombre Completo")
treeview.heading("Especialidad", text="Especialidad")
treeview.heading("Edad", text="Edad")
treeview.heading("Telefono", text="Telefono")
 
#DEFINIR ANCHOS DE COLUMNAS

treeview.column("Nombre", width=120) 
treeview.column("Especialidad", width=120) 
treeview.column("Edad", width=50, anchor="center") 
treeview.column("Telefono", width=60, anchor="center") 
treeview.grid(row=8, column=0, columnspan=2, padx=5, pady=10, sticky="nsew")
 
#SCROLBAR VERTICAL

scroll_y=ttk.Scrollbar(frame_doctores, orient="vertical", command=treeview.yview)
scroll_y.grid(row=8, column=2, sticky="nsew")
ventana_principal.mainloop()