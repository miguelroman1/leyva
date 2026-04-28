import flet as ft
import sqlite3

def main(page: ft.Page): 
    page.title = "Mini formulario" 
    page.window_width = 350 
    page.window_height = 500
    page.bgcolor = "black"

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    conn = sqlite3.connect("datos.db")
    
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            correo TEXT,
            edad INTEGER
        )
    """)
    
    conn.commit()


    nombre = ft.TextField(prefix_icon=ft.Icons.PERSON,label="Nombre", width=250, border_color=ft.Colors.GREEN_200) 
    correo = ft.TextField(prefix_icon=ft.Icons.EMAIL,label="Correo", width=250, border_color=ft.Colors.GREEN_200) 
    edad = ft.TextField(prefix_icon=ft.Icons.CALENDAR_TODAY,label="Edad", width=250, border_color=ft.Colors.GREEN_200) 

    resultado = ft.Text("", size=14, text_align=ft.TextAlign.CENTER)
    
    def guardar(e):
        if not nombre.value or not correo.value or not edad.value:
            resultado.value = "⚠️ Todos los campos son obligatorios"
            resultado.color = "red"
        elif not edad.value.isdigit(): 
            resultado.value = "⚠️ La edad debe ser un número"
            resultado.color = "red"
        else:
            cursor.execute("INSERT INTO usuarios (nombre, correo, edad) VALUES (?, ?, ?)", 
                        (nombre.value, correo.value, int(edad.value)))
            conn.commit()
            
            resultado.value = f"✅ Datos guardados en la db"
            resultado.color = "green"

            nombre.value = ""
            correo.value = ""
            edad.value = ""

        page.update()

    boton = ft.ElevatedButton("Guardar", on_click=guardar, style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_400, color=ft.Colors.WHITE))

    formulario = ft.Container(
        content=ft.Column(
            controls=[ 
                ft.Text("Formulario", size=20, weight="bold", color=ft.Colors.GREEN_700),
                nombre,
                correo,
                edad,
                boton,
                resultado
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        ),
        padding=20,
        border_radius=15,
        bgcolor=ft.Colors.GREY_800,
        border=ft.border.all(2, "green"),
        width=300
    )
    
    page.add(formulario)

ft.app(target=main)