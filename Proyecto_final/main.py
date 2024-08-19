import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
from conexion import *
from menu1 import *
from menu2 import *
from menu3 import *
from usuario import *
import getpass
from clases import *
from clases2 import *
from clases3 import *

from conexion import *
class GanadoMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Administración")
        self.geometry("1360x768")
        self.configure(bg="#ffffff")
        self.menu1()

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestión de Rancho")
        self.geometry("1360x768")
        self.resizable(False, False)
        self.config(bg="#ffffff")  # Fondo blanco para un diseño más limpio

        # Definición de fuentes y colores
        self.font_title = tkfont.Font(family="Helvetica", size=28, weight="bold")
        self.font_buttons = tkfont.Font(family="Helvetica", size=16, weight="bold")
        self.bg_color = "#4a90e2"  # Color azul para el fondo de los botones
        self.fg_color = "#ffffff"  # Color blanco para el texto de los botones

        # Crea un frame para el menú principal
        self.frame_menu_principal = tk.Frame(self, bg="#ffffff")
        self.frame_menu_principal.pack(fill="both", expand=True)

        # Crea un label para el título del menú principal
        self.label_titulo = tk.Label(self.frame_menu_principal, text="Menú Principal", font=self.font_title, bg="#ffffff", fg=self.bg_color)
        self.label_titulo.pack(pady=20)

        # Crea un frame para las opciones del menú principal
        self.frame_opciones = tk.Frame(self.frame_menu_principal, bg="#ffffff")
        self.frame_opciones.pack(fill="both", expand=True)

        # Define el estilo de los botones
        self.style_button = {
            "bg": self.bg_color,
            "fg": self.fg_color,
            "font": self.font_buttons,
            "bd": 0,
            "highlightthickness": 0,
            "relief": "flat",
            "padx": 20,
            "pady": 10
        }

        # Crea botones para las opciones del menú principal
        self.boton_gestionar_animales = tk.Button(self.frame_opciones, text="Gestionar animales", command=self.menu1, **self.style_button)
        self.boton_gestionar_animales.pack(fill="x", pady=10)

        self.boton_gestionar_empleados = tk.Button(self.frame_opciones, text="Gestionar empleados", command=self.menu2, **self.style_button)
        self.boton_gestionar_empleados.pack(fill="x", pady=10)

        self.boton_gestionar_instalaciones = tk.Button(self.frame_opciones, text="Gestionar instalaciones", command=self.menu3, **self.style_button)
        self.boton_gestionar_instalaciones.pack(fill="x", pady=10)

        self.boton_gestionar_actividades = tk.Button(self.frame_opciones, text="Gestionar actividades", command=self.menu4, **self.style_button)
        self.boton_gestionar_actividades.pack(fill="x", pady=10)

        self.boton_gestionar_inventario = tk.Button(self.frame_opciones, text="Gestionar inventario", command=self.menu5, **self.style_button)
        self.boton_gestionar_inventario.pack(fill="x", pady=10)

        self.boton_informacion_rancho = tk.Button(self.frame_opciones, text="Información del rancho", command=self.menu6, **self.style_button)
        self.boton_informacion_rancho.pack(fill="x", pady=10)

        self.boton_registro_vacunas = tk.Button(self.frame_opciones, text="Registro de vacunas", command=self.menu7, **self.style_button)
        self.boton_registro_vacunas.pack(fill="x", pady=10)

        self.boton_salir = tk.Button(self.frame_opciones, text="Salir del sistema", command=self.salir, **self.style_button)
        self.boton_salir.pack(fill="x", pady=10)

    def menu1(self):
        # Crea una nueva ventana para el menú de administración de ganado
        self.ventana_ganado = tk.Toplevel(self)
        self.ventana_ganado.title("Menú de Administración de Ganado")
        self.ventana_ganado.geometry("1360x768")
        self.ventana_ganado.resizable(False, False)
        self.ventana_ganado.config(bg="#ffffff")

        # Definición de fuentes y colores para el menú de ganado
        font_title = tkfont.Font(family="Helvetica", size=24, weight="bold")
        font_buttons = tkfont.Font(family="Helvetica", size=16, weight="bold")
        bg_title = "#007bff"
        fg_title = "#ffffff"
        button_bg = "#4CAF50"
        button_fg = "#ffffff"

        # Crea un frame para el título del menú de administración de ganado
        self.frame_titulo_ganado = tk.Frame(self.ventana_ganado, bg=bg_title)
        self.frame_titulo_ganado.pack(fill="x")

        self.label_titulo_ganado = tk.Label(self.frame_titulo_ganado, text="Menú de Administración de Ganado", font=font_title, bg=bg_title, fg=fg_title)
        self.label_titulo_ganado.pack(pady=20)

        # Crea un frame para las opciones del menú de administración de ganado
        self.frame_opciones_ganado = tk.Frame(self.ventana_ganado, bg="#f0f0f0")
        self.frame_opciones_ganado.pack(fill="both", expand=True)

        # Define el estilo de los botones del menú de ganado
        style_button_ganado = {
            "bg": button_bg,
            "fg": button_fg,
            "font": font_buttons,
            "bd": 0,
            "highlightthickness": 0,
            "relief": "flat",
            "padx": 20,
            "pady": 10
        }

        # Crea botones para las opciones del menú de administración de ganado
        self.boton_anadir_animal = tk.Button(self.frame_opciones_ganado, text="Añadir un animal", command=self.anadir_animal, **style_button_ganado)
        self.boton_anadir_animal.pack(fill="x", pady=10)

        self.boton_actualizar_animal = tk.Button(self.frame_opciones_ganado, text="Actualizar información de un animal", command=self.actualizar_animal, **style_button_ganado)
        self.boton_actualizar_animal.pack(fill="x", pady=10)

        self.boton_ver_todos_los_animales = tk.Button(self.frame_opciones_ganado, text="Ver información de todos los animales", command=self.ver_todos_los_animales, **style_button_ganado)
        self.boton_ver_todos_los_animales.pack(fill="x", pady=10)

        self.boton_ver_un_animal = tk.Button(self.frame_opciones_ganado, text="Ver información de un animal", command=self.ver_un_animal, **style_button_ganado)
        self.boton_ver_un_animal.pack(fill="x", pady=10)

        self.boton_eliminar_animal = tk.Button(self.frame_opciones_ganado, text="Eliminar animal de los registros", command=self.eliminar_animal, **style_button_ganado)
        self.boton_eliminar_animal.pack(fill="x", pady=10)

        self.boton_salir = tk.Button(self.frame_opciones_ganado, text="Salir", command=self.salir_menu_ganado, bg="#007bff", fg="#ffffff", font=font_buttons, bd=0, highlightthickness=0, relief="flat", padx=20, pady=10)
        self.boton_salir.pack(fill="x", pady=10)

    def anadir_animal(self):
        # Crea una nueva ventana para el formulario de añadir un animal
        self.ventana_anadir_animal = tk.Toplevel(self.ventana_ganado)
        self.ventana_anadir_animal.title("Añadir un Animal")
        self.ventana_anadir_animal.geometry("400x400")

        # Labels y entradas para capturar los datos del animal
        tk.Label(self.ventana_anadir_animal, text="Especie del animal:").grid(row=0, column=0, pady=10, padx=10, sticky="w")
        self.especie_entry = tk.Entry(self.ventana_anadir_animal)
        self.especie_entry.grid(row=0, column=1, pady=10, padx=10)

        tk.Label(self.ventana_anadir_animal, text="Raza del animal:").grid(row=1, column=0, pady=10, padx=10, sticky="w")
        self.raza_entry = tk.Entry(self.ventana_anadir_animal)
        self.raza_entry.grid(row=1, column=1, pady=10, padx=10)

        tk.Label(self.ventana_anadir_animal, text="Sexo del animal (M/F):").grid(row=2, column=0, pady=10, padx=10, sticky="w")
        self.sexo_entry = tk.Entry(self.ventana_anadir_animal)
        self.sexo_entry.grid(row=2, column=1, pady=10, padx=10)

        tk.Label(self.ventana_anadir_animal, text="Fecha de nacimiento (YYYY-MM-DD):").grid(row=3, column=0, pady=10, padx=10, sticky="w")
        self.edad_entry = tk.Entry(self.ventana_anadir_animal)
        self.edad_entry.grid(row=3, column=1, pady=10, padx=10)

        tk.Label(self.ventana_anadir_animal, text="Peso del animal:").grid(row=4, column=0, pady=10, padx=10, sticky="w")
        self.peso_entry = tk.Entry(self.ventana_anadir_animal)
        self.peso_entry.grid(row=4, column=1, pady=10, padx=10)

        tk.Label(self.ventana_anadir_animal, text="Salud del animal (Saludable/Enfermo):").grid(row=5, column=0, pady=10, padx=10, sticky="w")
        self.salud_entry = tk.Entry(self.ventana_anadir_animal)
        self.salud_entry.grid(row=5, column=1, pady=10, padx=10)

        tk.Label(self.ventana_anadir_animal, text="Destino productivo:").grid(row=6, column=0, pady=10, padx=10, sticky="w")
        self.destino_entry = tk.Entry(self.ventana_anadir_animal)
        self.destino_entry.grid(row=6, column=1, pady=10, padx=10)

        tk.Label(self.ventana_anadir_animal, text="ID de la instalación:").grid(row=7, column=0, pady=10, padx=10, sticky="w")
        self.ubicacion_entry = tk.Entry(self.ventana_anadir_animal)
        self.ubicacion_entry.grid(row=7, column=1, pady=10, padx=10)

        # Botón para guardar el animal en la base de datos
        self.boton_guardar_animal = tk.Button(self.ventana_anadir_animal, text="Añadir Animal", command=self.guardar_animal)
        self.boton_guardar_animal.grid(row=8, column=0, columnspan=2, pady=20)

    def guardar_animal(self): #se modifico apartir de aqui
        especie = self.especie_entry.get().strip()
        raza = self.raza_entry.get().strip()
        sexo = self.sexo_entry.get().strip().upper()
        edad = self.edad_entry.get().strip()
        peso = float(self.peso_entry.get().strip())
        salud = self.salud_entry.get().strip()
        destino = self.destino_entry.get().strip()
        ubicacion = int(self.ubicacion_entry.get().strip())
        estatus = 1

    # Crear una instancia de Ganado con los datos del formulario
        nuevo_animal = Ganado(especie, raza, sexo, edad, peso, salud, destino, ubicacion, estatus)

    # Añadir el animal a la base de datos usando el método de la clase Ganado
        nuevo_animal.añadir()

    # Limpiar los campos del formulario
        self.especie_entry.delete(0, tk.END)
        self.raza_entry.delete(0, tk.END)
        self.sexo_entry.delete(0, tk.END)
        self.edad_entry.delete(0, tk.END)
        self.peso_entry.delete(0, tk.END)
        self.salud_entry.delete(0, tk.END)
        self.destino_entry.delete(0, tk.END)
        self.ubicacion_entry.delete(0, tk.END)

    def actualizar_animal(self):
        # Crea una nueva ventana para el formulario de actualización de un animal
        self.ventana_actualizar_animal = tk.Toplevel(self.ventana_ganado)
        self.ventana_actualizar_animal.title("Actualizar Animal")
        self.ventana_actualizar_animal.geometry("400x400")

        tk.Label(self.ventana_actualizar_animal, text="ID del animal a actualizar:").grid(row=0, column=0, pady=10, padx=10, sticky="w")
        self.id_entry = tk.Entry(self.ventana_actualizar_animal)
        self.id_entry.grid(row=0, column=1, pady=10, padx=10)

        tk.Label(self.ventana_actualizar_animal, text="Especie del animal:").grid(row=1, column=0, pady=10, padx=10, sticky="w")
        self.especie_entry = tk.Entry(self.ventana_actualizar_animal)
        self.especie_entry.grid(row=1, column=1, pady=10, padx=10)

        tk.Label(self.ventana_actualizar_animal, text="Raza del animal:").grid(row=2, column=0, pady=10, padx=10, sticky="w")
        self.raza_entry = tk.Entry(self.ventana_actualizar_animal)
        self.raza_entry.grid(row=2, column=1, pady=10, padx=10)

        tk.Label(self.ventana_actualizar_animal, text="Sexo del animal (M/F):").grid(row=3, column=0, pady=10, padx=10, sticky="w")
        self.sexo_entry = tk.Entry(self.ventana_actualizar_animal)
        self.sexo_entry.grid(row=3, column=1, pady=10, padx=10)

        tk.Label(self.ventana_actualizar_animal, text="Fecha de nacimiento (YYYY-MM-DD):").grid(row=4, column=0, pady=10, padx=10, sticky="w")
        self.edad_entry = tk.Entry(self.ventana_actualizar_animal)
        self.edad_entry.grid(row=4, column=1, pady=10, padx=10)

        tk.Label(self.ventana_actualizar_animal, text="Peso del animal:").grid(row=5, column=0, pady=10, padx=10, sticky="w")
        self.peso_entry = tk.Entry(self.ventana_actualizar_animal)
        self.peso_entry.grid(row=5, column=1, pady=10, padx=10)

        tk.Label(self.ventana_actualizar_animal, text="Salud del animal (Saludable/Enfermo):").grid(row=6, column=0, pady=10, padx=10, sticky="w")
        self.salud_entry = tk.Entry(self.ventana_actualizar_animal)
        self.salud_entry.grid(row=6, column=1, pady=10, padx=10)

        tk.Label(self.ventana_actualizar_animal, text="Destino productivo:").grid(row=7, column=0, pady=10, padx=10, sticky="w")
        self.destino_entry = tk.Entry(self.ventana_actualizar_animal)
        self.destino_entry.grid(row=7, column=1, pady=10, padx=10)

        tk.Label(self.ventana_actualizar_animal, text="ID de la instalación:").grid(row=8, column=0, pady=10, padx=10, sticky="w")
        self.ubicacion_entry = tk.Entry(self.ventana_actualizar_animal)
        self.ubicacion_entry.grid(row=8, column=1, pady=10, padx=10)

        tk.Label(self.ventana_actualizar_animal, text="Estatus (1 para activo, 0 para inactivo):").grid(row=9, column=0, pady=10, padx=10, sticky="w")
        self.estatus_entry = tk.Entry(self.ventana_actualizar_animal)
        self.estatus_entry.grid(row=9, column=1, pady=10, padx=10)

        self.boton_guardar_actualizacion = tk.Button(self.ventana_actualizar_animal, text="Actualizar Animal", command=self.guardar_actualizacion)
        self.boton_guardar_actualizacion.grid(row=10, column=0, columnspan=2, pady=20)

    def guardar_actualizacion(self):
        id_ganado = int(self.id_entry.get().strip())
        especie = self.especie_entry.get().strip()
        raza = self.raza_entry.get().strip()
        sexo = self.sexo_entry.get().strip().upper()
        edad = self.edad_entry.get().strip()
        peso = float(self.peso_entry.get().strip())
        salud = self.salud_entry.get().strip()
        destino = self.destino_entry.get().strip()
        ubicacion = self.ubicacion_entry.get().strip()
        estatus = self.estatus_entry.get().strip()

        Ganado.actualizar(id_ganado, especie, raza, sexo, edad, peso, salud, destino, ubicacion, estatus)

        self.id_entry.delete(0, tk.END)
        self.especie_entry.delete(0, tk.END)
        self.raza_entry.delete(0, tk.END)
        self.sexo_entry.delete(0, tk.END)
        self.edad_entry.delete(0, tk.END)
        self.peso_entry.delete(0, tk.END)
        self.salud_entry.delete(0, tk.END)
        self.destino_entry.delete(0, tk.END)
        self.ubicacion_entry.delete(0, tk.END)
        self.estatus_entry.delete(0, tk.END)

    def ver_todos_los_animales(self):
        # Crea una nueva ventana para mostrar la información de todos los animales
        self.ventana_ver_todos = tk.Toplevel(self.ventana_ganado)
        self.ventana_ver_todos.title("Ver Todos los Animales")
        self.ventana_ver_todos.geometry("800x600")

        self.text_area = tk.Text(self.ventana_ver_todos)
        self.text_area.pack(fill="both", expand=True)

        # Obtener y mostrar la información
        animales = Ganado.leer_todo()
        for animal in animales:
            self.text_area.insert(tk.END, f"id: {animal[0]}, especie: {animal[1]}, raza: {animal[2]}, sexo: {animal[3]}, edad: {animal[4]}, peso: {animal[5]}, salud: {animal[6]}, destino: {animal[7]}, ubicacion: {animal[8]}, estatus: {animal[9]}\n")
  
    def ver_un_animal(self):
        # Crea una nueva ventana para el formulario de búsqueda de un animal
        self.ventana_ver_uno = tk.Toplevel(self.ventana_ganado)
        self.ventana_ver_uno.title("Ver Un Animal")
        self.ventana_ver_uno.geometry("400x200")

        tk.Label(self.ventana_ver_uno, text="ID del animal a inspeccionar:").grid(row=0, column=0, pady=10, padx=10, sticky="w")
        self.id_un_animal_entry = tk.Entry(self.ventana_ver_uno)
        self.id_un_animal_entry.grid(row=0, column=1, pady=10, padx=10)

        self.boton_ver_un_animal = tk.Button(self.ventana_ver_uno, text="Ver Animal", command=self.mostrar_animal)
        self.boton_ver_un_animal.grid(row=1, column=0, columnspan=2, pady=20)

        self.text_area_un_animal = tk.Text(self.ventana_ver_uno, height=8, width=50)
        self.text_area_un_animal.grid(row=2, column=0, columnspan=2)

    def mostrar_animal(self):
        id_ganado_str = self.id_un_animal_entry.get().strip()
        try:
            id_ganado = int(id_ganado_str)
        except ValueError:
            self.text_area_un_animal.delete(1.0, tk.END)
            self.text_area_un_animal.insert(tk.END, "Por favor, ingresa un ID válido (entero).\n")
            return
        
        # Llamar al método para leer el animal con el ID entero
        animal = Ganado.leer_uno(id_ganado)

        # Verificar si el animal existe
        if animal:
            self.text_area_un_animal.delete(1.0, tk.END)
            self.text_area_un_animal.insert(tk.END, f"id: {animal[0]}, especie: {animal[1]}, raza: {animal[2]}, sexo: {animal[3]}, edad: {animal[4]}, peso: {animal[5]}, salud: {animal[6]}, destino: {animal[7]}, ubicacion: {animal[8]}, estatus: {animal[9]}\n")
        else:
            self.text_area_un_animal.delete(1.0, tk.END)
            self.text_area_un_animal.insert(tk.END, "Animal no encontrado.\n")
    
    
        animal = Ganado.leer_uno(id_ganado)

        # Verificar si el animal existe
        if animal:
            self.text_area_un_animal.delete(1.0, tk.END)
            self.text_area_un_animal.insert(tk.END, f"id: {animal[0]}, especie: {animal[1]}, raza: {animal[2]}, sexo: {animal[3]}, edad: {animal[4]}, peso: {animal[5]}, salud: {animal[6]}, destino: {animal[7]}, ubicacion: {animal[8]}, estatus: {animal[9]}\n")
        else:
            self.text_area_un_animal.delete(1.0, tk.END)
            self.text_area_un_animal.insert(tk.END, "Animal no encontrado.\n")

    def eliminar_animal(self): #se modifico esto
        self.ventana_eliminar_animal = tk.Toplevel(self.ventana_ganado)
        self.ventana_eliminar_animal.title("Eliminar Animal")
        self.ventana_eliminar_animal.geometry("400x200")

        tk.Label(self.ventana_eliminar_animal, text="ID del animal a dar de baja:").grid(row=0, column=0, pady=10, padx=10, sticky="w")
        self.id_eliminar_entry = tk.Entry(self.ventana_eliminar_animal)
        self.id_eliminar_entry.grid(row=0, column=1, pady=10, padx=10)

        self.boton_eliminar = tk.Button(self.ventana_eliminar_animal, text="Eliminar Animal", command=self.eliminar)
        self.boton_eliminar.grid(row=1, column=0, columnspan=2, pady=20)

    def eliminar(self):
        id_ganado = self.id_eliminar_entry.get().strip()
        if Ganado.eliminar(id_ganado):
            messagebox.showinfo("Éxito", "Animal eliminado con éxito.")
        else:
            messagebox.showerror("Error", "No se pudo eliminar el animal.")
        
        self.id_eliminar_entry.delete(0, tk.END)

    def salir_menu_ganado(self):
        self.ventana_ganado.destroy()

    def salir(self):
        self.quit()

    def menu2(self):
        # Método para el menú de administración de empleados
        self.ventana_empleados = tk.Toplevel(self)
        self.ventana_empleados.title("Menú de Administración de Empleados")
        self.ventana_empleados.geometry("1360x768")
        self.ventana_empleados.resizable(False, False)
        self.ventana_empleados.config(bg="#ffffff")  # Fondo blanco para el diseño

        # Definición de fuentes y colores para el menú de empleados
        font_title = tkfont.Font(family="Helvetica", size=24, weight="bold")
        font_buttons = tkfont.Font(family="Helvetica", size=16, weight="bold")
        bg_title = "#007bff"  # Azul para el fondo del título
        fg_title = "#ffffff"  # Blanco para el texto del título
        button_bg = "#4CAF50"  # Verde para el fondo de los botones
        button_fg = "#ffffff"  # Blanco para el texto de los botones

        # Crea un frame para el título del menú de administración de empleados
        self.frame_titulo_empleados = tk.Frame(self.ventana_empleados, bg=bg_title)
        self.frame_titulo_empleados.pack(fill="x")

        self.label_titulo_empleados = tk.Label(self.frame_titulo_empleados, text="Menú de Administración de Empleados", font=font_title, bg=bg_title, fg=fg_title)
        self.label_titulo_empleados.pack(pady=20)

        # Crea un frame para las opciones del menú de administración de empleados
        self.frame_opciones_empleados = tk.Frame(self.ventana_empleados, bg="#f0f0f0")
        self.frame_opciones_empleados.pack(fill="both", expand=True)

        # Define el estilo de los botones del menú de empleados
        style_button_empleados = {
            "bg": button_bg,
            "fg": button_fg,
            "font": font_buttons,
            "bd": 0,
            "highlightthickness": 0,
            "relief": "flat",
            "padx": 20,
            "pady": 10
        }

        # Crea botones para las opciones del menú de administración de empleados
        self.boton_anadir_empleado = tk.Button(self.frame_opciones_empleados, text="Añadir un empleado", command=self.registrar_empleado, **style_button_empleados)
        self.boton_anadir_empleado.pack(fill="x", pady=10)

        self.boton_actualizar_empleado = tk.Button(self.frame_opciones_empleados, text="Actualizar información de un empleado", command=self.actualizar_empleado, **style_button_empleados)
        self.boton_actualizar_empleado.pack(fill="x", pady=10)

        self.boton_ver_todos_los_empleados = tk.Button(self.frame_opciones_empleados, text="Ver información de todos los empleados", command=self.ver_todos_los_empleados, **style_button_empleados)
        self.boton_ver_todos_los_empleados.pack(fill="x", pady=10)

        self.boton_ver_un_empleado = tk.Button(self.frame_opciones_empleados, text="Ver información de un empleado", command=self.ver_un_empleado, **style_button_empleados)
        self.boton_ver_un_empleado.pack(fill="x", pady=10)

        self.boton_dar_baja_empleado = tk.Button(self.frame_opciones_empleados, text="Dar de baja a un empleado", command=self.dar_baja_empleado, **style_button_empleados)
        self.boton_dar_baja_empleado.pack(fill="x", pady=10)

        self.boton_salir_empleados = tk.Button(self.frame_opciones_empleados, text="Salir", command=self.salir_menu_empleados, bg="#007bff", fg="#ffffff", font=font_buttons, bd=0, highlightthickness=0, relief="flat", padx=20, pady=10)
        self.boton_salir_empleados.pack(fill="x", pady=10)

    def registrar_empleado(self):
        self.ventana_anadir_empleado = tk.Toplevel(self)
        self.ventana_anadir_empleado.title("Añadir un nuevo empleado")
        
        # Campos de entrada
        tk.Label(self.ventana_anadir_empleado, text="Nombre:").grid(row=0, column=0, pady=10, padx=10, sticky="w")
        self.nombre_entry = tk.Entry(self.ventana_anadir_empleado)
        self.nombre_entry.grid(row=0, column=1, pady=10, padx=10)

        tk.Label(self.ventana_anadir_empleado, text="Apellido paterno:").grid(row=1, column=0, pady=10, padx=10, sticky="w")
        self.apellido_p_entry = tk.Entry(self.ventana_anadir_empleado)
        self.apellido_p_entry.grid(row=1, column=1, pady=10, padx=10)

        tk.Label(self.ventana_anadir_empleado, text="Apellido materno:").grid(row=2, column=0, pady=10, padx=10, sticky="w")
        self.apellido_m_entry = tk.Entry(self.ventana_anadir_empleado)
        self.apellido_m_entry.grid(row=2, column=1, pady=10, padx=10)

        tk.Label(self.ventana_anadir_empleado, text="CURP:").grid(row=3, column=0, pady=10, padx=10, sticky="w")
        self.curp_entry = tk.Entry(self.ventana_anadir_empleado)
        self.curp_entry.grid(row=3, column=1, pady=10, padx=10)

        tk.Label(self.ventana_anadir_empleado, text="Fecha de nacimiento (YYYY-MM-DD):").grid(row=4, column=0, pady=10, padx=10, sticky="w")
        self.fecha_nac_entry = tk.Entry(self.ventana_anadir_empleado)
        self.fecha_nac_entry.grid(row=4, column=1, pady=10, padx=10)

        tk.Label(self.ventana_anadir_empleado, text="Rol:").grid(row=5, column=0, pady=10, padx=10, sticky="w")
        self.rol_entry = tk.Entry(self.ventana_anadir_empleado)
        self.rol_entry.grid(row=5, column=1, pady=10, padx=10)

        tk.Label(self.ventana_anadir_empleado, text="Salario:").grid(row=6, column=0, pady=10, padx=10, sticky="w")
        self.salario_entry = tk.Entry(self.ventana_anadir_empleado)
        self.salario_entry.grid(row=6, column=1, pady=10, padx=10)

        tk.Label(self.ventana_anadir_empleado, text="ID del rancho:").grid(row=7, column=0, pady=10, padx=10, sticky="w")
        self.ranchoID_entry = tk.Entry(self.ventana_anadir_empleado)
        self.ranchoID_entry.grid(row=7, column=1, pady=10, padx=10)

        # Botón para guardar el empleado en la base de datos
        self.boton_guardar_empleado = tk.Button(self.ventana_anadir_empleado, text="Añadir Empleado", command=self.guardar_empleado)
        self.boton_guardar_empleado.grid(row=8, column=0, columnspan=2, pady=20)
        
    def guardar_empleado(self):
        try:
            # Aquí iría el código para guardar los datos del empleado en la base de datos
            nombre = self.nombre_entry.get()
            apellido_p = self.apellido_p_entry.get()
            apellido_m = self.apellido_m_entry.get()
            curp = self.curp_entry.get()
            fecha_nac = self.fecha_nac_entry.get()
            rol = self.rol_entry.get()
            salario = self.salario_entry.get()
            ranchoID = self.ranchoID_entry.get()

            # Implementa la lógica para guardar en la base de datos
            # ...

            tk.messagebox.showinfo("Éxito", "Empleado añadido correctamente.")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Ha ocurrido un error: {e}")


    def actualizar_empleado(self):
        # Crea una nueva ventana para el formulario de actualización de empleado
        self.ventana_actualizar_empleado = tk.Toplevel(self)
        self.ventana_actualizar_empleado.title("Actualizar Información de un Empleado")

        # Campo de entrada para ID del empleado
        tk.Label(self.ventana_actualizar_empleado, text="ID del empleado:").grid(row=0, column=0, pady=10, padx=10, sticky="w")
        self.id_empleado_entry = tk.Entry(self.ventana_actualizar_empleado)
        self.id_empleado_entry.grid(row=0, column=1, pady=10, padx=10)

        # Campos de entrada para los datos del empleado
        tk.Label(self.ventana_actualizar_empleado, text="Nuevo nombre (deja en blanco para no cambiar):").grid(row=1, column=0, pady=10, padx=10, sticky="w")
        self.nombre_entry = tk.Entry(self.ventana_actualizar_empleado)
        self.nombre_entry.grid(row=1, column=1, pady=10, padx=10)

        tk.Label(self.ventana_actualizar_empleado, text="Nuevo apellido paterno (deja en blanco para no cambiar):").grid(row=2, column=0, pady=10, padx=10, sticky="w")
        self.apellido_p_entry = tk.Entry(self.ventana_actualizar_empleado)
        self.apellido_p_entry.grid(row=2, column=1, pady=10, padx=10)

        tk.Label(self.ventana_actualizar_empleado, text="Nuevo apellido materno (deja en blanco para no cambiar):").grid(row=3, column=0, pady=10, padx=10, sticky="w")
        self.apellido_m_entry = tk.Entry(self.ventana_actualizar_empleado)
        self.apellido_m_entry.grid(row=3, column=1, pady=10, padx=10)

        tk.Label(self.ventana_actualizar_empleado, text="Nuevo CURP (deja en blanco para no cambiar):").grid(row=4, column=0, pady=10, padx=10, sticky="w")
        self.curp_entry = tk.Entry(self.ventana_actualizar_empleado)
        self.curp_entry.grid(row=4, column=1, pady=10, padx=10)

        tk.Label(self.ventana_actualizar_empleado, text="Nueva fecha de nacimiento (YYYY-MM-DD) (deja en blanco para no cambiar):").grid(row=5, column=0, pady=10, padx=10, sticky="w")
        self.fecha_nac_entry = tk.Entry(self.ventana_actualizar_empleado)
        self.fecha_nac_entry.grid(row=5, column=1, pady=10, padx=10)

        tk.Label(self.ventana_actualizar_empleado, text="Nuevo rol (deja en blanco para no cambiar):").grid(row=6, column=0, pady=10, padx=10, sticky="w")
        self.rol_entry = tk.Entry(self.ventana_actualizar_empleado)
        self.rol_entry.grid(row=6, column=1, pady=10, padx=10)

        tk.Label(self.ventana_actualizar_empleado, text="Nuevo salario (deja en blanco para no cambiar):").grid(row=7, column=0, pady=10, padx=10, sticky="w")
        self.salario_entry = tk.Entry(self.ventana_actualizar_empleado)
        self.salario_entry.grid(row=7, column=1, pady=10, padx=10)

        tk.Label(self.ventana_actualizar_empleado, text="Nuevo ID de rancho (deja en blanco para no cambiar):").grid(row=8, column=0, pady=10, padx=10, sticky="w")
        self.ranchoID_entry = tk.Entry(self.ventana_actualizar_empleado)
        self.ranchoID_entry.grid(row=8, column=1, pady=10, padx=10)

        tk.Label(self.ventana_actualizar_empleado, text="Nuevo estatus (1/0) (deja en blanco para no cambiar):").grid(row=9, column=0, pady=10, padx=10, sticky="w")
        self.estatus_entry = tk.Entry(self.ventana_actualizar_empleado)
        self.estatus_entry.grid(row=9, column=1, pady=10, padx=10)

        # Botón para guardar la actualización del empleado en la base de datos
        self.boton_guardar_actualizacion = tk.Button(self.ventana_actualizar_empleado, text="Actualizar Empleado", command=self.guardar_actualizacion_empleado)
        self.boton_guardar_actualizacion.grid(row=10, column=0, columnspan=2, pady=20)

    def guardar_actualizacion_empleado(self):
        id_empleado = self.id_empleado_entry.get().strip()
        nombre = self.nombre_entry.get().strip() or None
        apellido_p = self.apellido_p_entry.get().strip() or None
        apellido_m = self.apellido_m_entry.get().strip() or None
        curp = self.curp_entry.get().strip().upper() or None
        fecha_nac = self.fecha_nac_entry.get().strip() or None
        rol = self.rol_entry.get().strip() or None
        salario = self.salario_entry.get().strip()
        estatus = self.estatus_entry.get().strip()
        ranchoID = self.ranchoID_entry.get().strip()

        # Convertir valores a tipos adecuados
        salario = float(salario) if salario else None
        estatus = int(estatus) if estatus else None
        ranchoID = int(ranchoID) if ranchoID else None

        # Actualizar el empleado usando el método de la clase Empleado
        if id_empleado:
            Empleado.actualizar(id_empleado, nombre, apellido_p, apellido_m, curp, fecha_nac, rol, salario, estatus, ranchoID)

            # Limpiar los campos del formulario
            self.id_empleado_entry.delete(0, tk.END)
            self.nombre_entry.delete(0, tk.END)
            self.apellido_p_entry.delete(0, tk.END)
            self.apellido_m_entry.delete(0, tk.END)
            self.curp_entry.delete(0, tk.END)
            self.fecha_nac_entry.delete(0, tk.END)
            self.rol_entry.delete(0, tk.END)
            self.salario_entry.delete(0, tk.END)
            self.ranchoID_entry.delete(0, tk.END)
            self.estatus_entry.delete(0, tk.END)
        else:
            print("Error: Debes ingresar el ID del empleado.")


    def ver_todos_los_empleados(self):
        # Crear una nueva ventana para mostrar todos los empleados
        self.ventana_ver_todos_empleados = tk.Toplevel(self)
        self.ventana_ver_todos_empleados.title("Información de Todos los Empleados")
        self.ventana_ver_todos_empleados.geometry("1360x768")
        self.ventana_ver_todos_empleados.config(bg="#ffffff")

        # Definir una fuente para el texto
        font_text = tkfont.Font(family="Helvetica", size=12)

        # Crear un widget Text para mostrar los datos de todos los empleados
        self.text_empleados = tk.Text(self.ventana_ver_todos_empleados, wrap="word", font=font_text, bg="#f0f0f0")
        self.text_empleados.pack(fill="both", expand=True, padx=10, pady=10)

        # Cargar y mostrar los datos de todos los empleados
        try:
            empleados = Empleado.leer_todo()
            if empleados:
                for empleado in empleados:
                    self.text_empleados.insert(tk.END, f"id: {empleado[0]}, nombre: {empleado[1]}, apellido paterno: {empleado[2]}, apellido materno: {empleado[3]}, curp: {empleado[4]}, fecha nacimiento: {empleado[5]}, rol: {empleado[6]}, salario: {empleado[7]}, estatus: {empleado[8]}, ranchoID: {empleado[9]}\n")
            else:
                self.text_empleados.insert(tk.END, "No hay empleados activos en el sistema.\n")
        except Exception as e:
            self.text_empleados.insert(tk.END, f"Error al obtener la información de los empleados: {e}\n")

        # Agregar un botón para cerrar la ventana
        self.boton_cerrar = tk.Button(self.ventana_ver_todos_empleados, text="Cerrar", command=self.ventana_ver_todos_empleados.destroy, bg="#007bff", fg="#ffffff", font=font_text)
        self.boton_cerrar.pack(pady=10)

    
    def ver_un_empleado(self):
        # Crear una nueva ventana para mostrar la información del empleado específico
        self.ventana_ver_un_empleado = tk.Toplevel(self)
        self.ventana_ver_un_empleado.title("Información del Empleado")
        self.ventana_ver_un_empleado.geometry("1360x768")
        self.ventana_ver_un_empleado.config(bg="#ffffff")

        # Crear un marco para el formulario de búsqueda
        self.frame_busqueda = tk.Frame(self.ventana_ver_un_empleado, bg="#f0f0f0")
        self.frame_busqueda.pack(padx=10, pady=10)

        tk.Label(self.frame_busqueda, text="ID del empleado:", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.id_empleado_entry = tk.Entry(self.frame_busqueda)
        self.id_empleado_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.boton_buscar_empleado = tk.Button(self.frame_busqueda, text="Buscar", command=self.buscar_empleado)
        self.boton_buscar_empleado.grid(row=1, column=0, columnspan=2, pady=10)

        # Crear un widget Text para mostrar los datos del empleado
        self.text_empleado = tk.Text(self.ventana_ver_un_empleado, wrap="word", font=("Helvetica", 12), bg="#f0f0f0", height=20)
        self.text_empleado.pack(fill="both", expand=True, padx=10, pady=10)

        # Agregar un botón para cerrar la ventana
        self.boton_cerrar = tk.Button(self.ventana_ver_un_empleado, text="Cerrar", command=self.ventana_ver_un_empleado.destroy, bg="#007bff", fg="#ffffff", font=("Helvetica", 12))
        self.boton_cerrar.pack(pady=10)

    def buscar_empleado(self):
        # Obtener el ID del empleado del campo de entrada
        try:
            id_empleado = int(self.id_empleado_entry.get().strip())
            if id_empleado:
                # Llamar al método estático para obtener los datos del empleado
                resultado = Empleado.leer_uno(id_empleado)
                if resultado:
                    self.text_empleado.delete(1.0, tk.END)  # Limpiar el Text widget
                    self.text_empleado.insert(tk.END, f"id: {resultado[0]}, nombre: {resultado[1]}, apellido paterno: {resultado[2]}, apellido materno: {resultado[3]}, curp: {resultado[4]}, fecha nacimiento: {resultado[5]}, rol: {resultado[6]}, salario: {resultado[7]}, estatus: {resultado[8]}, ranchoID: {resultado[9]}\n")
                else:
                    self.text_empleado.delete(1.0, tk.END)  # Limpiar el Text widget
                    self.text_empleado.insert(tk.END, "No se encontró el empleado con el ID proporcionado.\n")
        except ValueError:
            self.text_empleado.delete(1.0, tk.END)
            self.text_empleado.insert(tk.END, "Error: ID inválido. Debes ingresar un número entero.\n")
        except Exception as e:
            self.text_empleado.delete(1.0, tk.END)
            self.text_empleado.insert(tk.END, f"Error al obtener la información del empleado: {e}\n")


    def dar_baja_empleado(self):
        # Crear una nueva ventana para dar de baja al empleado
        self.ventana_dar_baja_empleado = tk.Toplevel(self)
        self.ventana_dar_baja_empleado.title("Dar de Baja a un Empleado")
        self.ventana_dar_baja_empleado.geometry("400x200")
        self.ventana_dar_baja_empleado.config(bg="#ffffff")

        # Crear un marco para el formulario de baja
        self.frame_baja = tk.Frame(self.ventana_dar_baja_empleado, bg="#f0f0f0")
        self.frame_baja.pack(padx=10, pady=10, fill="both", expand=True)

        tk.Label(self.frame_baja, text="ID del empleado:", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.id_empleado_entry = tk.Entry(self.frame_baja)
        self.id_empleado_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.boton_dar_baja = tk.Button(self.frame_baja, text="Dar de Baja", command=self.dar_baja)
        self.boton_dar_baja.grid(row=1, column=0, columnspan=2, pady=10)

        # Crear un widget Text para mostrar el resultado de la operación
        self.text_resultado = tk.Text(self.ventana_dar_baja_empleado, wrap="word", font=("Helvetica", 12), bg="#f0f0f0", height=5)
        self.text_resultado.pack(fill="both", expand=True, padx=10, pady=10)

        # Agregar un botón para cerrar la ventana
        self.boton_cerrar = tk.Button(self.ventana_dar_baja_empleado, text="Cerrar", command=self.ventana_dar_baja_empleado.destroy, bg="#007bff", fg="#ffffff", font=("Helvetica", 12))
        self.boton_cerrar.pack(pady=10)

    def dar_baja(self):
        try:
            id_empleado = int(self.id_empleado_entry.get().strip())
            if id_empleado:
                Empleado.eliminar(id_empleado)
                self.text_resultado.delete(1.0, tk.END)  # Limpiar el Text widget
                self.text_resultado.insert(tk.END, "Empleado dado de baja con éxito.\n")
        except ValueError:
            self.text_resultado.delete(1.0, tk.END)
            self.text_resultado.insert(tk.END, "Error: ID inválido. Debes ingresar un número entero.\n")
        except Exception as e:
            self.text_resultado.delete(1.0, tk.END)
            self.text_resultado.insert(tk.END, f"Error al dar de baja al empleado: {e}\n")

           
    def salir_menu_empleados(self):
        self.ventana_empleados.destroy()

    def salir(self):
        self.destroy()


    def menu3(self):
        # Crear una ventana para el menú de administración de instalaciones
        self.ventana_instalaciones = tk.Toplevel(self)
        self.ventana_instalaciones.title("Menú de Administración de Instalaciones")
        self.ventana_instalaciones.geometry("1360x768")
        self.ventana_instalaciones.resizable(False, False)
        self.ventana_instalaciones.config(bg="#ffffff")

        # Crear el marco para el título
        self.frame_titulo = tk.Frame(self.ventana_instalaciones, bg="#007bff")
        self.frame_titulo.pack(fill="x")

        self.label_titulo = tk.Label(self.frame_titulo, text="Menú de Administración de Instalaciones", font=("Helvetica", 24, "bold"), bg="#007bff", fg="#ffffff")
        self.label_titulo.pack(pady=20)

        # Crear el marco para los botones del menú
        self.frame_botones = tk.Frame(self.ventana_instalaciones, bg="#f0f0f0")
        self.frame_botones.pack(fill="both", expand=True)

        # Crear los botones del menú
        self.boton_anadir = tk.Button(self.frame_botones, text="Añadir una instalación", command=self.anadir_instalacion, font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="#ffffff")
        self.boton_anadir.pack(fill="x", pady=10)

        self.boton_actualizar = tk.Button(self.frame_botones, text="Actualizar información de una instalación", command=self.actualizar_instalacion, font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="#ffffff")
        self.boton_actualizar.pack(fill="x", pady=10)

        self.boton_ver_todas = tk.Button(self.frame_botones, text="Ver información de todas las instalaciones", command=self.ver_todas_las_instalaciones, font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="#ffffff")
        self.boton_ver_todas.pack(fill="x", pady=10)

        self.boton_ver_una = tk.Button(self.frame_botones, text="Ver información de una instalación", command=self.ver_una_instalacion, font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="#ffffff")
        self.boton_ver_una.pack(fill="x", pady=10)

        self.boton_dar_baja = tk.Button(self.frame_botones, text="Dar de baja una instalación", command=self.dar_baja_instalacion, font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="#ffffff")
        self.boton_dar_baja.pack(fill="x", pady=10)

        self.boton_salir = tk.Button(self.frame_botones, text="Salir", command=self.salir_menu3, font=("Helvetica", 16, "bold"), bg="#007bff", fg="#ffffff")
        self.boton_salir.pack(fill="x", pady=10)

    def anadir_instalacion(self):
        # Implementar la lógica para añadir una instalación
        pass

    def actualizar_instalacion(self):
        # Implementar la lógica para actualizar la información de una instalación
        pass

    def ver_todas_las_instalaciones(self):
        # Implementar la lógica para ver toda la información de las instalaciones
        pass

    def ver_una_instalacion(self):
        # Implementar la lógica para ver la información de una instalación específica
        pass

    def dar_baja_instalacion(self):
        # Implementar la lógica para dar de baja una instalación
        pass

    def salir_menu3(self):
        # Cerrar la ventana del menú de administración de instalaciones
        self.ventana_instalaciones.destroy()


    def menu4(self):
        # Crear una ventana para el menú de administración de actividades
        self.ventana_actividades = tk.Toplevel(self)
        self.ventana_actividades.title("Menú de Administración de Actividades")
        self.ventana_actividades.geometry("1360x768")
        self.ventana_actividades.resizable(False, False)
        self.ventana_actividades.config(bg="#ffffff")

        # Crear el marco para el título
        self.frame_titulo = tk.Frame(self.ventana_actividades, bg="#007bff")
        self.frame_titulo.pack(fill="x")

        self.label_titulo = tk.Label(self.frame_titulo, text="Menú de Administración de Actividades", font=("Helvetica", 24, "bold"), bg="#007bff", fg="#ffffff")
        self.label_titulo.pack(pady=20)

        # Crear el marco para los botones del menú
        self.frame_botones = tk.Frame(self.ventana_actividades, bg="#f0f0f0")
        self.frame_botones.pack(fill="both", expand=True)

        # Crear los botones del menú
        self.boton_registrar = tk.Button(self.frame_botones, text="Registrar actividad", command=self.registrar_actividad, font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="#ffffff")
        self.boton_registrar.pack(fill="x", pady=10)

        self.boton_editar = tk.Button(self.frame_botones, text="Editar información de una actividad", command=self.editar_actividad, font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="#ffffff")
        self.boton_editar.pack(fill="x", pady=10)

        self.boton_ver_todos = tk.Button(self.frame_botones, text="Ver todos los registros", command=self.ver_todos_los_registros, font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="#ffffff")
        self.boton_ver_todos.pack(fill="x", pady=10)

        self.boton_ver_dia = tk.Button(self.frame_botones, text="Ver registros de un día", command=self.ver_registros_dia, font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="#ffffff")
        self.boton_ver_dia.pack(fill="x", pady=10)

        self.boton_salir = tk.Button(self.frame_botones, text="Salir", command=self.salir_menu4, font=("Helvetica", 16, "bold"), bg="#007bff", fg="#ffffff")
        self.boton_salir.pack(fill="x", pady=10)

    def registrar_actividad(self):
        # Implementar la lógica para registrar una actividad
        pass

    def editar_actividad(self):
        # Implementar la lógica para editar la información de una actividad
        pass

    def ver_todos_los_registros(self):
        # Implementar la lógica para ver todos los registros de actividades
        pass

    def ver_registros_dia(self):
        # Implementar la lógica para ver registros de actividades de un día específico
        pass

    def salir_menu4(self):
        # Cerrar la ventana del menú de administración de actividades
        self.ventana_actividades.destroy()


    def menu5(self):
        # Crear una ventana para el menú de administración de inventario
        self.ventana_inventario = tk.Toplevel(self)
        self.ventana_inventario.title("Menú de Administración de Inventario")
        self.ventana_inventario.geometry("1360x768")
        self.ventana_inventario.resizable(False, False)
        self.ventana_inventario.config(bg="#ffffff")

        # Crear el marco para el título
        self.frame_titulo = tk.Frame(self.ventana_inventario, bg="#007bff")
        self.frame_titulo.pack(fill="x")

        self.label_titulo = tk.Label(self.frame_titulo, text="Menú de Administración de Inventario", font=("Helvetica", 24, "bold"), bg="#007bff", fg="#ffffff")
        self.label_titulo.pack(pady=20)

        # Crear el marco para los botones del menú
        self.frame_botones = tk.Frame(self.ventana_inventario, bg="#f0f0f0")
        self.frame_botones.pack(fill="both", expand=True)

        # Crear los botones del menú
        self.boton_anadir = tk.Button(self.frame_botones, text="Añadir inventario", command=self.anadir_inventario, font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="#ffffff")
        self.boton_anadir.pack(fill="x", pady=10)

        self.boton_actualizar = tk.Button(self.frame_botones, text="Actualizar datos", command=self.actualizar_datos, font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="#ffffff")
        self.boton_actualizar.pack(fill="x", pady=10)

        self.boton_ver_todo = tk.Button(self.frame_botones, text="Ver todo el inventario", command=self.ver_todo_el_inventario, font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="#ffffff")
        self.boton_ver_todo.pack(fill="x", pady=10)

        self.boton_ver_producto = tk.Button(self.frame_botones, text="Ver producto específico", command=self.ver_producto_especifico, font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="#ffffff")
        self.boton_ver_producto.pack(fill="x", pady=10)

        self.boton_salir = tk.Button(self.frame_botones, text="Salir", command=self.salir_menu5, font=("Helvetica", 16, "bold"), bg="#007bff", fg="#ffffff")
        self.boton_salir.pack(fill="x", pady=10)

    def anadir_inventario(self):
        # Implementar la lógica para añadir inventario
        pass

    def actualizar_datos(self):
        # Implementar la lógica para actualizar los datos del inventario
        pass

    def ver_todo_el_inventario(self):
        # Implementar la lógica para ver todo el inventario
        pass

    def ver_producto_especifico(self):
        # Implementar la lógica para ver un producto específico
        pass

    def menu6(self):
        # Crear una ventana para el menú de administración del rancho
        self.ventana_rancho = tk.Toplevel(self)
        self.ventana_rancho.title("Menú de Administración del Rancho")
        self.ventana_rancho.geometry("1360x768")
        self.ventana_rancho.resizable(False, False)
        self.ventana_rancho.config(bg="#ffffff")

        # Crear el marco para el título
        self.frame_titulo = tk.Frame(self.ventana_rancho, bg="#007bff")
        self.frame_titulo.pack(fill="x")

        self.label_titulo = tk.Label(self.frame_titulo, text="Menú de Administración del Rancho", font=("Helvetica", 24, "bold"), bg="#007bff", fg="#ffffff")
        self.label_titulo.pack(pady=20)

        # Crear el marco para los botones del menú
        self.frame_botones = tk.Frame(self.ventana_rancho, bg="#f0f0f0")
        self.frame_botones.pack(fill="both", expand=True)

        # Crear los botones del menú
        self.boton_anadir = tk.Button(self.frame_botones, text="Añadir Rancho", command=self.anadir_rancho, font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="#ffffff")
        self.boton_anadir.pack(fill="x", pady=10)

        self.boton_actualizar = tk.Button(self.frame_botones, text="Actualizar datos del rancho", command=self.actualizar_datos_rancho, font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="#ffffff")
        self.boton_actualizar.pack(fill="x", pady=10)

        self.boton_ver_datos = tk.Button(self.frame_botones, text="Ver datos del rancho", command=self.ver_datos_rancho, font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="#ffffff")
        self.boton_ver_datos.pack(fill="x", pady=10)

        self.boton_salir = tk.Button(self.frame_botones, text="Salir", command=self.salir_menu7, font=("Helvetica", 16, "bold"), bg="#007bff", fg="#ffffff")
        self.boton_salir.pack(fill="x", pady=10)

    def anadir_rancho(self):
        # Implementar la lógica para añadir un rancho
        pass

    def actualizar_datos_rancho(self):
        # Implementar la lógica para actualizar los datos del rancho
        pass

    def ver_datos_rancho(self):
        # Implementar la lógica para ver los datos del rancho
        pass

    def salir_menu6(self):
        # Cerrar la ventana del menú de administración del rancho
        self.ventana_rancho.destroy()


    def menu7(self):
        # Crear una ventana para el menú de registro de vacunas
        self.ventana_vacunas = tk.Toplevel(self)
        self.ventana_vacunas.title("Menú de Registro de Vacunas")
        self.ventana_vacunas.geometry("1360x768")
        self.ventana_vacunas.resizable(False, False)
        self.ventana_vacunas.config(bg="#ffffff")

        # Crear el marco para el título
        self.frame_titulo = tk.Frame(self.ventana_vacunas, bg="#007bff")
        self.frame_titulo.pack(fill="x")

        self.label_titulo = tk.Label(self.frame_titulo, text="Menú de Registro de Vacunas", font=("Helvetica", 24, "bold"), bg="#007bff", fg="#ffffff")
        self.label_titulo.pack(pady=20)

        # Crear el marco para los botones del menú
        self.frame_botones = tk.Frame(self.ventana_vacunas, bg="#f0f0f0")
        self.frame_botones.pack(fill="both", expand=True)

        # Crear los botones del menú
        self.boton_anadir = tk.Button(self.frame_botones, text="Añadir registro", command=self.anadir_registro, font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="#ffffff")
        self.boton_anadir.pack(fill="x", pady=10)

        self.boton_modificar = tk.Button(self.frame_botones, text="Modificar registro", command=self.modificar_registro, font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="#ffffff")
        self.boton_modificar.pack(fill="x", pady=10)

        self.boton_ver_datos = tk.Button(self.frame_botones, text="Ver datos de registro", command=self.ver_datos_registro, font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="#ffffff")
        self.boton_ver_datos.pack(fill="x", pady=10)

        self.boton_ver_todo = tk.Button(self.frame_botones, text="Ver todos los registros", command=self.ver_todos_registros, font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="#ffffff")
        self.boton_ver_todo.pack(fill="x", pady=10)

        self.boton_salir = tk.Button(self.frame_botones, text="Salir", command=self.salir_menu8, font=("Helvetica", 16, "bold"), bg="#007bff", fg="#ffffff")
        self.boton_salir.pack(fill="x", pady=10)

    def anadir_registro(self):
        # Crea una nueva ventana para el formulario de añadir un registro de vacuna
        self.ventana_anadir_registro = tk.Toplevel(self.ventana_vacunas)
        self.ventana_anadir_registro.title("Añadir Registro de Vacuna")
        self.ventana_anadir_registro.geometry("400x300")

        # Labels y entradas para capturar los datos del registro de vacuna
        tk.Label(self.ventana_anadir_registro, text="ID del Animal:").grid(row=0, column=0, pady=10, padx=10, sticky="w")
        self.entry_animal = tk.Entry(self.ventana_anadir_registro)
        self.entry_animal.grid(row=0, column=1, pady=10, padx=10)

        tk.Label(self.ventana_anadir_registro, text="Responsable de la Vacunación:").grid(row=1, column=0, pady=10, padx=10, sticky="w")
        self.entry_responsable = tk.Entry(self.ventana_anadir_registro)
        self.entry_responsable.grid(row=1, column=1, pady=10, padx=10)

        tk.Label(self.ventana_anadir_registro, text="Observaciones:").grid(row=2, column=0, pady=10, padx=10, sticky="w")
        self.entry_observacion = tk.Entry(self.ventana_anadir_registro)
        self.entry_observacion.grid(row=2, column=1, pady=10, padx=10)

        tk.Label(self.ventana_anadir_registro, text="Fecha (YYYY-MM-DD):").grid(row=3, column=0, pady=10, padx=10, sticky="w")
        self.entry_fecha = tk.Entry(self.ventana_anadir_registro)
        self.entry_fecha.grid(row=3, column=1, pady=10, padx=10)

        # Botón para guardar el registro en la base de datos
        self.boton_guardar_registro = tk.Button(self.ventana_anadir_registro, text="Guardar Registro", command=self.guardar_registro)
        self.boton_guardar_registro.grid(row=4, column=0, columnspan=2, pady=20)

    def guardar_registro(self):
        try:
            animal = int(self.entry_animal.get().strip())
            responsable = self.entry_responsable.get().strip()
            observacion = self.entry_observacion.get().strip()
            fecha_admin = self.entry_fecha.get().strip()

            # Añadir el registro usando el método de la clase Registro
            Registro.añadir(animal, responsable, observacion, fecha_admin)

            # Limpiar los campos del formulario
            self.entry_animal.delete(0, tk.END)
            self.entry_responsable.delete(0, tk.END)
            self.entry_observacion.delete(0, tk.END)
            self.entry_fecha.delete(0, tk.END)

            # Cerrar la ventana después de guardar
            self.ventana_anadir_registro.destroy()

        except ValueError:
            tk.messagebox.showerror("Error", "El ID del animal debe ser un número entero.")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error al añadir el registro: {e}")

    def modificar_registro(self):
        # Crear una ventana para actualizar un registro de vacuna
        self.ventana_actualizar_registro = tk.Toplevel(self)
        self.ventana_actualizar_registro.title("Actualizar Registro de Vacuna")
        self.ventana_actualizar_registro.geometry("400x400")

        # Campo para el ID del registro a actualizar
        tk.Label(self.ventana_actualizar_registro, text="ID del Registro:").grid(row=0, column=0, pady=10, padx=10, sticky="w")
        self.entry_num_registro = tk.Entry(self.ventana_actualizar_registro)
        self.entry_num_registro.grid(row=0, column=1, pady=10, padx=10)

        # Campos para los nuevos valores
        tk.Label(self.ventana_actualizar_registro, text="Nuevo ID del Animal (deja en blanco para no cambiar):").grid(row=1, column=0, pady=10, padx=10, sticky="w")
        self.entry_animal = tk.Entry(self.ventana_actualizar_registro)
        self.entry_animal.grid(row=1, column=1, pady=10, padx=10)

        tk.Label(self.ventana_actualizar_registro, text="Nuevo Responsable (deja en blanco para no cambiar):").grid(row=2, column=0, pady=10, padx=10, sticky="w")
        self.entry_responsable = tk.Entry(self.ventana_actualizar_registro)
        self.entry_responsable.grid(row=2, column=1, pady=10, padx=10)

        tk.Label(self.ventana_actualizar_registro, text="Nueva Observación (deja en blanco para no cambiar):").grid(row=3, column=0, pady=10, padx=10, sticky="w")
        self.entry_observacion = tk.Entry(self.ventana_actualizar_registro)
        self.entry_observacion.grid(row=3, column=1, pady=10, padx=10)

        tk.Label(self.ventana_actualizar_registro, text="Nueva Fecha (YYYY-MM-DD) (deja en blanco para no cambiar):").grid(row=4, column=0, pady=10, padx=10, sticky="w")
        self.entry_fecha = tk.Entry(self.ventana_actualizar_registro)
        self.entry_fecha.grid(row=4, column=1, pady=10, padx=10)

        # Botón para guardar los cambios
        self.boton_guardar_actualizacion = tk.Button(self.ventana_actualizar_registro, text="Actualizar Registro", command=self.guardar_actualizacion)
        self.boton_guardar_actualizacion.grid(row=5, column=0, columnspan=2, pady=20)

    def guardar_modificacion(self):
        try:
            num_registro = int(self.entry_num_registro.get().strip())
            nuevo_animal = self.entry_animal.get().strip() or None
            nuevo_responsable = self.entry_responsable.get().strip() or None
            nueva_observacion = self.entry_observacion.get().strip() or None
            nueva_fecha_admin = self.entry_fecha.get().strip() or None

            # Construir la cláusula SET para la actualización
            set_clause = []
            parametros = []

            if nuevo_animal:
                set_clause.append("animal = %s")
                parametros.append(nuevo_animal)

            if nuevo_responsable:
                set_clause.append("responsable = %s")
                parametros.append(nuevo_responsable)

            if nueva_observacion:
                set_clause.append("observacion = %s")
                parametros.append(nueva_observacion)

            if nueva_fecha_admin:
                set_clause.append("fecha_admin = %s")
                parametros.append(nueva_fecha_admin)

            if set_clause:
                set_clause_str = ", ".join(set_clause)
                sentencia = f"UPDATE reg_vacunas SET {set_clause_str} WHERE num_registro = %s"
                parametros.append(num_registro)

                # Confirmar con el usuario antes de ejecutar
                if tk.messagebox.askyesno("Confirmar", "¿Ejecutar cambios?"):
                    cursor.execute(sentencia, tuple(parametros))
                    conexion.commit()
                    tk.messagebox.showinfo("Éxito", "Actualización realizada con éxito.")
                    self.ventana_actualizar_registro.destroy()  # Cerrar la ventana después de guardar
                else:
                    tk.messagebox.showinfo("Cancelado", "Actualización cancelada.")
            else:
                tk.messagebox.showinfo("Información", "No se realizaron cambios.")

        except ValueError:
            tk.messagebox.showerror("Error", "El ID del registro debe ser un número entero.")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error al actualizar el registro: {e}")

    def ver_datos_registro(self):
        # Crear una ventana para ver los datos del registro de vacuna
        self.ventana_ver_datos = tk.Toplevel(self)
        self.ventana_ver_datos.title("Ver Datos del Registro de Vacuna")
        self.ventana_ver_datos.geometry("400x300")

        # Campo para el ID del registro a buscar
        tk.Label(self.ventana_ver_datos, text="ID del Registro:").grid(row=0, column=0, pady=10, padx=10, sticky="w")
        self.entry_num_registro = tk.Entry(self.ventana_ver_datos)
        self.entry_num_registro.grid(row=0, column=1, pady=10, padx=10)

        # Botón para buscar los datos del registro
        self.boton_buscar_registro = tk.Button(self.ventana_ver_datos, text="Buscar Registro", command=self.mostrar_datos_registro)
        self.boton_buscar_registro.grid(row=1, column=0, columnspan=2, pady=20)

        # Área para mostrar los datos del registro
        self.texto_datos = tk.Text(self.ventana_ver_datos, height=10, width=50)
        self.texto_datos.grid(row=2, column=0, columnspan=2, pady=10, padx=10)
        self.texto_datos.config(state=tk.DISABLED)

    def mostrar_datos_registro(self):
        try:
            num_registro = int(self.entry_num_registro.get().strip())
            
            # Leer los datos del registro usando el método de la clase Registro
            cursor.execute("SELECT * FROM reg_vacunas WHERE num_registro = %s", (num_registro,))
            resultados = cursor.fetchall()
            
            # Mostrar los datos en el área de texto
            self.texto_datos.config(state=tk.NORMAL)
            self.texto_datos.delete(1.0, tk.END)
            
            if resultados:
                for i in resultados:
                    datos = (f"ID del Registro: {i[0]}\n"
                            f"ID del Animal: {i[1]}\n"
                            f"Responsable: {i[2]}\n"
                            f"Observación: {i[3]}\n"
                            f"Fecha de Administración: {i[4]}\n")
                    self.texto_datos.insert(tk.END, datos)
            else:
                self.texto_datos.insert(tk.END, "No se encontraron registros con ese ID.")
            
            self.texto_datos.config(state=tk.DISABLED)
        except ValueError:
            tk.messagebox.showerror("Error", "El ID del registro debe ser un número entero.")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error al leer el registro: {e}")


    def ver_todos_registros(self):
        # Crear una ventana para ver todos los registros de vacunas
        self.ventana_ver_todos = tk.Toplevel(self)
        self.ventana_ver_todos.title("Ver Todos los Registros de Vacunas")
        self.ventana_ver_todos.geometry("600x400")

        # Área para mostrar todos los registros
        self.texto_todos_registros = tk.Text(self.ventana_ver_todos, height=20, width=80)
        self.texto_todos_registros.pack(pady=10, padx=10)
        self.texto_todos_registros.config(state=tk.DISABLED)

        # Botón para cargar todos los registros
        self.boton_cargar_todos = tk.Button(self.ventana_ver_todos, text="Cargar Registros", command=self.mostrar_todos_registros)
        self.boton_cargar_todos.pack(pady=10)

    def mostrar_todos_registros(self):
        try:
            # Leer todos los registros usando el método de la clase Registro
            cursor.execute("SELECT * FROM reg_vacunas")
            resultados = cursor.fetchall()
            
            # Mostrar los registros en el área de texto
            self.texto_todos_registros.config(state=tk.NORMAL)
            self.texto_todos_registros.delete(1.0, tk.END)
            
            if resultados:
                for i in resultados:
                    datos = (f"ID del Registro: {i[0]}\n"
                            f"ID del Animal: {i[1]}\n"
                            f"Responsable: {i[2]}\n"
                            f"Observación: {i[3]}\n"
                            f"Fecha de Administración: {i[4]}\n"
                            f"{'-'*40}\n")
                    self.texto_todos_registros.insert(tk.END, datos)
            else:
                self.texto_todos_registros.insert(tk.END, "No se encontraron registros.")
            
            self.texto_todos_registros.config(state=tk.DISABLED)
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error al leer los registros: {e}")

    def salir_menu7(self):
        # Cerrar la ventana del menú de registro de vacunas
        self.ventana_vacunas.destroy()


    def salir(self):
        # implementa la lógica para salir del sistema
        self.destroy()

ventana = tk.Tk()
ventana.title("Pantalla Inicial")
ventana.geometry("1360x768")
ventana.configure(bg="#f2f2f2")  # Fondo de la ventana

def mostrar_ventana_inicio_sesion():
    for widget in ventana.winfo_children():
        widget.destroy()

    # Título
    tk.Label(ventana, text="Introduce tus credenciales", font=("Arial", 20, "bold"), bg="#f2f2f2").pack(pady=30)

    # Entrada de correo electrónico
    tk.Label(ventana, text="Correo electrónico:", font=("Arial", 14), bg="#f2f2f2").pack(pady=10)
    global entry_usuario
    entry_usuario = tk.Entry(ventana, font=("Arial", 14), width=30)
    entry_usuario.pack(pady=10)

    # Entrada de contraseña
    tk.Label(ventana, text="Contraseña:", font=("Arial", 14), bg="#f2f2f2").pack(pady=10)
    global entry_contrasena
    entry_contrasena = tk.Entry(ventana, show="*", font=("Arial", 14), width=30)
    entry_contrasena.pack(pady=10)

    # Botón de iniciar sesión
    tk.Button(ventana, text="Iniciar sesión", font=("Arial", 14), bg="#4CAF50", fg="white", command=inicioSesion, width=15).pack(pady=20)

    # Mensaje de resultado
    global resultado
    resultado = tk.Label(ventana, text="", font=("Arial", 14), bg="#f2f2f2")
    resultado.pack(pady=10)

    # Botón para regresar
    tk.Button(ventana, text="Regresar", font=("Arial", 14), bg="#f44336", fg="white", command=pantalla_inicial, width=15).pack(pady=10)

def mostrar_ventana_registrar():
    for widget in ventana.winfo_children():
        widget.destroy()

    tk.Label(ventana, text="Introduce tus datos", font=("Arial", 20, "bold"), bg="#f2f2f2").pack(pady=30)

    tk.Label(ventana, text="Nombre:", font=("Arial", 14), bg="#f2f2f2").pack(pady=10)
    global entry_nombre
    entry_nombre = tk.Entry(ventana, font=("Arial", 14), width=30)
    entry_nombre.pack(pady=10)

    tk.Label(ventana, text="Apellidos:", font=("Arial", 14), bg="#f2f2f2").pack(pady=10)
    global entry_apellidos
    entry_apellidos = tk.Entry(ventana, font=("Arial", 14), width=30)
    entry_apellidos.pack(pady=10)

    tk.Label(ventana, text="Correo electrónico:", font=("Arial", 14), bg="#f2f2f2").pack(pady=10)
    global entry_email
    entry_email = tk.Entry(ventana, font=("Arial", 14), width=30)
    entry_email.pack(pady=10)

    tk.Label(ventana, text="Contraseña:", font=("Arial", 14), bg="#f2f2f2").pack(pady=10)
    global entry_contrasena
    entry_contrasena = tk.Entry(ventana, show="*", font=("Arial", 14), width=30)
    entry_contrasena.pack(pady=10)

    tk.Button(ventana, text="Registrar", font=("Arial", 14), bg="#4CAF50", fg="white", command=registrarSesion, width=15).pack(pady=20)

    global resultado
    resultado = tk.Label(ventana, text="", font=("Arial", 14), bg="#f2f2f2")
    resultado.pack(pady=10)

    tk.Button(ventana, text="Regresar", font=("Arial", 14), bg="#f44336", fg="white", command=pantalla_inicial, width=15).pack(pady=10)

def registrarSesion():
    nombre = entry_nombre.get()
    apellidos = entry_apellidos.get()
    email = entry_email.get()
    password = entry_contrasena.get()
    
    if not nombre or not apellidos or not email or not password:
        resultado.config(text="Todos los campos son obligatorios", fg="red")
        return
    
    usuario = Usuario(nombre, apellidos, email, password)
    if usuario.registrar(conexion):
        resultado.config(text="Registro exitoso", fg="green")
        pantalla_inicial()
    else:
        resultado.config(text="Error al registrar el usuario", fg="red")

def inicioSesion():
    email = entry_usuario.get()
    contrasena = entry_contrasena.get()

    usuario = Usuario.iniciar_sesion(conexion, email, contrasena)

    if usuario:
        resultado.config(text="Inicio de sesión exitoso", fg="green")
        Aplicacion()  # Asumiendo que Aplicacion() es una función definida en otro lugar
    else:
        resultado.config(text="Correo o contraseña incorrectos", fg="red")

def pantalla_inicial():
    for widget in ventana.winfo_children():
        widget.destroy()

    tk.Label(ventana, text="Bienvenido a la Aplicación", font=("Arial", 24, "bold"), bg="#f2f2f2").pack(pady=50)

    tk.Button(ventana, text="Iniciar sesión", font=("Arial", 18), bg="#2196F3", fg="white", command=mostrar_ventana_inicio_sesion, width=20, height=2).pack(pady=20)
    tk.Button(ventana, text="Registrar usuario", font=("Arial", 18), bg="#FF9800", fg="white", command=mostrar_ventana_registrar, width=20, height=2).pack(pady=20)
    tk.Button(ventana, text="Salir", font=("Arial", 18), bg="#f44336", fg="white", command=salir, width=20, height=2).pack(pady=20)

def salir():
    ventana.quit()  # Cierra la aplicación Tkinter

# Llamar a la función para iniciar la pantalla inicial
pantalla_inicial()

# Iniciar el bucle principal
ventana.mainloop()
if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()