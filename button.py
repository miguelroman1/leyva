import flet as ft

def main(page: ft.Page): 
    page.title = "App con botón" 

    mensaje = ft.Text("Hola, mundo desde Flet!", size=25, color="blue")

    def cambiar_texto(e):
        mensaje.value = "¡El mensaje ha cambiado!" 
        mensaje.color = "red" 
        page.update() 


    boton1 = ft.ElevatedButton("Cambiar mensaje", on_click=cambiar_texto)

    page.add(mensaje, boton1)

ft.app(target=main)