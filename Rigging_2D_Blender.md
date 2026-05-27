# 🎬 Tutorial Completo de Rigging 2D en Blender: De Cero a Héroe

![Blender](https://img.shields.io/badge/Blender-2.8+-orange?style=for-the-badge&logo=blender&logoColor=white)
![Nivel](https://img.shields.io/badge/Nivel-Intermedio-blue?style=for-the-badge)
![Estado](https://img.shields.io/badge/Estado-Completado-success?style=for-the-badge)

<details>
<summary>📋 <b>Tabla de Contenidos</b> (Haz clic para expandir)</summary>

- [1. Prerrequisitos](#1-prerrequisitos)
- [2. Paso a Paso: Creación del Rig](#2-paso-a-paso-creación-del-rig)
- [3. Parentesco y Weight Painting](#3-parentesco-y-weight-painting)
- [4. Cinemática Inversa (IK)](#4-cinemática-inversa-ik---magia-para-animar)
- [5. Formas Personalizadas (Custom Bones)](#5-formas-personalizadas-custom-bones---estilizando-tu-rig)
- [6. Animación Final](#6-animación-final)
- [7. Videos de Referencia](#7-videos-de-referencia-más-recursos)
- [8. Subir a GitHub](#8-subir-a-github)

</details>

---

¡Bienvenido a esta guía completa sobre rigging 2D en Blender! El **rigging** es el proceso de crear un esqueleto (armature) para un personaje, permitiendo que cobre vida a través de la animación. Aunque Blender es famoso por su entorno 3D, sus herramientas para animación 2D son increíblemente potentes y versátiles.

En este tutorial, no solo aprenderás a construir un esqueleto, sino también a implementar técnicas avanzadas como la **Cinemática Inversa (IK)** para lograr movimientos fluidos y naturales.

<div align="center">
  <img src="./1.png" alt="Referencia de Rigging">
</div>

---

## 1. Prerrequisitos

Antes de sumergirnos en el mundo del rigging, asegúrate de tener todo listo:

*   **Blender:** Descarga la última versión desde [blender.org](https://www.blender.org/download/). Este tutorial es compatible con Blender 2.8x y versiones posteriores.
*   **Imagen del Personaje:** Es fundamental que tengas una imagen de tu personaje con las **partes del cuerpo separadas** (cabeza, torso, brazo, antebrazo, etc.). Lo ideal es tener cada parte como un archivo PNG con fondo transparente.

> [!TIP]
> **Consejo de Diseño:** Un buen diseño de personaje, ya separado por piezas desde su concepción, te ahorrará mucho tiempo y te facilitará enormemente el proceso de rigging.

---

## 2. Paso a Paso: Creación del Rig

### Paso 2.1: Preparar el Espacio de Trabajo

1.  Abre Blender y selecciona `2D Animation`. Esto configura el entorno ideal para nuestro trabajo.
2.  Asegúrate de estar en la **vista de cámara** (<kbd>Numpad 0</kbd>) y en modo ortográfico.
3.  Importa las partes de tu personaje usando `Add > Image > As Planes`. Si no encuentras esta opción, actívala en `Edit > Preferences > Add-ons` buscando "Import Images as Planes".
4.  Organiza las diferentes partes del cuerpo en la vista, ensamblando a tu personaje.

### Paso 2.2: Creación del Esqueleto (Armature)

El esqueleto es el corazón de nuestro rig.

1.  Coloca el cursor 3D en el centro de tu personaje (<kbd>Shift</kbd> + <kbd>C</kbd>).
2.  Añade una armadura: `Add > Armature`.
3.  En las propiedades del `Armature`, ve a `Viewport Display` y activa **`In Front`**. Esto mantendrá los huesos siempre visibles.

![Hueso inicial](2.png)

### Paso 2.3: Construyendo el Esqueleto

Vamos a darle forma a ese esqueleto.

1.  Entra en **`Edit Mode`** (<kbd>Tab</kbd>).
2.  Mueve y escala el primer hueso para que se ajuste a la **pelvis** o al **torso inferior**.
3.  Selecciona la punta de un hueso y presiona <kbd>E</kbd> para extruir nuevos huesos, formando la columna, el cuello y la cabeza.
4.  Para las extremidades, extruye desde las articulaciones (hombros y caderas) para crear los brazos y las piernas.

<details>
<summary>🦴 <b>Ver Diagrama Conceptual del Esqueleto</b></summary>

A continuación se muestra la sugerencia de jerarquía para los huesos principales:

```mermaid
graph TD
    A[Pelvis] --> B[Torso];
    B --> C[Pecho];
    C --> D[Cuello];
    D --> E[Cabeza];
    C -- "Extruir" --> F[Hombro_L];
    F --> G[Brazo_L];
    G --> H[Antebrazo_L];
    H --> I[Mano_L];
    C -- "Extruir" --> J[Hombro_R];
    J --> K[Brazo_R];
    K --> L[Antebrazo_R];
    L --> M[Mano_R];
    A -- "Extruir" --> N[Cadera_L];
    N --> O[Pierna_L];
    O --> P[Pantorrilla_L];
    P --> Q[Pie_L];
    A -- "Extruir" --> R[Cadera_R];
    R --> S[Pierna_R];
    S --> T[Pantorrilla_R];
    T --> U[Pie_R];
```

</details>

### Paso 2.4: Nombrar los Huesos

Un rig bien organizado es un rig feliz. En `Edit Mode`, selecciona un hueso y presiona <kbd>F2</kbd> para renombrarlo. Usa sufijos como **`.L`** (izquierda) y **`.R`** (derecha).

---

## 3. Parentesco y Weight Painting

### Paso 3.1: Conectando el Personaje al Esqueleto

1.  En `Object Mode`, selecciona todas las partes de la malla de tu personaje, y finalmente, con <kbd>Shift</kbd> + **Click**, selecciona el `Armature`.
2.  Presiona <kbd>Ctrl</kbd> + <kbd>P</kbd> y elige **`With Automatic Weights`**.

### Paso 3.2: El Arte del Weight Painting

`Automatic Weights` es un buen punto de partida, pero el **`Weight Painting`** te da el control total.

1.  Selecciona el `Armature`, luego la malla, y entra en **`Weight Paint Mode`** (<kbd>Ctrl</kbd> + <kbd>Tab</kbd>).
2.  En el `Armature`, entra en **`Pose Mode`** para poder mover los huesos y ver cómo afectan a la malla en tiempo real.
3.  Selecciona un hueso (en `Pose Mode`) y pinta sobre la malla para ajustar su influencia: 🔴 **rojo** para máxima influencia, 🔵 **azul** para nula.

![Weight Painting](3.png)

---

## 4. Cinemática Inversa (IK) - ¡Magia para Animar!

La Cinemática Inversa (IK) te permite mover una cadena de huesos (como un brazo o una pierna) simplemente moviendo el último hueso de la cadena (la mano o el pie).

### Paso 4.1: Creando el Hueso Controlador IK

1.  En `Edit Mode`, selecciona la punta de la mano o el pie y extruye un nuevo hueso (<kbd>E</kbd>).
2.  Desconéctalo de la cadena principal: <kbd>Alt</kbd> + <kbd>P</kbd> > `Clear Parent`.
3.  Nómbralo claramente, por ejemplo, `control_mano.L`.

### Paso 4.2: Aplicando la Restricción IK

1.  Ve a **`Pose Mode`**.
2.  Selecciona el hueso del **antebrazo** (o la pantorrilla).
3.  Ve al panel de `Bone Constraints` (el icono de la cadena) y añade una restricción **`Inverse Kinematics`**.
4.  En la configuración de la restricción:
    *   **Target:** Elige tu `Armature`.
    *   **Bone:** Selecciona el hueso controlador que creaste (`control_mano.L`).
    *   **Chain Length:** Ajústalo a `2` para que afecte al antebrazo y al brazo.

> [!NOTE]
> ¡Al mover el hueso controlador que acabas de configurar, todo el brazo se moverá de forma conectada natural!

---

## 5. Formas Personalizadas (Custom Bones) - Estilizando tu Rig

Una vez que tu esqueleto y la IK funcionan correctamente, ver tantos huesos octaédricos (las formas por defecto) puede volverse confuso. Los **Custom Bones** (huesos personalizados) te permiten reemplazar la apariencia de los huesos por mallas geométricas (círculos, flechas, cuadrados) sin alterar sus funciones mecánicas.

Esto es un estándar en la industria porque logra que el rig sea interactivo, limpio y mucho más intuitivo para el animador (evitando clics accidentales).

### Paso 5.1: Crear y Modelar la Geometría Custom
No necesitas ser un modelador experto. Los controladores suelen ser líneas simples o "alambres" (wireframes) para que no bloqueen la vista de tu dibujo 2D. 

1. Asegúrate de estar en **`Object Mode`**.
2. Añade un círculo básico: `Add > Mesh > Circle`. (Selecciona en el menú inferior izquierdo *Align a View* si quieres que nazca frente a ti).
3. Entra a **`Edit Mode`** (<kbd>Tab</kbd>). Aquí viene la parte divertida: darle forma.
   * **Para un controlador circular suave:** Puedes dejar el círculo tal como está.
   * **Para crear flechas (súper usadas en controladores IK de manos/pies):** Selecciona algunos vértices del círculo y bórralos (<kbd>X</kbd> > `Vertices`). Extruye (<kbd>E</kbd>) vértices simples para dibujar líneas que formen una cruz o una flecha.
   * *Importante:* Asegúrate de borrar cualquier cara interna (`Faces`); quieres que tu controlador sea **puro borde (Edges)** para que al ponerlo se vea como una guía transparente.
4. Vuelve a **`Object Mode`**, presiona <kbd>F2</kbd> y nómbralo de forma profesional. La regla en la industria es usar el sufijo `WGT_`: por ejemplo, `WGT_Control_Mano.L` (WGT significa *Widget*).
5. **Organización Ninja:** Selecciona tus formas creadas, presiona <kbd>M</kbd> y muévelas a una nueva Colección llamada `Rig_Shapes`. Luego, oculta esa colección desmarcando el "Ojo" en el *Outliner*. ¡Tus formas no necesitan ser vistas en el proyecto final, Blender solo robará su diseño!

### Paso 5.2: Asignar la Forma al Hueso
1. Selecciona tu **Armature** principal y entra en **`Pose Mode`** (<kbd>Ctrl</kbd> + <kbd>Tab</kbd>).
2. Selecciona el hueso que deseas modificar (por ejemplo, el *Controlador IK* de la mano).
3. Ve al panel de **`Bone Properties`** (el ícono del hueso verde a la derecha).
4. Desplázate hacia abajo hasta la sección **`Viewport Display`**.
5. Donde dice **`Custom Object`**, haz clic en el cuentagotas y selecciona la malla `WGT_Mano.L` que creaste.
6. ¡La forma mágica reemplazará al hueso! Usa las opciones que están justo debajo para ajustar su `Scale`, `Translation` (posición) y `Rotation` hasta que encaje perfecto con la mano.

> [!TIP]
> **Reutilización:** Puedes usar el mismo círculo o widget para diferentes huesos. Al ajustar la escala y traslación dentro de las propiedades del propio hueso (`Bone Properties`), la malla original `WGT` almacenada en tu colección no se verá afectada.

### Extra: Estandariza tus Diseños de Controladores 🎨
Para darle consistencia visual a tu Rig, la industria suele seguir la siguiente convención geométrica:

| Parte del Cuerpo | Tipo de Controlador "Custom Bone" Sugerido |
| :--- | :--- |
| **Raíz / Root** (El que mueve todo) | Círculo grande con flechas cardinales grandes en la base. |
| **IK de Manos y Pies** | Formas de cajas o cubos vacíos (Wireframe). |
| **Codos y Rodillas (Pole Targets)** | Círculos pequeños o simples estrellas de 4 puntas flotando en el espacio detrás/delante de la articulación. |
| **Huesos del Torso/Columna** | Círculos simples que abrazan la cintura/pecho. |
| **Huesos Faciales (Cejas, ojos)** | Cruces minúsculas o diminutos triángulos direccionales. |

---

## 6. Animación Final

<div align="center">
  <h3>¡Mira el resultado en acción! 🎥</h3>
  <img src="./animacion_small.gif" alt="Demostración de Animación Final en Blender">
</div>

---

## 7. Videos de Referencia (¡Más Recursos!)

Para una comprensión más visual y profunda, estos tutoriales son oro puro:

1.  **2D Cutout Animation in Blender (Completo):**
    *   [Ver en YouTube](https://www.youtube.com/watch?v=oqyW-i32W_0)
    *   Un clásico que cubre todo el proceso.

2.  **Blender 2D Rigging for Beginners (Ideal para empezar):**
    *   [Ver en YouTube](https://www.youtube.com/watch?v=JL87x9R3lYM)
    *   Claro, conciso y perfecto para principiantes.

3.  **Advanced 2D Rigging (Técnicas Pro):**
    *   [Ver en YouTube](https://www.youtube.com/watch?v=CQKQk0qw5W8)
    *   Explora conceptos más avanzados para llevar tu rig al siguiente nivel.

4.  **¡NUEVO! Rigging con IK en Blender para 2D:**
    *   [Ver en YouTube](https://www.youtube.com/watch?v=H9s51TbgKFI)
    *   Un excelente tutorial enfocado específicamente en la configuración de IK para personajes 2D.

5.  **¡NUEVO! Animación de Personajes 2D en Blender:**
    *   [Ver en YouTube](https://www.youtube.com/watch?v=CUrfA6MXU2E)
    *   Una vez que tu rig esté listo, este video te enseñará a darle vida.

---

## 8. Subir a GitHub

Mantén tu repositorio actualizado con tu increíble trabajo.

1.  **Añade, confirma y sube tus cambios:**
    ```bash
    # Navega a la carpeta de tu repositorio si no estás en ella
    cd Topicos-Avanzados-De-Programacion-Unidad-2
    
    # Añade todos los archivos nuevos o modificados
    git add .
    
    # Crea un commit con un mensaje descriptivo
    git commit -m "Tutorial de rigging 2D mejorado con IK y más recursos"
    
    # Sube los cambios a GitHub
    git push origin main
    ```

[↑ Volver al inicio](#-tutorial-completo-de-rigging-2d-en-blender-de-cero-a-héroe)

---

> ✨ **Documento elaborado para Tópicos Avanzados de Programación.** ¡Dale una estrella ⭐ al repositorio si te fue de utilidad!
