import streamlit as st

st.set_page_config(page_title="El Tutor de Silicio", layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>

html, body, [class*="css"]  {
    font-family: "Georgia", serif;
}

.title{
    font-size:60px;
    font-weight:700;
}

.subtitle{
    text-align:right;
    font-style:italic;
    font-size:20px;
    margin-top:-20px;
}

.section{
    height:80vh;
    display:flex;
    flex-direction:column;
    justify-content:center;
}

.header{
    font-size:40px;
    font-family:Arial, sans-serif;
    color:#6b3fa0;
    margin-bottom:30px;
}

.text{
    font-size:20px;
    line-height:1.7;
    max-width:900px;
}

.nav{
    display:flex;
    justify-content:center;
    gap:30px;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)


# ---------- CONTENIDO ----------
sections = [

{
"title":"Título",
"content":"""
<div class='title'>El Tutor de Silicio: ¿Puede la Inteligencia Artificial Entender el Alma del Estudiante?</div>
<div class='subtitle'>“En una era de máquinas dirigiendo humanos, ¿aún se necesita a los educadores?”</div>
"""
},

{
"title":"Introducción",
"content":"""
<div class='header'>Introducción</div>
<div class='text'>
Imagínese a un estudiante sentado frente a su ordenador a las dos de la mañana. 
Frustrado, murmura para sí mismo: "Nunca voy a entender esto, soy un desastre". 
En ese instante, una pequeña notificación aparece en pantalla.

No es un mensaje de un amigo despierto, sino una respuesta de un tutor inteligente 
que ha detectado ese tono de derrota y ofrece una palabra de aliento precisa para 
evitar que el desánimo gane la batalla.

Esta escena es hoy el núcleo de un debate fascinante en la psicología educativa. 
La Inteligencia Artificial ya no es solo una herramienta técnica, sino un sistema 
capaz de emular procesos cognitivos complejos.
</div>
"""
},

{
"title":"Sección 1",
"content":"""
<div class='header'>Un espejo que aprende a conocernos</div>
<div class='text'>
Los algoritmos actuales pueden analizar grandes cantidades de datos educativos y 
detectar patrones invisibles para los docentes humanos. Esto permite personalizar 
la enseñanza y adaptarla al ritmo de aprendizaje de cada estudiante.

Sin embargo, el paso de una educación estandarizada a una personalizada por 
algoritmos abre preguntas sobre la autonomía del estudiante y el nuevo rol del docente.
</div>
"""
},

{
"title":"Sección 2",
"content":"""
<div class='header'>La frialdad del dato frente al matiz del ensayo</div>
<div class='text'>
La inteligencia artificial puede evaluar con gran precisión preguntas cerradas 
y respuestas cortas. No obstante, cuando se trata de interpretar creatividad, 
ironía o pensamiento crítico en ensayos complejos, su desempeño se vuelve más limitado.

La máquina puede analizar estructuras del lenguaje, pero los humanos siguen siendo 
mejores interpretando matices y significados profundos.
</div>
"""
},

{
"title":"Sección 3",
"content":"""
<div class='header'>IA y bienestar emocional</div>
<div class='text'>
Existen sistemas capaces de detectar auto-habla negativa en estudiantes y responder 
con mensajes motivacionales. Aunque estas herramientas pueden apoyar el aprendizaje, 
no sustituyen la intervención de profesionales en salud mental.
</div>
"""
},

{
"title":"Sección 4",
"content":"""
<div class='header'>El dilema del algoritmo: ¿Aliado o vigilante?</div>
<div class='text'>
La implementación de IA en la educación requiere un contrato ético basado en 
transparencia, privacidad y control humano.

Sin regulaciones adecuadas, el uso de datos académicos podría convertir el aula 
en un espacio de vigilancia constante.
</div>
"""
},

{
"title":"Sección 5",
"content":"""
<div class='header'>El futuro: el toque humano en la era digital</div>
<div class='text'>
El modelo educativo emergente propone un sistema híbrido llamado 
human-in-the-loop: la máquina analiza y propone, pero el humano supervisa y decide.

El objetivo no es reemplazar a los docentes, sino potenciar la inteligencia humana.
</div>
"""
},

{
"title":"Ideas clave",
"content":"""
<div class='header'>Ideas Clave</div>
<div class='text'>
• La IA puede personalizar el aprendizaje analizando grandes volúmenes de datos.  
• Su desempeño es alto en tareas estructuradas, pero limitado en análisis subjetivo.  
• El uso ético requiere transparencia, privacidad y supervisión humana.  
• La educación del futuro probablemente será híbrida: humanos + IA.
</div>
"""
},

{
"title":"Cierre",
"content":"""
<div class='header'>Cierre</div>
<div class='text'>
La integración de la inteligencia artificial en la educación no es un destino 
final, sino un proceso continuo de adaptación.

La meta no es que las máquinas piensen como nosotros, sino que nos ayuden a 
pensar mejor y construir un aprendizaje más humano.
</div>
"""
}

]

# ---------- SESSION STATE ----------
if "page" not in st.session_state:
    st.session_state.page = 0


# ---------- MOSTRAR SECCIÓN ----------
current = sections[st.session_state.page]

st.markdown(f"<div class='section'>{current['content']}</div>", unsafe_allow_html=True)


# ---------- NAVEGACIÓN ----------
col1, col2, col3 = st.columns([1,2,1])

with col1:
    if st.session_state.page > 0:
        if st.button("⬅ Anterior"):
            st.session_state.page -= 1
            st.rerun()

with col3:
    if st.session_state.page < len(sections)-1:
        if st.button("Siguiente ➡"):
            st.session_state.page += 1
            st.rerun()


# ---------- REFERENCIAS ----------
if st.session_state.page == len(sections)-1:

    st.markdown("## Referencias")

    refs = {
        "Al-Zahrani (2024)":("https://doi.org/10.1016/j.heliyon.2024.e30696",
        "Analiza impactos negativos de la IA como aislamiento estudiantil y dependencia tecnológica."),
        
        "Azman & Tümkaya (2025)":("https://doi.org/10.12688/f1000research.160011.1",
        "Explica el potencial de tutorías personalizadas mediante IA y la necesidad de marcos éticos."),
        
        "Bako (2025)":("https://doi.org/10.30574/wjaets.2025.15.1.0262",
        "Discute el equilibrio entre automatización educativa y privacidad estudiantil."),
        
        "Eden et al. (2024)":("https://doi.org/10.30574/msarr.2024.10.2.0039",
        "Analiza oportunidades y desafíos éticos en la integración de IA educativa."),
        
        "Jukiewicz & Wyrwa (2026)":("https://doi.org/10.3390/app16020680",
        "Revisión de estudios sobre evaluación automatizada con modelos de lenguaje.")
    }

    for r in refs:
        with st.expander(r):
            st.write(refs[r][1])
            st.link_button("Abrir artículo", refs[r][0])
