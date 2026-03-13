import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="El Tutor de Silicio", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- ESTILOS CSS (UX/UI) ---
# Implementación de fuentes Serif para lectura y Sans-serif para títulos 
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Lora:ital,wght@0,400;0,700;1,400&display=swap');

    /* Contenedor principal sin scroll vertical infinito [cite: 101] */
    .main .block-container {
        max-width: 1000px;
        height: 80vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding-top: 2rem;
    }
    
    /* Tipografías */
    .titulo-grande { font-family: 'Inter', sans-serif; font-size: 3.5rem; font-weight: 700; line-height: 1.1; margin-bottom: 1rem; }
    .frase-motivadora { font-family: 'Inter', sans-serif; text-align: right; font-size: 1.2rem; font-style: italic; color: #555; }
    .subtitulo-morado { font-family: 'Inter', sans-serif; color: #6a0dad; font-weight: bold; font-size: 2rem; margin-bottom: 1.5rem; }
    .texto-cuerpo { font-family: 'Lora', serif; font-size: 1.25rem; line-height: 1.8; text-align: justify; }
    
    /* Botones de navegación */
    .stButton > button {
        border-radius: 20px;
        padding: 0.5rem 2.5rem;
        background-color: transparent;
        color: #1a1a1a;
        border: 1px solid #1a1a1a;
        transition: 0.3s ease;
    }
    .stButton > button:hover { background-color: #f0f0f0; border-color: #6a0dad; color: #6a0dad; }
    </style>
""", unsafe_allow_html=True)

# --- MANEJO DE ESTADO (NAVEGACIÓN) ---
if 'step' not in st.session_state:
    st.session_state.step = 0

def next_page(): st.session_state.step += 1
def prev_page(): st.session_state.step -= 1

# --- BASE DE DATOS DE REFERENCIAS (Modales) [cite: 139, 145] ---
referencias_db = {
    "Al-Zahrani (2024)": {
        "url": "https://doi.org/10.1016/j.heliyon.2024.e30696",
        "resumen": "Adoptando una perspectiva opuesta a las narrativas tecnológicamente optimistas, el estudio saca a la luz las 'sombras' o los impactos negativos implícitos de la IA en la educación."
    },
    "Azman & Tümkaya (2025)": {
        "url": "https://doi.org/10.12688/f1000research.160011.1",
        "resumen": "Resalta que su capacidad de crear tutorías personalizadas es prometedora, no obstante, requiere imperativamente de consejos de revisión ética y marcos regulatorios."
    },
    "Jukiewicz & Wyrwa (2026)": {
        "url": "https://doi.org/10.3390/app16020680",
        "resumen": "Revela que las inteligencias artificiales funcionan excelentemente en cuestionarios cortos, pero tambalean ante tareas complejas o altamente subjetivas."
    }
}

@st.dialog("Detalle de Referencia")
def modal_referencia(key):
    ref = referencias_db[key]
    st.write(f"**Resumen:** {ref['resumen']}")
    st.link_button("Ir al artículo original", ref["url"])

# --- RENDERIZADO DE SECCIONES ---
# Sección 0: Portada [cite: 92, 94]
if st.session_state.step == 0:
    st.markdown('<div class="titulo-grande">El Tutor de Silicio: ¿Puede la Inteligencia Artificial Entender el Alma del Estudiante?</div>', unsafe_allow_html=True)
    st.markdown('<div class="frase-motivadora">"En una era de máquinas dirigiendo humanos, ¿aún se necesita a los educadores?"</div>', unsafe_allow_html=True)

# Sección 1: Introducción [cite: 106, 109]
elif st.session_state.step == 1:
    st.markdown('<div class="subtitulo-morado">Introducción</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="texto-cuerpo">Imagínese a un estudiante sentado frente a su ordenador a las dos de la mañana... una respuesta de un tutor inteligente ha detectado ese tono de derrota y ofrece una palabra de aliento precisa. [cite: 107, 109]</div>', unsafe_allow_html=True)

# Sección 2: Punto 1 - Un espejo que aprende a conocernos [cite: 112, 116]
elif st.session_state.step == 2:
    st.markdown('<div class="subtitulo-morado">Un espejo que aprende a conocernos</div>', unsafe_allow_html=True)
    st.markdown('<div class="texto-cuerpo">En el corazón de esta revolución se encuentra la capacidad de los algoritmos para procesar el "Big Data"... La IA puede identificar patrones de estudio que para un profesor humano serían invisibles. [cite: 113, 115]</div>', unsafe_allow_html=True)

# Sección 3: Punto 2 - La frialdad del dato [cite: 120, 125]
elif st.session_state.step == 3:
    st.markdown('<div class="subtitulo-morado">La frialdad del dato frente al matiz del ensayo</div>', unsafe_allow_html=True)
    st.markdown('<div class="texto-cuerpo">¿Podría una máquina calificar tus exámenes mejor que un profesor? Investigaciones revelan que ChatGPT es preciso en respuestas cortas, pero carece de la "piel" necesaria para captar la ironía. [cite: 121, 124]</div>', unsafe_allow_html=True)

# Sección 4: Punto 3 - Dilema del algoritmo [cite: 128, 132]
elif st.session_state.step == 4:
    st.markdown('<div class="subtitulo-morado">El dilema del algoritmo: ¿Aliado o vigilante?</div>', unsafe_allow_html=True)
    st.markdown('<div class="texto-cuerpo">Existen principios que no podemos negociar: transparencia, privacidad y control humano... la recolección constante de datos podría convertir la escuela en un entorno de vigilancia. [cite: 130, 131]</div>', unsafe_allow_html=True)

# Sección 5: Punto 4 - El futuro [cite: 133, 138]
elif st.session_state.step == 5:
    st.markdown('<div class="subtitulo-morado">El futuro: El toque humano en la era digital</div>', unsafe_allow_html=True)
    st.markdown('<div class="texto-cuerpo">La síntesis apunta hacia un modelo de "IA ética" donde la máquina propone, pero el humano supervisa y decide (human-in-the-loop). [cite: 135, 136]</div>', unsafe_allow_html=True)

# Sección 6: Referencias Interactivas [cite: 141, 142]
elif st.session_state.step == 6:
    st.markdown('<div class="subtitulo-morado">Referencias</div>', unsafe_allow_html=True)
    st.write("Seleccione un artículo para ver su resumen y enlace:")
    for ref_key in referencias_db.keys():
        if st.button(f"📄 {ref_key}"):
            modal_referencia(ref_key)

# --- CONTROLES DE NAVEGACIÓN (Centrados en la parte inferior) [cite: 103] ---
st.write("---")
nav_cols = st.columns([1, 1, 1])
with nav_cols[0]:
    if st.session_state.step > 0:
        st.button("← Anterior", on_click=prev_page)
with nav_cols[2]:
    if st.session_state.step < 6: # Total de secciones
        st.button("Siguiente →", on_click=next_page)
