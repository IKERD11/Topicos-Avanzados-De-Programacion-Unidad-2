import flet as ft
import random
import time


def main(page: ft.Page):
    # Configuración de la ventana
    page.title = "Piedra, Papel o Tijera"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 400
    page.window.height = 650
    page.window.resizable = False
    page.padding = 20
    page.bgcolor = "#F0F4F8"

    # Estado del juego
    puntaje_jugador = 0
    puntaje_cpu = 0
    empates = 0
    animando = False

    # Opciones
    OPCIONES = {
        "Piedra": "✊",
        "Papel": "✋",
        "Tijera": "✌️",
    }

    REGLAS = {
        "Piedra": "Tijera",
        "Papel": "Piedra",
        "Tijera": "Papel",
    }

    # Título
    titulo = ft.Text(
        "✊ Papel o Tijera ✋",
        size=28,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )

    subtitulo = ft.Text(
        "Piedra, Papel o Tijera",
        size=16,
        color="gray",
        text_align=ft.TextAlign.CENTER,
    )

    # Marcadores
    texto_jugador = ft.Text("0", size=30, color="blue")
    texto_cpu = ft.Text("0", size=30, color="red")
    texto_empate = ft.Text("0", size=20, color="gray")

    def tarjeta(nombre, texto):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(nombre),
                    texto,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor="white",
            padding=10,
            border_radius=10,
            width=100,
        )

    fila_puntaje = ft.Row(
        [
            tarjeta("Jugador", texto_jugador),
            tarjeta("Empates", texto_empate),
            tarjeta("CPU", texto_cpu),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # Área de juego
    display_jugador = ft.Text("❔", size=60)
    display_cpu = ft.Text("❔", size=60)

    area_juego = ft.Row(
        [
            ft.Column(
                [ft.Text("Jugador"), display_jugador],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            ft.Column(
                [ft.Text("CPU"), display_cpu],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50,
    )

    resultado = ft.Text(
        "Selecciona una opción",
        size=18,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )

    # Actualizar puntaje
    def actualizar():
        texto_jugador.value = str(puntaje_jugador)
        texto_cpu.value = str(puntaje_cpu)
        texto_empate.value = str(empates)

    # Lógica del juego
    def jugar(eleccion):
        nonlocal puntaje_jugador, puntaje_cpu, empates, animando

        if animando:
            return

        animando = True

        cpu = random.choice(list(OPCIONES.keys()))

        display_jugador.value = OPCIONES[eleccion]
        display_cpu.value = OPCIONES[cpu]

        if eleccion == cpu:
            empates += 1
            resultado.value = "🤝 Empate"

        elif REGLAS[eleccion] == cpu:
            puntaje_jugador += 1
            resultado.value = "🎉 Ganaste"

        else:
            puntaje_cpu += 1
            resultado.value = "💻 La CPU gana"

        actualizar()
        page.update()

        time.sleep(0.2)
        animando = False

    # Reiniciar
    def reiniciar(e):
        nonlocal puntaje_jugador, puntaje_cpu, empates

        puntaje_jugador = 0
        puntaje_cpu = 0
        empates = 0

        display_jugador.value = "❔"
        display_cpu.value = "❔"
        resultado.value = "Juego reiniciado"

        actualizar()
        page.update()

    # Botones
    botones = ft.Row(
        [
            ft.ElevatedButton("✊ Piedra", on_click=lambda e: jugar("Piedra")),
            ft.ElevatedButton("✋ Papel", on_click=lambda e: jugar("Papel")),
            ft.ElevatedButton("✌️ Tijera", on_click=lambda e: jugar("Tijera")),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        wrap=True,
    )

    boton_reset = ft.ElevatedButton(
        "🔄 Reiniciar juego",
        bgcolor="red",
        color="white",
        on_click=reiniciar,
    )

    # Layout
    page.add(
        ft.Column(
            [
                titulo,
                subtitulo,
                fila_puntaje,
                ft.Divider(),
                area_juego,
                resultado,
                botones,
                boton_reset,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )


# Ejecutar aplicación
if __name__ == "__main__":
    ft.app(target=main)