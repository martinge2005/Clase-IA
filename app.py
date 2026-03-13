import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="El Tutor de Silicio", layout="wide", initial_sidebar_state="collapsed")

# --- ESTILOS CSS PERSONALIZADOS (UI/UX) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700&family=Lora:ital,wght@0,400;0,700;1,400&display=swap');

    /* Forzar Viewport 100% y ocultar scroll general */
    .main .block-container {
        max-width: 900px;
        padding-top: 5rem;
        padding-bottom: 5rem;
    }
    
    /* Tipografías */
    h1, h2, h3 { font-family: 'Inter', sans-serif !important; font-weight: 700; color: #1a1a1a; }
    p, li { font-family: 'Lora', serif !important; font-size: 1.2rem; line-height: 1.6; color: #333; }
    
    .quote-text { text-align: right; font-style: italic; color: #666; margin-bottom: 2rem; }
    
    /* Botones de navegación */
    .stButton > button {
        border-radius: 50px;
        padding: 0.5rem 2rem;
        border: 1px solid #ddd;
        background-color: white;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        border-color: #1a1a1a;
        background-color: #f9f9f9;
    }
    </style>
""", unsafe_allow_html=True)

# --- ESTADO DE LA SESIÓN (Navegación) ---
if 'step' not in st.session_state:
    st.session_state.step = 0

def next_step(): st.session_state.step += 1
def prev_step(): st.session_state.step -= 1

# --- BASE DE DATOS DE REFERENCIAS ---
referencias = {
    "Al-Zahrani (2024)": {
        "titulo": "Unveiling the shadows: Beyond the hype of AI in education",
        "link": "https://doi.org/10.1016/j.heliyon.2024.e30696",
        "resumen": "Adopta una perspectiva opuesta a las narrativas optimistas, revelando impactos negativos como el aislamiento estudiantil y pérdida de pensamiento crítico."
    },
    "Azman & Tümkaya (2025)": {
        "titulo": "Navigating the ethical landscape of AI integration in education",
        "link": "https://doi.org/10.12688/f1000research.160011.1",
        "resumen": "Resalta la capacidad de crear tutorías personalizadas pero subraya la necesidad de marcos regulatorios y ética escolar."
    },
    "Jukiewicz & Wyrwa (2026)": {
        "titulo": "Can ChatGPT replace the teacher in assessment?",
        "link": "https://doi.org/10.3390/app16020680",
        "resumen": "Determina que la IA es excelente en cuestionarios cortos, pero falla en tareas complejas o subjetivas."
    }
}

@st.dialog("Referencia Bibliográfica")
def mostrar_referencia(ref_key):
    ref = referencias[ref_key]
    st.subheader(ref["titulo"])
    st.write(f"**Resumen:** {ref['resumen']}")
    st.link_button("Ver artículo completo", ref["link"])

# --- LÓGICA DE SECCIONES ---
secciones = [
    "Portada", "Introducción", "Punto 1: El Espejo", "Punto 2: Evaluación", 
    "Punto 3: Bienestar", "Punto 4: Ética", "Punto 5: El Futuro", "Referencias"
]

# --- RENDERIZADO DE CONTENIDO ---
content_area = st.container()

with content_area:
    if st.session_state.step == 0: # PORTADA
        st.markdown('<p class="quote-text">"En una era de máquinas dirigiendo humanos, ¿aún se necesita a los educadores?"</p>', unsafe_allow_html=True)
        st.title("El Tutor de Silicio: ¿Puede la Inteligencia Artificial Entender el Alma del Estudiante?")
        st.caption("Un artículo de divulgación sobre IA y Psicología Educativa")

    elif st.session_state.step == 1: # INTRODUCCIÓN
        st.header("La Notificación a las 2:00 AM")
        st.write("Imagínese a un estudiante frustrado frente a su ordenador. En ese instante, una pequeña notificación aparece... no es un amigo, es un tutor inteligente que ha detectado su derrota.")
        st.write("Esta escena es hoy el núcleo de un debate fascinante en la psicología educativa.")

    elif st.session_state.step == 2: # PUNTO 1
        st.header("Un espejo que aprende a conocernos")
        st.write("La IA puede identificar patrones de estudio que para un profesor humano serían invisibles. Como explican Azman y Tümkaya (2025), es una oportunidad para personalizar el aprendizaje.")
        if st.button("Ver Referencia: Azman & Tümkaya"): mostrar_referencia("Azman & Tümkaya (2025)")

    elif st.session_state.step == 3: # PUNTO 2
        st.header("La frialdad del dato frente al matiz")
        st.write("¿Podría una máquina calificar tus exámenes? Según Jukiewicz y Wyrwa (2026), la respuesta es un 'sí' a medias. La IA es impecable en reglas rígidas, pero carece de 'piel' para captar la ironía.")
        if st.button("Ver Referencia: Jukiewicz & Wyrwa"): mostrar_referencia("Jukiewicz & Wyrwa (2026)")

    elif st.session_state.step == 7: # REFERENCIAS FINAL
        st.header("Referencias Interactivas")
        st.write("Haga clic en cada autor para ver el resumen y el enlace original:")
        for r in referencias:
            if st.button(f"📖 {r}"): mostrar_referencia(r)

# --- BARRA DE NAVEGACIÓN (Sticky bottom) ---
st.markdown("---")
cols = st.columns([1, 2, 1])
with cols[0]:
    if st.session_state.step > 0:
        st.button("← Anterior", on_click=prev_step)
with cols[2]:
    if st.session_state.step < len(secciones) - 1:
        st.button("Siguiente →", on_click=next_step)
with cols[1]:
    st.write(f"<p style='text-align:center; font-size:0.8rem;'>Sección {st.session_state.step + 1} de {len(secciones)}</p>", unsafe_allow_html=True)
