# Semana 1 — Lección Completa
## "Crea Tu Primera App de una Sola Sentada" — Un Cuestionario Educativo para Pacientes

*Una lección completa, paso a paso, para principiantes absolutos. Sin programar. Sin datos de pacientes.*
*Complemento del programa Vibe Coding para Profesionales de la Salud.*

---

> **Nota sobre las capturas de pantalla:** Los recuadros marcados como **[PANTALLA]** más abajo son *maquetas descritas* de lo que verás —dibujadas en texto para que sigan siendo precisas aunque las herramientas cambien su apariencia—. Las apps reales cambian a menudo sus botones y colores; lo que debes buscar son las *etiquetas y acciones* descritas aquí. Cuando el texto difiera un poco, elige el botón más parecido.

---

## La Lección de un Vistazo

- **Objetivo:** Crear y publicar en vivo un cuestionario educativo "Diabetes Básica" para pacientes.
- **Tiempo:** 60 a 90 minutos.
- **Herramienta:** Lovable (sin instalación, funciona en tu navegador web).
- **Costo:** La prueba gratuita basta para completar esta lección.
- **Te llevarás:** Un enlace web real que puedes abrir en tu teléfono y compartir.
- **Seguridad de datos:** Cero datos de pacientes. Todo aquí es contenido público de educación en salud.

### Qué necesitas

- Una laptop o computadora de escritorio con navegador web (Chrome, Edge o Safari).
- Una dirección de correo electrónico.
- 90 minutos tranquilos.

---

## Parte 0 — El Chequeo de Seguridad (2 minutos, siempre)

Antes de *cualquier* construcción, di esto en voz alta:

> **"¿Esta herramienta toca información real de pacientes?"**
> Nuestro cuestionario usa **datos públicos generales de salud** sobre la diabetes. **Sin nombres de pacientes, sin expedientes, sin PHI.** ✅ Seguro para construir.

Si alguna vez la respuesta es "sí, toca datos reales de pacientes", te **detienes** y hablas con TI/cumplimiento. En esta lección estamos firmemente en la **zona verde**.

---

## Parte 1 — Crea Tu Cuenta (5 minutos)

**Paso 1.** Abre tu navegador y entra a **lovable.dev**.

**Paso 2.** Haz clic en **Sign up** (Registrarse, arriba a la derecha). Usa tu correo o "Continuar con Google".

```
[PANTALLA] — Página de inicio de Lovable
+------------------------------------------------------+
|  Lovable                  [ Iniciar sesión ][Registrarse]|
|                                                      |
|     Crea algo Lovable                                |
|     Describe tu idea. Obtén una app funcional.       |
|                                                      |
|     [  Describe lo que quieres construir...      ]   |
|     [                              ( ↑ Enviar )  ]   |
+------------------------------------------------------+
```

**Paso 3.** Confirma tu correo si te lo piden. Llegarás a un gran cuadro de texto que dice algo como *"Describe lo que quieres construir."* Ese cuadro es donde ocurre la magia.

> 🧑‍🏫 **Guion de enseñanza:** "¿Ven ese único cuadro de texto? Ese es todo el 'lenguaje de programación' que necesitamos hoy: español claro. Vamos a escribir una descripción y la IA construye la app. Si puedes escribir una hoja de indicaciones para un paciente, puedes hacer esto."

---

## Parte 2 — Planifica Antes de Construir (10 minutos)

Las buenas construcciones empiezan con una solicitud clara. Escribiremos nuestra descripción en tres partes simples.

**La receta de 3 partes para el prompt de cualquier app:**

1. **Qué es** — una oración.
2. **Qué contiene** — las piezas/el contenido.
3. **Cómo se ve y se comporta** — estilo y botones.

Este es nuestro plan terminado para el cuestionario. **No lo escribas todavía**, solo léelo:

> **Qué es:** Una app sencilla de cuestionario educativo para pacientes llamada "Diabetes Básica".
>
> **Qué contiene:** Una pantalla de bienvenida con un botón "Comenzar cuestionario", luego 5 preguntas de opción múltiple (una a la vez) sobre diabetes tipo 2, cada una con 3 opciones de respuesta. Después de cada respuesta, mostrar si fue correcta y una explicación de una oración. Al final, mostrar el puntaje sobre 5 y un botón "Intentar de nuevo".
>
> **Cómo se ve y se comporta:** Limpia y amigable, texto grande y legible, colores tranquilos en azul y blanco, botones grandes adecuados para pacientes mayores. Compatible con teléfonos móviles.

> 🧑‍🏫 **Guion de enseñanza:** "Fíjense que nunca dijimos *cómo* construirla, ni una palabra de código. Describimos la *experiencia* que tendría un paciente. Esa es toda la habilidad."

---

## Parte 3 — Genera la Versión 1 (10 minutos)

**Paso 4.** Haz clic en el cuadro de texto grande. Copia el **guion de prompt** de abajo y pégalo.

### ⌨️ Guion de Prompt #1 — La Primera Construcción

```
Crea una app web sencilla de cuestionario educativo para pacientes llamada "Diabetes Básica".

Contenido:
- Una pantalla de bienvenida con el título, una frase amigable y un botón grande "Comenzar cuestionario".
- 5 preguntas de opción múltiple sobre diabetes tipo 2, mostradas de una en una.
- Cada pregunta tiene 3 opciones de respuesta.
- Después de que el usuario elija una respuesta, mostrar si fue correcta y una explicación de una oración.
- Un botón "Siguiente" pasa a la próxima pregunta.
- Al final, mostrar el puntaje sobre 5 y un botón "Intentar de nuevo" que reinicia el cuestionario.

Estilo:
- Limpio, amigable y tranquilo. Colores azul y blanco.
- Texto grande y fácil de leer, y botones grandes, adecuados para adultos mayores.
- Que funcione bien en la pantalla de un teléfono.

Usa datos de educación en salud públicos, generales y precisos sobre la diabetes tipo 2.
No incluyas ninguna información real de pacientes.
```

**Paso 5.** Presiona **Enviar** (la flecha / botón "Enviar"). Ahora espera: la IA escribe la app mientras observas.

```
[PANTALLA] — Construyendo
+-------------------------+----------------------------+
|  Chat (tus mensajes)    |   Vista previa en vivo     |
|                         |                            |
|  Tú: Crea una app...    |   ⏳ Generando tu app...   |
|                         |   • creando bienvenida     |
|  Lovable: Trabajando    |   • agregando 5 preguntas  |
|  ✓ Bienvenida creada    |   • aplicando estilo       |
|  ✓ Preguntas agregadas  |                            |
|  ✓ Puntaje agregado     |   [ aquí aparece la vista ]|
+-------------------------+----------------------------+
```

**Paso 6.** En 1 a 3 minutos aparece una app funcional en la **Vista previa en vivo** de la derecha. Haz clic en **Comenzar cuestionario** y pruébala.

> 🧑‍🏫 **Guion de enseñanza:** "Felicidades: acabas de crear software. No te preocupes si no es perfecto. Las primeras versiones nunca lo son. Nuestro verdadero trabajo empieza ahora: probar y refinar."

---

## Parte 4 — Prueba con Ojo Crítico (10 minutos)

Tu trabajo es *intentar romperla.* Haz clic en todo. Usa esta lista:

**✅ Lista de Pruebas de la Semana 1**

- [ ] ¿**Comenzar cuestionario** abre la primera pregunta?
- [ ] ¿Están las **5 preguntas**?
- [ ] ¿Cada pregunta tiene **3 opciones**?
- [ ] Al elegir una respuesta, ¿me dice si es **correcta o incorrecta**?
- [ ] ¿Hay una **explicación de una oración** tras cada respuesta?
- [ ] ¿**Siguiente** avanza siempre?
- [ ] Al final, ¿hay un **puntaje sobre 5**?
- [ ] ¿**Intentar de nuevo** reinicia desde el principio?
- [ ] En una **ventana angosta** (arrástrala fina como un teléfono), ¿el texto sigue cabiendo?

Anota todo lo que esté mal o feo. Cada punto se convierte en un refinamiento en la Parte 5.

> 🧑‍🏫 **Guion de enseñanza:** "Quien prueba no es pesimista: es el defensor del paciente. Si un clic confuso es posible, un paciente real lo encontrará. Anótalo; lo arreglaremos."

---

## Parte 5 — Refina en Pasos Pequeños (15 minutos)

Ahora mejoramos la app **un cambio a la vez**, escribiendo cada solicitud en el mismo cuadro de chat. Tras cada uno, la vista previa se actualiza: vuelve a probar antes del siguiente cambio.

### ⌨️ Guiones de Prompt — Refinamientos Iniciales Comunes

Usa solo los que realmente necesites:

**Agrandar el texto / hacerlo más amigable:**
```
Agranda todo el texto y añade más espacio entre los botones,
para que sea cómodo de leer y tocar para adultos mayores.
```

**Agregar un indicador de progreso:**
```
En la parte superior de cada pregunta, muestra "Pregunta 2 de 5"
para que los usuarios sepan cuánto avanzaron.
```

**Mejorar el final:**
```
En la pantalla final de puntaje, agrega un mensaje de aliento:
si el puntaje es 4 o 5, di "¡Excelente trabajo!"; si es 3 o menos,
di "Buen comienzo: repasa e inténtalo de nuevo". Mantén el botón "Intentar de nuevo".
```

**Corregir un error específico (ejemplo):**
```
Cuando hago clic en "Siguiente" en la pregunta 3, no pasa nada.
Por favor, haz que el botón "Siguiente" avance a la próxima pregunta siempre.
```

> 🧑‍🏫 **Guion de enseñanza — el hábito #1:** "Un cambio, luego prueba. Si pides cinco cosas a la vez y algo se rompe, no sabrás cuál fue. Lento es suave, y suave es rápido."

> 💡 **Regla de oro para reportar errores:** Describe **qué pasó**, no cómo arreglarlo. "Cuando hago clic en Guardar, no pasa nada" le da a la IA todo lo que necesita. No tienes que saber la solución.

---

## Parte 6 — Publícala (10 minutos)

**Paso 7.** Busca el botón **Publicar** (o **Desplegar**), normalmente arriba a la derecha.

```
[PANTALLA] — Barra superior
+------------------------------------------------------+
|  Diabetes Básica          [ Compartir ] [ Publicar ▸ ]|
+------------------------------------------------------+
```

**Paso 8.** Haz clic en **Publicar**. Tras unos segundos obtendrás un **enlace en vivo** como `diabetes-basica.lovable.app`.

**Paso 9.** Abre ese enlace en tu **teléfono**. Ya es una app real, en vivo, en internet.

**Paso 10.** Envía el enlace a un colega de confianza y pregúntale: *"¿Esto ayudaría a un paciente recién diagnosticado? ¿Qué resulta confuso?"*

> 🧑‍🏫 **Guion de enseñanza:** "Ese enlace funciona en cualquier teléfono, en cualquier lugar, y no instalaste nada. Este es el momento en que la mayoría se da cuenta de que sí puede hacerlo."

---

## Parte 7 — Cierre y Tarea (5 minutos)

**Lo lograste.** Planificaste, construiste, probaste, refinaste y publicaste una app real, sin código y sin datos de pacientes.

### 📋 Tarea para la próxima sesión

1. **Vuelve a probar** tu cuestionario publicado en un teléfono y arregla **una** cosa que no te guste (un prompt pequeño).
2. **Escribe un plan** (la receta de 3 partes) para una herramienta que *tú* quieras: una lista de verificación, una calculadora, un juego de tarjetas. No la construyas todavía; solo escribe la descripción.
3. **Inicia tu Biblioteca de Prompts:** abre un archivo de notas y pega cualquier prompt que haya funcionado bien hoy.

### ✅ Autoevaluación: ¿cumpliste los objetivos?

- [ ] Creé una cuenta y encontré el cuadro de "describe tu app".
- [ ] Escribí un plan claro de 3 partes.
- [ ] Generé una primera versión funcional.
- [ ] La probé con la lista de verificación.
- [ ] Hice al menos un refinamiento, un cambio a la vez.
- [ ] La publiqué y abrí el enlace en vivo en mi teléfono.
- [ ] Confirmé: **ningún dato real de pacientes** en ningún lugar. ✅

---

## Solución Rápida de Problemas

| Problema | Qué hacer |
|---|---|
| La app no se generó / dio error | Vuelve a hacer clic en Enviar, o pega: *"Eso no funcionó. Por favor, intenta construir el cuestionario de nuevo."* |
| Un botón no hace nada | Dile a la IA exactamente: *"Cuando hago clic en X, no pasa nada. Por favor, haz que X haga Y."* |
| Se ve apretado en el teléfono | Pega: *"Hazlo compatible con móviles, con texto y espaciado más grandes."* |
| Cambió algo que me gustaba | Pega: *"Deshaz el último cambio y vuelve a como estaba antes."* |
| Se me acabaron los créditos gratis | Puedes detenerte aquí; tu enlace publicado sigue funcionando. Mejorar el plan es opcional. |

---

## Notas para Quien Enseña Esta Lección

- **Tamaño del grupo:** Funciona de 1 a 1 o hasta ~12 personas con un ayudante que circule.
- **Preparación previa:** Pide a los participantes crear la cuenta *antes* de la clase para ahorrar 5 minutos.
- **La única regla a recalcar:** el chequeo de seguridad de datos de la Parte 0. Repítelo al inicio y al final.
- **Tropiezo común:** los participantes intentan arreglar las cosas ellos mismos en lugar de *describir el problema*. Reencáuzalos hacia "describe qué pasó".
- **Si alguien termina antes:** que agregue una 6.ª pregunta, o que cambie el estilo con el prompt *"Dale un aspecto más cálido y tranquilizador."*
- **Ahorro de tiempo:** mantén el Guion de Prompt #1 en un volante o documento compartido para que nadie tenga que volver a teclearlo.

---

*Esta lección es educativa y usa únicamente contenido público de educación en salud. No constituye asesoramiento legal ni de cumplimiento. Nunca ingreses información real de pacientes en herramientas de IA y sigue las políticas de tu organización.*
