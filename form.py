import flet as ft

def main(page: ft.Page):
    page.title = "Mini formulario con Flet"
    page.bgcolor= "limeAccent100"

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    nombre = ft.TextField(label="Nombre", width=250)
    correo = ft.TextField(label="Correo electrónico", width=250)
    edad = ft.TextField(label="Edad", width=250 )

    resultado = ft.Text("", size=14, text_align=ft.TextAlign.CENTER)

    def enviar(e):
        if not nombre.value or not correo.value or not edad.value:
            resultado.value = "Por favor, completa todos los campos."
            resultado.color = "red"
        elif not edad.value.isdigit():
            resultado.value = "La edad debe ser un número."
            resultado.color = "red"
        else:
            resultado.value = f"Hola{nombre.value}, registro exitoso"
            resultado.color = "green"

            nombre.value = ""
            correo.value = ""
            edad.value = ""

        page.update()

        btn = ft.ElevatedButton("Enviar", on_click=enviar)

        formulario = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Formulario", size=20, weight="bold"),
                    nombre,
                    correo,
                    edad,
                    btn,
                    resultado
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15
            ),
            padding=20,
            border_radius=15,
            bgcolor=ft.Color.GRAY_100,
            width=300
        )

ft.app(target=main)