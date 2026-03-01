# 🎮 Tutorial: Creando y Ejecutando "Piedra, Papel o Tijera" con Flet

¡Bienvenido! En este tutorial aprenderás paso a paso cómo se estructuró el juego de **Piedra, Papel o Tijera** utilizando **Flet** (un framework de Python que te permite construir aplicaciones web, de escritorio y móviles sin necesidad de saber HTML, CSS o JavaScript) y, lo más emocionante, **cómo jugarlo directamente en tu teléfono móvil escaneando un código QR**.

---

## 🛠️ Parte 1: ¿Cómo se construyó el juego? (Código a detalle)

El juego completo se encuentra en el archivo `Juego.py`. A continuación, desglosaremos las partes más importantes del código para entender cómo funciona.

### 1. Importaciones y Configuración Inicial
Para empezar, necesitamos importar `flet`. También importamos `random` (para que la computadora elija su jugada) y `time` (para una pequeña pausa animada). 
Todo el contenido visual de Flet debe ir dentro de una función principal, que tradicionalmente llamamos `main` y recibe el parámetro `page` (la pantalla de tu app).

```python
import flet as ft
import random
import time

def main(page: ft.Page):
    # Configuración principal de la ventana
    page.title = "Piedra, Papel o Tijera"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 400
    page.window.height = 650
    page.window.resizable = False
    page.padding = 20
    page.bgcolor = "#F0F4F8"
```
* **Explicación:** Aquí le decimos a Flet de qué tamaño queremos la ventana (400x650 pixeles, parecido a un móvil) y definimos su color de fondo con un código hexadecimal `"#F0F4F8"`.

### 2. Estado del Juego y Reglas
Antes de pintar la interfaz, necesitamos variables que recuerden cómo va la partida: los puntos y si hay una animación en curso para evitar clics dobles.

```python
    # Variables de estado
    puntaje_jugador = 0
    puntaje_cpu = 0
    empates = 0
    animando = False

    # Diccionario con los Emojis visuales
    OPCIONES = {
        "Piedra": "✊",
        "Papel": "✋",
        "Tijera": "✌️",
    }

    # Diccionario de reglas: Quién le gana a quién
    # Clave: Lo que yo elijo -> Valor: A lo que le gano
    REGLAS = {
        "Piedra": "Tijera",
        "Papel": "Piedra",
        "Tijera": "Papel",
    }
```
* **Explicación:** Los diccionarios `OPCIONES` y `REGLAS` simplifican muchísimo la lógica. Para saber si ganamos, solo preguntaremos si `REGLAS[Mi_Eleccion] == Eleccion_Del_CPU`.

### 3. Diseñando la Interfaz Visual (Textos y Tarjetas)
En Flet, todo en la pantalla es un *Control*. Creamos controles de Texto (`ft.Text`) y los agrupamos en Filas (`ft.Row`) y Columnas (`ft.Column`).

```python
    # Textos que muestran los puntos (inician en "0")
    texto_jugador = ft.Text("0", size=30, color="blue")
    texto_cpu = ft.Text("0", size=30, color="red")
    texto_empate = ft.Text("0", size=20, color="gray")

    # Función auxiliar para crear un cuadrito (tarjeta) para cada marcador
    def tarjeta(nombre, texto):
        return ft.Container(
            content=ft.Column([ft.Text(nombre), texto], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            bgcolor="white",
            padding=10,
            border_radius=10,
            width=100,
        )

    # Agrupamos las tres tarjetas en una fila horizontal
    fila_puntaje = ft.Row(
        [tarjeta("Jugador", texto_jugador), tarjeta("Empates", texto_empate), tarjeta("CPU", texto_cpu)],
        alignment=ft.MainAxisAlignment.CENTER,
    )
```
* **Explicación:** Empaquetar marcadores dentro de un `ft.Container` nos permite darles un fondo blanco, bordes redondeados (`border_radius`) y márgenes (`padding`), haciéndolo lucir moderno como tarjetas reales. 
Además, guardar estos textos en variables (`texto_jugador`, `texto_cpu`) es clave porque más adelante, al modificar la propiedad `.value` de estos objetos, Flet actualizará el número en pantalla automáticamente.

---

### 4. Manteniendo la Pantalla Sincronizada: La función `actualizar()`
Antes de pasar a la lógica principal, el código define una pequeña función que se encarga exclusivamente de reflejar los puntos en pantalla:

```python
    def actualizar():
        # Tomamos el valor de las variables numéricas y reemplazamos el texto en pantalla
        texto_jugador.value = str(puntaje_jugador)
        texto_cpu.value = str(puntaje_cpu)
        texto_empate.value = str(empates)
```
* **¿Por qué esto es importante?** En aplicaciones Flet o Reactivas, el estado (los números reales en memoria) y la vista (lo que ve el usuario) están separados. Sumarle `1` a la variable `puntaje_jugador` en código Python no hace que la pantalla cambie mágicamente. Tenemos que forzar a que la propiedad `.value` de los textos se iguale a las variables.

---

### 5. La Lógica Principal: La función `jugar()`
Esta es la función que se ejecuta cada vez que presionas un botón ("Piedra", "Papel" o "Tijera").

```python
    def jugar(eleccion):
        # Usamos nonlocal para poder modificar las variables declaradas arriba
        nonlocal puntaje_jugador, puntaje_cpu, empates, animando

        if animando: return # Evita clics rápidos
        animando = True

        # El CPU elige aleatoriamente de las llaves del diccionario ("Piedra", "Papel", "Tijera")
        cpu = random.choice(list(OPCIONES.keys()))

        # Actualizamos la pantalla con los emojis elegidos
        display_jugador.value = OPCIONES[eleccion]
        display_cpu.value = OPCIONES[cpu]

        # Lógica para determinar al ganador
        if eleccion == cpu:
            empates += 1
            resultado.value = "🤝 Empate"
        elif REGLAS[eleccion] == cpu:
            puntaje_jugador += 1
            resultado.value = "🎉 Ganaste"
        else:
            puntaje_cpu += 1
            resultado.value = "💻 La CPU gana"

        # ⚠️ SÚPER IMPORTANTE: Actualizar los Textos y decirle a la pantalla que se redibuje
        actualizar()
        page.update()

        # Pequeña pausa antes de permitir el siguiente turno
        time.sleep(0.2)
        animando = False
```
* **El uso de `nonlocal`:** En Python, si defines una variable fuera de una función (como nuestros contadores de puntos) e intentas modificarla dentro de una función anidada (`jugar`), Python podría creer que estás creando una variable nueva local. La palabra clave `nonlocal` le dice a Python explícitamente: *"Oye, no crees una variable nueva, modifica las de estado que están declaradas arriba en la ventana principal"*.

---

### 6. La función para `reiniciar()` el juego
Toda buena aplicación necesita un botón de *Reset* para volver a empezar. Fíjate cómo la lógica es idéntica a `jugar()`: primero se altera la información interna y luego la visual.

```python
    def reiniciar(e):
        nonlocal puntaje_jugador, puntaje_cpu, empates

        # 1. Regresamos las variables a 0
        puntaje_jugador = 0
        puntaje_cpu = 0
        empates = 0

        # 2. Limpiamos la pantalla visual regresando los emojis a signo de interrogación
        display_jugador.value = "❔"
        display_cpu.value = "❔"
        resultado.value = "Juego reiniciado"

        # 3. Sincronizamos los textos a cero y renderizamos la pantalla para que el usuario note el cambio
        actualizar()
        page.update()
```

---

### 7. Botones y Ensamblaje Final
Por último, creamos los botones y agregamos todos los componentes a nuestra página (`page.add(...)`).

```python
    # Botones principales interactivos
    botones = ft.Row(
        [
            # lambda e: jugar(...) sirve para pasar el parámetro de nuestra elección al dar click
            ft.ElevatedButton("✊ Piedra", on_click=lambda e: jugar("Piedra")),
            ft.ElevatedButton("✋ Papel", on_click=lambda e: jugar("Papel")),
            ft.ElevatedButton("✌️ Tijera", on_click=lambda e: jugar("Tijera")),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # Agregamos todo a la página ordenado verticalmente (en una Columna)
    page.add(
        ft.Column(
            [titulo, subtitulo, fila_puntaje, ft.Divider(), area_juego, resultado, botones, boton_reset],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )

# Instrucción para iniciar la aplicación de Flet
if __name__ == "__main__":
    ft.app(target=main)
```

---

## 📱 Parte 2: Ejecuta tu juego en tu Teléfono (Escaneando un QR)

Flet permite correr esta misma aplicación de escritorio en tu teléfono (iOS o Android) de manera instantánea vía red local y Wi-Fi utilizando su app oficial. **No necesitas compilar archivos `.apk` ni `.ipa`.**

Sigue estos sencillos pasos:

### Paso 1: Descarga la App de Flet
Desde tu teléfono móvil, dirígete a tu tienda de aplicaciones:
* **En Android:** Busca e instala "Flet" en la [Google Play Store].
* **En iOS / iPhone:** Busca e instala "Flet" en la [App Store].

### Paso 2: Conéctate a la misma red Wi-Fi 🛜
Asegúrate de que tu computadora (donde estás ejecutando el código) y tu teléfono móvil estén conectados a la **misma red Wi-Fi**. Esto es obligatorio, de lo contrario no se podrán comunicar.

### Paso 3: Genera el Código QR en tu computadora
Abre una terminal (CMD, PowerShell o la terminal integrada de tu editor como VS Code) asegurándote de estar ubicado en la carpeta donde guardaste tu archivo `Juego.py`.

A continuación, en lugar de usar comandos como `python Juego.py`, usarás Flet para lanzar el servidor.
Escribe el siguiente comando y da Enter:

```bash
flet run Juego.py --android
```
*(Nota: Si usas iPhone, puedes escribir el flag `--ios` en lugar de `--android`. Ambos levantan temporalmente el servidor QR de manera similar).*

> **💡 ¿Qué ocurre tras teclear esto?**
> Flet levantará un servidor interno en la red de tu casa/escuela y en tu terminal aparecerá dibujado un **Código QR gigante** hecho con símbolos ASCII.

### Paso 4: ¡Escanea y juega!
1. Toma tu teléfono móvil y abre la aplicación **Flet** que descargaste.
2. Dentro de la App, busca la opción de escanear o simplemente abre la **Cámara** normal de tu teléfono y apunta tu cámara al **Código QR** que se muestra en la pantalla de tu computadora.
3. Se abrirá un enlace que conectará automáticamente la app de Flet.
4. **¡Listo!** Verás la interfaz de tu juego *Piedra, Papel o Tijera* exactamente como la diseñaste. ¡Interactúa con los botones, y visualiza la lógica procesada desde tu PC pero visible y jugable en la palma de tu mano!

*(Extra: Si el programa sigue corriendo en la computadora, cualquier cambio de colores, textos o lógica que le hagas y guardes en tu código `Juego.py`, se recargará automáticamente ¡al instante en tu móvil!)*
---

## 🚀 Requisitos Previos e Instalación

Para que todo esto funcione en tu computadora y puedas enviar el juego a tu celular, asegúrate de tener instaladas las siguientes herramientas:

1. **Python:** Descarga e instala la última versión desde [python.org](https://www.python.org/). OJO: Durante la instalación, asegúrate de marcar la casilla *"Add Python to PATH"*.
2. **Flet:** Una vez que Python esté instalado, abre tu consola o terminal y escribe el siguiente comando para descargar Flet en tu PC:
```bash
pip install flet
```

---

## 🐛 Errores Comunes (Solución de problemas)

Si tienes problemas probando el juego en el celular con el código QR, verifica lo siguiente:

* **"No se reconoce el comando flet":** Esto significa que instalaste Flet, pero tu computadora no lo encuentra en las variables de entorno (PATH). Intenta abrir una nueva terminal desde cero o usar el comando `python -m flet run Juego.py --android`.
* **La app del celular se queda cargando o dice "Error de conexión":**
   * Regla de oro: Tu PC y tu celular **tienen** que estar conectados al mismo Wi-Fi. No servirá si la PC tiene cable Ethernet a un modem distinto o si el celular está usando Datos Móviles (4G/5G).
   * Puede que el *Firewall* (Cortafuegos) de Windows o de tu Antivirus esté bloqueando al servidor de Python. Asegúrate de darle permisos a Python para redes públicas y privadas en la ventana emergente de Seguridad de Windows que suele aparecer la primera vez que ejecutas Flet.

---

## 📦 Pasa tu juego a tus amigos (Crear un .exe)

Otra maravilla de Flet es que no solo te permite probarlo en celular, sino que puedes empaquetar tu código `.py` en un ejecutable real (`.exe` o `.app` en Mac) para que cualquier persona pueda jugarlo en su computadora sin tener que instalar Python.

Para hacer esto, abre la consola en la carpeta de tu juego y usa el comando:
```bash
flet pack Juego.py
```
*(Esto creará una carpeta llamada `dist` donde estará tu archivo ejecutable listo para mandárselo a quien tú quieras).*
