import flet as ft

def main(page: ft.Page): 
    page.title = "Mini formulario" 
    page.window_width = 350 
    page.window_height = 500
    page.bgcolor = "black"

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    nombre = ft.TextField(prefix_icon=ft.Icons.PERSON, label="Nombre", width=250, border_color="lightBlueAccent") 
    correo = ft.TextField(prefix_icon=ft.Icons.EMAIL, label="Correo", width=250, border_color="lightBlueAccent") 
    edad = ft.TextField(prefix_icon=ft.Icons.CALENDAR_TODAY, label="Edad", width=250, border_color="lightBlueAccent") 

    resultado = ft.Text("", size=14, text_align=ft.TextAlign.CENTER)

    def enviar(e):
        if not nombre.value or not correo.value or not edad.value:
            resultado.value = "⚠️ Todos los campos son obligatorios"
            resultado.color = "red"
        elif not edad.value.isdigit(): 
            resultado.value = "⚠️ La edad debe ser un número"
            resultado.color = "red"
        else:
            resultado.value = f"✅ Hola {nombre.value}, registro exitoso"
            resultado.color = "green"

            nombre.value = ""
            correo.value = ""
            edad.value = ""

        page.update() 
    boton = ft.Button("Enviar", on_click=enviar)

    formulario = ft.Container(
        content=ft.Column(
            controls=[ 
                ft.Text("Formulario", size=20, weight="bold"),
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
        bgcolor=ft.Colors.GREY_100,
        width=300
    )
    
    page.add(formulario)

ft.app(target=main)