# Vibe Coding para Profesionales de la Salud
## Programa para Principiantes — Crear Herramientas Útiles con IA (Sin Saber Programar)

*Para personal clínico, de enfermería, administrativo y de salud afín, con experiencia técnica mínima.*
*Última actualización: junio de 2026.*

---

## De Qué Trata Este Curso

**"Vibe coding"** significa crear software funcional *describiendo en lenguaje cotidiano lo que quieres* y dejando que una IA escriba el código. No aprendes un lenguaje de programación: aprendes a **describir, probar y refinar**. El término surgió a principios de 2025 y, desde entonces, las herramientas para principiantes han mejorado muchísimo.

**La promesa:** Puedes crear una app pequeña —un cuestionario educativo para pacientes, una lista de verificación para el cambio de turno, un generador de borradores de cartas de derivación, una herramienta de consulta de códigos— en una tarde.

**La advertencia honesta (léela dos veces):** las apps generadas por IA *no* son automáticamente seguras ni privadas. En el ámbito de la salud, eso importa muchísimo. Este programa te enseña a construir **y** a conocer tus límites, sobre todo la regla estricta sobre los datos de pacientes, que tiene su propio módulo.

**Dedicación:** ~6 a 8 semanas, unas pocas horas por semana. Cada módulo = conceptos + una mini-práctica.

**Al finalizar podrás:**

- Explicar qué es y qué no es el vibe coding.
- Elegir la herramienta adecuada para cada idea.
- Crear, probar y publicar una app sencilla, útil y sin datos de pacientes (PHI).
- Aplicar una regla clara de seguridad de datos cada vez.
- Saber exactamente cuándo detenerte y llamar a TI, cumplimiento o a un desarrollador.

---

## Para Quién Es (y Para Quién No)

**Es para ti si:** trabajas en salud, tienes una idea de herramienta que te ahorraría tiempo y poca o nula experiencia técnica.

**Todavía NO es para:** crear algo que almacene, muestre o transmita información **real** de pacientes. Eso requiere a los equipos de TI, seguridad y cumplimiento de tu organización; este curso te enseña a reconocer ese límite, no a cruzarlo por tu cuenta.

---

## Las 5 Reglas del Curso (Cuélgalas a la Vista)

1. **Nunca** ingreses información real de pacientes (PHI) en ninguna herramienta de IA: ni en una instrucción, ni "solo para probar".
2. Usa **datos falsos / de ejemplo** para todo lo que construyas.
3. Construye en la **"zona verde"**: educación, referencias públicas, tareas administrativas personales, demos con datos ficticios.
4. **Un cambio a la vez**, y luego prueba: así aprendes qué funciona.
5. Cuando haya datos reales de pacientes, **detente y escala** a TI/cumplimiento.

---

## Módulo 0 — Fundamentos (Antes de Construir Nada)

**Objetivo:** Hablar el idioma; entender qué ocurre realmente.

- Qué es de verdad una "app", una "app web" y "la nube", en palabras simples.
- Qué es un modelo de IA (LLM) y por qué a veces se equivoca ("alucina").
- El ciclo del vibe coding: **Describir → Generar → Probar → Refinar → Repetir.**
- Vocabulario básico: *prompt (instrucción), publicar/desplegar, frontend / backend, base de datos, alojamiento, repositorio.*
- Cambio de mentalidad: eres el **diseñador del producto y quien lo prueba**, no quien teclea código.

**Mini-tarea:** Escribe un párrafo que describa una herramienta que desearías tener en tu trabajo. Ese párrafo es tu primer "prompt".

---

## Módulo 1 — Tu Caja de Herramientas (El Panorama Actual)

**Objetivo:** Saber qué herramienta elegir y por qué. Si no programas, elige un **constructor de apps con IA** (te crea la app completa), no un "asistente de programación" (supone que ya sabes programar).

| Herramienta | Mejor para | Por qué la elige un principiante |
|---|---|---|
| **Lovable** (~25 USD/mes) | La mejor opción general para no programadores | Describes una app y obtienes una app funcional: sin terminal, sin instalaciones, alojamiento automático. La mejor valoración para principiantes. |
| **Replit** | Cuando creces más allá de tu primera app | Editor, agente de IA, alojamiento e historial de versiones en una sola pestaña del navegador. |
| **Bolt.new** | Prototipos rápidos | Muy rápido, en el navegador, fácil para principiantes. |
| **ChatGPT / Claude** | Planificar, redactar prompts, explicar errores | Tu "compañero de ideas" junto al constructor. Úsalo para planificar *antes* de construir. |

**Cómo elegir:** Empieza con **Lovable** en tu primera app. Suma **ChatGPT o Claude** (tienen versiones gratuitas) como apoyo para redactar mejores prompts y descifrar mensajes de error.

**Mini-tarea:** Crea una cuenta de prueba en un constructor, construye el ejemplo inicial de la plataforma y haz clic en **Publicar** para ver un enlace en vivo.

---

## Módulo 2 — Tu Primera App Real (Práctica)

**Objetivo:** Llevar una idea de una frase a una app con la que se puede interactuar. *(Esta es la lección de la Semana 1; consulta el documento complementario "Semana 1 — Lección Completa").*

- Convertir una idea en una solicitud clara y específica (la especificidad gana a la astucia).
- Generar la versión 1 y luego **probar con ojo crítico**: haz clic en todo, intenta romperla.
- Refinar en pasos pequeños ("agranda el botón", "agrega una segunda pregunta").
- Publicar y compartir un enlace para recibir comentarios.

**Primeras prácticas seguras (sin datos de pacientes):**

- Una **calculadora de referencia** de dosis (fórmulas públicas).
- Un **cuestionario** educativo sobre una afección común.
- Una **app de lista de verificación** para un flujo de trabajo recurrente (preparación de sala, pasos de admisión).

**Mini-tarea:** Publica una de las anteriores y comparte el enlace con un colega.

---

## Módulo 3 — El Módulo de Seguridad en Salud (La Parte Más Importante)

**Objetivo:** Construir con responsabilidad. Aquí la salud se diferencia de todos los demás campos.

**La Regla de Oro:** **Nunca** ingreses información real de pacientes en una herramienta de vibe coding —ni en un prompt, ni en una prueba, ni "solo por esta vez"—. Usa únicamente datos falsos.

**Por qué — riesgos documentados de las apps de salud generadas por IA:**

- **Sin cifrado por defecto** — el código de IA suele guardar los datos como texto legible salvo que exijas cifrado explícitamente.
- **Puertas abiertas** — los backends generados por IA con frecuencia dejan los datos accesibles sin inicios de sesión ni permisos adecuados.
- **Sin registro de auditoría** — HIPAA exige rastrear quién vio qué; la IA rara vez lo construye sin que se lo pidas.
- **El problema del BAA** — manejar PHI real suele requerir un *Acuerdo de Asociado Comercial (BAA)* firmado. La mayoría de las herramientas de vibe coding **no lo ofrecen**, así que usarlas con PHI real puede ser, en sí mismo, una infracción.

**Qué harás en su lugar:**

- Clasifica cada idea: **(A)** Sin datos de pacientes → construye libremente. **(B)** Toca datos de pacientes → detente e involucra a TI/cumplimiento.
- Mantén tus proyectos personales en la **zona verde**.
- Reconoce el punto en que un proyecto se vuelve un esfuerzo oficial de TI/cumplimiento/legal.

**Mini-tarea:** Escribe tu chequeo de seguridad en una línea: *"¿Esto toca información real de pacientes? Si la respuesta es sí → detente y escala."*

---

## Módulo 4 — Proyectos Prácticos para el Día a Día

**Objetivo:** Aplicar lo aprendido a necesidades reales (pero seguras). Elige proyectos según tu rol.

- **Eficiencia del flujo de trabajo:** listas de verificación inteligentes, plantillas de cambio de turno, control de salas/equipos (sin PHI).
- **Aprendizaje y enseñanza:** apps de tarjetas de memoria, cuestionarios sobre guías clínicas, explicadores para pacientes, herramientas de *estudio* de interacciones farmacológicas (datos públicos).
- **Administrativo:** resúmenes de notas de reuniones, planificadores de horarios, generadores de borradores de cartas con nombres **ficticios**, control de inventario.
- **Productividad personal:** un registro de educación médica continua, un organizador de club de revistas, un planificador de congresos.

**Mini-tarea:** Crea una herramienta que te ahorre ≥10 minutos por turno.

---

## Módulo 5 — Habilidades de Prompting e Iteración (El Verdadero Oficio)

**Objetivo:** Obtener mejores resultados de cualquier herramienta.

- **Sé específico:** quién la usa, qué hace, cómo se ve, qué hace cada botón.
- **Un cambio a la vez** para saber qué funcionó.
- **Describe el problema, no la solución:** "Cuando hago clic en Guardar, no pasa nada" es mejor que intentar adivinar el código.
- Usa ChatGPT/Claude para **planificar primero** y luego pega el plan en tu constructor.
- Mantén una "biblioteca de prompts" personal con las frases que funcionaron.

**Mini-tarea:** Mejora un proyecto anterior con tres prompts de refinamiento precisos.

---

## Módulo 6 — Conocer Tus Límites y Cuándo Pedir Ayuda

**Objetivo:** Ser quien innova *de forma segura*.

- La diferencia entre una **herramienta de ayuda personal** y un **sistema clínico/de producción** (este último siempre necesita profesionales).
- Señales de alerta que significan "llama a TI/cumplimiento/un desarrollador": datos reales de pacientes; algo de lo que otros dependen para decisiones clínicas; algo que se conecta a sistemas hospitalarios.
- Cómo presentar un prototipo de vibe coding a tu equipo de TI/innovación como un *punto de partida*, no un producto terminado.
- La realidad del mantenimiento: ¿quién lo arregla cuando se rompe?

**Mini-tarea:** Escribe una breve "nota de entrega" que describa un prototipo como si lo propusieras a TI.

---

## Proyecto Final

Crea, publica y presenta **una herramienta pulida y sin PHI** que mejore tu trabajo diario. Entregables:

1. Un enlace en vivo para compartir.
2. Una demostración de 2 minutos para un colega.
3. Un chequeo de seguridad de datos por escrito que confirme que no hay información de pacientes.
4. Una breve reflexión: qué te ahorra y qué haría falta para usarla "de verdad".

---

## Glosario de Referencia Rápida

- **Prompt** — tu instrucción en lenguaje cotidiano para la IA.
- **Publicar / Desplegar** — poner tu app en vivo en internet.
- **PHI** — Información de Salud Protegida (datos reales de pacientes).
- **BAA** — Acuerdo de Asociado Comercial (contrato legal requerido para manejar PHI).
- **Alucinación** — cuando la IA produce algo incorrecto con total seguridad.
- **Frontend / Backend** — lo que ve el usuario / el motor que está por detrás.
- **Iterar** — mejorar en pasos pequeños y probados.

---

## Fuentes y Lecturas Adicionales

**Herramientas y panorama**

- Best Vibe Coding Tools 2026 — TechRadar: https://www.techradar.com/pro/best-vibe-coding-tools
- Best Vibe Coding Tools for Non-Coders — Medium/Predict: https://medium.com/predict/best-vibe-coding-tools-2026-for-non-coders-8ce9d18443bf
- Best Vibe Coding Tools for Beginners 2026 — Rocket Blog: https://www.rocket.new/blog/best-vibe-coding-tools

**Seguridad en salud y HIPAA**

- HIPAA-Compliant AI Tools for Vibe-Coded Healthcare Apps — Knack: https://www.knack.com/blog/hipaa-compliant-ai-tools-vibe-coded-apps/
- What Nobody Tells You About PHI & HIPAA — Specode: https://www.specode.ai/blog/phi-hipaa-vibe-coded-healthcare-app
- Why Healthcare Vibe Coding Needs Oversight in 2026 — Japeto Labs: https://www.japeto.ai/why-healthcare-vibe-coding-needs-oversight-in-2026/
- The Risks of Vibe Coding — Retool: https://retool.com/blog/vibe-coding-risks

---

*Este programa es educativo. No constituye asesoramiento legal ni de cumplimiento. Sigue siempre las políticas de tu propia organización antes de construir algo que pueda tocar datos de pacientes.*
