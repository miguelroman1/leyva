import flet as ft

def main(page: ft.Page):
    page.title = "App con botón"

    page.window_width = 320  
    page.window_height = 420
   
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    mensaje = ft.Text("Hola, escribe algo abajo 👇", size=16)

    caja_texto = ft.TextField(label="Escribe tu mensaje")

    def cambiar_texto(e):
        mensaje.value = f"Tú escribiste: {caja_texto.value}"  
        mensaje.color = "purple"   
        page.update()     
    boton1 = ft.Button("Mostrar texto", on_click=cambiar_texto)

    page.add(
        ft.Column(
            controls=[mensaje, caja_texto, boton1],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)