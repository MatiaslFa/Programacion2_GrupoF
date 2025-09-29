# Importación de librerías
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
 
# funcion para enmascarar fecha
# Nota: usa las variables globales fechaN y edadVar que se definen más abajo
 
def enmascarar_fecha(texto):
    limpio = ''.join(filter(str.isdigit, texto))
    formato_final = ""
 
    if len(limpio) > 8:
        limpio = limpio[:8]
    if len(limpio) > 4:
        formato_final = f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
    elif len(limpio) > 2:
        formato_final = f"{limpio[:2]}-{limpio[2:]}"
    else:
        formato_final = limpio
 
    if fechaN.get() != formato_final:
        fechaN.delete(0, tk.END)
        fechaN.insert(0, formato_final)
 
    if len(fechaN.get()) == 10:
        fecha_actual = datetime.now().date()
        fecha_nacimiento = datetime.strptime(fechaN.get(), "%d-%m-%Y").date()
        edad = fecha_actual.year - fecha_nacimiento.year
        edadVar.set(edad)
    else:
        edadVar.set("")
    return True
 
# Persistencia de pacientes
 
def guardar_en_archivo():
    with open("pacienteEstatura.txt", "w", encoding="utf-8") as archivo:
        for paciente in pacientes_data:
            archivo.write(
                f"{paciente['Nombre']}|{paciente['Fecha de Nacimiento']}|{paciente['Edad']}|"
                f"{paciente['Género']}|{paciente['Grupo Sanguíneo']}|"
                f"{paciente['Tipo de Seguro']}|{paciente['Centro Médico']}|{paciente['Estatura']}\n"
            )
 
# lista de pacientes
datos_columnas = ("Nombre", "FechaN", "Edad", "Género", "GrupoS", "TipoS", "CentroM", "Estatura")
pacientes_data = []
 
# funcion para registrar pacientes
 
def registrarPaciente():
    # crear un diccionario con los datos del paciente
    paciente = {
        "Nombre": nombreP.get(),
        "Fecha de Nacimiento": fechaN.get(),
        "Edad": edadVar.get(),
        "Género": genero.get(),
        "Grupo Sanguíneo": entryGrupoS.get(),
        "Tipo de Seguro": tipoSeguro.get(),
        "Centro Médico": centroM.get(),
        "Estatura": estaturaP.get(),
    }
    # agregar paciente a la lista
    pacientes_data.append(paciente)
    # guardar cambios en archivo
    guardar_en_archivo()
    # recargar tabla
    cargar_treeview()
 
 
def cargar_treeview():
    # limpiar el treeview
    for paciente in treeview.get_children():
        treeview.delete(paciente)
    # insertar cada paciente
    for i, item in enumerate(pacientes_data):
        treeview.insert(
            "", "end", iid=str(i),
            values=(
                item["Nombre"],
                item["Fecha de Nacimiento"],
                item["Edad"],
                item["Género"],
                item["Grupo Sanguíneo"],
                item["Tipo de Seguro"],
                item["Centro Médico"],
                item["Estatura"],
            )
        )
 
 
def cargar_desde_archivo_paciente():
    try:
        with open("pacienteEstatura.txt", "r", encoding="utf-8") as archivo:
            pacientes_data.clear()
            for linea in archivo:
                datos = linea.strip().split("|")
                if len(datos) == 8:
                    paciente = {
                        "Nombre": datos[0],
                        "Fecha de Nacimiento": datos[1],
                        "Edad": datos[2],
                        "Género": datos[3],
                        "Grupo Sanguíneo": datos[4],
                        "Tipo de Seguro": datos[5],
                        "Centro Médico": datos[6],
                        "Estatura": datos[7],
                    }
                    pacientes_data.append(paciente)
                elif len(datos) == 7:
                    # Compatibilidad con archivos sin estatura
                    paciente = {
                        "Nombre": datos[0],
                        "Fecha de Nacimiento": datos[1],
                        "Edad": datos[2],
                        "Género": datos[3],
                        "Grupo Sanguíneo": datos[4],
                        "Tipo de Seguro": datos[5],
                        "Centro Médico": datos[6],
                        "Estatura": "",
                    }
                    pacientes_data.append(paciente)
            cargar_treeview()
    except FileNotFoundError:
        open
 
 
def eliminar_paciente():
    seleccionado = treeview.selection()
    if seleccionado:
        indice = int(seleccionado[0])
        id_item = seleccionado[0]
        nombre = treeview.item(id_item, 'values')[0]
        if messagebox.askyesno("Eliminar paciente", f"¿Estás seguro de que deseas eliminar el paciente '{nombre}'?"):
            del pacientes_data[indice]
            guardar_en_archivo()  # guarda los cambios en el archivo
            cargar_treeview()
            messagebox.showinfo("Eliminar Paciente", "Paciente eliminado exitosamente")
    else:  # este else es del if seleccionado
        messagebox.showwarning("Eliminar Paciente", "No se ha seleccionado ningun paciente.")
        return
 
 
# Crear ventana principal
ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Libro de Pacientes")
ventanaPrincipal.geometry("950x600")
 
# Crear contenedor NoteBook (pestañas)
pestañas = ttk.Notebook(ventanaPrincipal)
 
# Frame de Pacientes
framePacientes = tk.Frame(pestañas)
 
# Agregar pestaña de Pacientes
pestañas.add(framePacientes, text="Pacientes")
 
# Mostrar las pestañas en la ventana
pestañas.pack(expand=True, fill="both")
 
# Nombre
labelNombre = tk.Label(framePacientes, text=" Nombre Completo:")
labelNombre.grid(row=0, column=0, padx=5, pady=5, sticky="w")
nombreP = tk.Entry(framePacientes)
nombreP.grid(row=0, column=1, padx=5, pady=5, sticky="w")
 
# Fecha de nacimiento
labelFechaN = tk.Label(framePacientes, text=" Fecha de Nacimiento:")
labelFechaN.grid(row=1, column=0, padx=5, pady=5, sticky="w")
validacion_fecha = ventanaPrincipal.register(enmascarar_fecha)
fechaN = ttk.Entry(framePacientes, validate="key", validatecommand=(validacion_fecha, '%P'))
fechaN.grid(row=1, column=1, padx=5, pady=5, sticky="w")
 
# Edad (readonly)
labelEdad = tk.Label(framePacientes, text=" Edad:")
labelEdad.grid(row=2, column=0, padx=5, pady=5, sticky="w")
edadVar = tk.StringVar()
edadP = tk.Entry(framePacientes, textvariable=edadVar, state="readonly")
edadP.grid(row=2, column=1, padx=5, pady=5, sticky="w")
 
# Género
labelGenero = tk.Label(framePacientes, text=" Género:")
labelGenero.grid(row=3, column=0, padx=5, pady=5, sticky="w")
genero = tk.StringVar()
genero.set("Masculino")  # Valor por defecto
radioMasculino = ttk.Radiobutton(framePacientes, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, padx=5, sticky="w")
radioFemenino = ttk.Radiobutton(framePacientes, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=4, column=1, padx=5, sticky="w")
 
# Grupo sanguíneo
labelGrupoS = tk.Label(framePacientes, text=" Grupo Sanguíneo:")
labelGrupoS.grid(row=5, column=0, padx=5, pady=5, sticky="w")
entryGrupoS = tk.Entry(framePacientes)
entryGrupoS.grid(row=5, column=1, padx=5, pady=5, sticky="w")
 
# Tipo de seguro
labelTipoS = tk.Label(framePacientes, text=" Tipo de Seguro:")
labelTipoS.grid(row=6, column=0, padx=5, pady=5, sticky="w")
tipoSeguro = tk.StringVar()
tipoSeguro.set("Público")  # Valor por defecto
comboTipoS = ttk.Combobox(framePacientes, values=["Público", "Privado", "Ninguno"], textvariable=tipoSeguro)
comboTipoS.grid(row=6, column=1, padx=5, pady=5, sticky="w")
 
# Tipo de centro médico
labelCentroM = tk.Label(framePacientes, text=" Centro Médico:")
labelCentroM.grid(row=7, column=0, padx=5, pady=5, sticky="w")
centroM = tk.StringVar()
centroM.set("Hospital Central")  # Valor por defecto
comboCentroM = ttk.Combobox(framePacientes, values=["Hospital Central", "Clínica Norte", "Centro Salud Sur"], textvariable=centroM)
comboCentroM.grid(row=7, column=1, padx=5, pady=5, sticky="w")
 
# Estatura (nuevo campo)
labelEstatura = tk.Label(framePacientes, text=" Estatura (cm):")
labelEstatura.grid(row=8, column=0, padx=5, pady=5, sticky="w")
estaturaP = tk.Entry(framePacientes)
estaturaP.grid(row=8, column=1, padx=5, pady=5, sticky="w")
 
# Frame para los botones
btnFrame = tk.Frame(framePacientes)
btnFrame.grid(row=9, column=1, columnspan=2, pady=5, sticky="w")
 
# Botón Registrar
btnRegistrar = tk.Button(btnFrame, text="Registrar", command=registrarPaciente)
btnRegistrar.grid(row=0, column=0, padx=5)
 
# Botón Eliminar
btnEliminar = tk.Button(btnFrame, text="Eliminar", command=eliminar_paciente)
btnEliminar.grid(row=0, column=1, padx=5)
 
# Crear Treeview para mostrar los pacientes
treeview = ttk.Treeview(framePacientes, columns=datos_columnas, show="headings")
 
# Definir encabezados
treeview.heading("Nombre", text="Nombre")
treeview.heading("FechaN", text="Fecha de Nacimiento")
treeview.heading("Edad", text="Edad")
treeview.heading("Género", text="Género")
treeview.heading("GrupoS", text="Grupo Sanguíneo")
treeview.heading("TipoS", text="Tipo de Seguro")
treeview.heading("CentroM", text="Centro Médico")
treeview.heading("Estatura", text="Estatura (cm)")
 
# definir ancho de columnas
treeview.column("Nombre", width=200)
treeview.column("FechaN", width=120)
treeview.column("Edad", width=50)
treeview.column("Género", width=100)
treeview.column("GrupoS", width=120)
treeview.column("TipoS", width=120)
treeview.column("CentroM", width=150)
treeview.column("Estatura", width=100)
 
# ubicar el treeview en la cuadrícula
treeview.grid(row=10, column=0, columnspan=4, padx=5, pady=5)
 
# Scrollbar vertical
scrollbar = ttk.Scrollbar(framePacientes, orient="vertical", command=treeview.yview)
treeview.configure(yscroll=scrollbar.set)
scrollbar.grid(row=10, column=4, sticky="ns")
 
# Carga inicial de datos
cargar_desde_archivo_paciente()  # carga datos desde archivo al iniciar la aplicación
 
ventanaPrincipal.mainloop()
 
 