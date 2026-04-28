import flet as ft 
import sqlite3
import sys

def main(page: ft.Page):

    page.title = "CRUD Usuarios"
    page.bgcolor = ft.Colors.LIME_100
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    conn = sqlite3.connect("datos.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios2 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        correo TEXT,
        edad INTEGER
    )
""")
    conn.commit()

    id_usuario = ft.TextField(label="ID", width=250, read_only=True, label_style=ft.TextStyle(color=ft.Colors.GREY_400))
    nombre = ft.TextField(label="Nombre", autofocus=True, width=250, label_style=ft.TextStyle(color=ft.Colors.GREY_400))
    correo = ft.TextField(label="Correo", width=250, label_style=ft.TextStyle(color=ft.Colors.GREY_400))
    edad = ft.TextField(label="Edad", width=250,label_style=ft.TextStyle(color=ft.Colors.GREY_400))

    resultado = ft.Text()

    lista_datos = ft.Container(
        content=ft.Column(scroll=ft.ScrollMode.AUTO),
        height=150,
        width=350,
        bgcolor=ft.Colors.WHITE,
        border_radius=10,
        padding=5
    )


    def limpiar(e):
        id_usuario.value = ""
        nombre.value = ""
        correo.value = ""
        edad.value = ""
        resultado.value = ""
        page.update()

    def consultar(e): 
        lista_datos.content.controls.clear()
        resultado.value =" "

        cursor.execute("SELECT id, nombre, correo, edad FROM usuarios2") # hace la consulta
        registros = cursor.fetchall() # obtiene los datos y los gurda en la variable registros    

        for id_, nom, cor, ed in registros: 
            def seleccionar(e, id_=id_, nom=nom, cor=cor, ed=ed):
                id_usuario.value = str(id_)
                nombre.value = nom
                correo.value = cor
                edad.value = str(ed)

                resultado.value = f"Seleccionado ID: {id_}"
                resultado.color = "blue"
                page.update()

            lista_datos.content.controls.append(
                ft.ListTile(
                    title=ft.Text(f"{nom} ({ed})"),
                    subtitle=ft.Text(cor),
                    on_click=seleccionar # al dar clic Se cargan los datos al formulario
                )
            )

            page.update()

    def guardar(e):
        if not nombre.value or not correo.value or not edad.value:
            resultado.value = "⚠️ Campos obligatorios"
            resultado.color = "red"

        elif not edad.value.isdigit():
            resultado.value = "⚠️ Edad inválida"
            resultado.color = "red"

        else:
            cursor.execute(
                "INSERT INTO usuarios2 (nombre, correo, edad) VALUES (?, ?, ?)",
                (nombre.value, correo.value, edad.value)
            )
            conn.commit()  # Confirma y Guarda cambios en la BD

            resultado.value = "✅ Registro guardado"
            resultado.color = "green"

            limpiar(None)
            consultar(None)

        page.update()

    def actualizar(e):
        if not id_usuario.value:
            resultado.value = "⚠️ Selecciona un registro"
            resultado.color = "red"
        else:
            cursor.execute(
                "UPDATE usuarios2 SET nombre=?, correo=?, edad=? WHERE id=?",
                (nombre.value, correo.value, edad.value, id_usuario.value)
            )
            conn.commit()

            resultado.value = "✏️ Registro actualizado"
            resultado.color = "blue"

            consultar(None)
            page.update()

    def eliminar(e):

        if not id_usuario.value:
            resultado.value = "⚠️ Selecciona un registro"
            resultado.color = "red"
            page.update()
            return

        print("Eliminando ID:", id_usuario.value)

        cursor.execute(
            "DELETE FROM usuarios2 WHERE id=?",
            (id_usuario.value,)
        )
        conn.commit() # actualiza cambios en la base de datos

        print("Filas afectadas:", cursor.rowcount)

        if cursor.rowcount == 0:
            resultado.value = "⚠️ No se encontró el registro"
            resultado.color = "orange"
        else:
            limpiar(None)
            consultar(None)
            resultado.value = "🗑️ Registro eliminado"
            resultado.color = "red"

        page.update()

    def salir(e):
        conn.close()
        sys.exit()

    btn_guardar = ft.Button("Guardar", on_click=guardar, width=100)
    btn_consultar = ft.Button("Consultar", on_click=consultar, width=110)
    btn_actualizar = ft.Button("Actualizar", on_click=actualizar, width=115)

    btn_eliminar = ft.Button("Eliminar", on_click=eliminar, width=105)
    btn_limpiar = ft.Button("Limpiar", on_click=limpiar, width=100)
    btn_salir = ft.Button("Salir", on_click=salir, width=100,bgcolor="red")

    fila1 = ft.Row( 
        [btn_guardar, btn_consultar, btn_actualizar],
        alignment=ft.MainAxisAlignment.CENTER
    )

    fila2 = ft.Row( 
        [btn_eliminar, btn_limpiar, btn_salir],
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("CRUD USUARIOS", size=20, weight="bold"),
                    id_usuario,
                    nombre,
                    correo,
                    edad,
                    fila1,
                    fila2,
                    resultado,
                    lista_datos
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            ),
            padding=20,
            border_radius=15,
            bgcolor=ft.Colors.GREY_100,
            width=400
        )
    )

    consultar(None)

ft.run(main)