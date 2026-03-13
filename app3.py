import streamlit as st

st.set_page_config(page_title="El Tutor de Silicio", layout="wide")

# ---------- ESTILOS ----------
st.markdown("""
<style>

html, body {
    font-family: "Georgia", serif;
}

.title{
    font-size:55px;
    font-weight:700;
}

.subtitle{
    text-align:right;
    font-style:italic;
    font-size:20px;
    margin-top:-15px;
}

.header{
    font-size:38px;
    color:#6b3fa0;
    margin-top:30px;
    font-family:Arial, sans-serif;
}

.text{
    font-size:20px;
    line-height:1.7;
    max-width:900px;
}

</style>
""", unsafe_allow_html=True)


# ---------- ÍNDICE LATERAL ----------
st.sidebar.title("Índice")

section = st.sidebar.radio(
    "",
    [
        "Título",
        "Introducción",
        "Un espejo que aprende a conocernos",
        "La frialdad del dato frente al matiz del ensayo",
        "El dilema del algoritmo",
        "El futuro",
        "Referencias"
    ]
)


# ---------- CONTENIDO ----------

if section == "Título":

    st.markdown("""
<div class='title'>
El Tutor de Silicio: ¿Puede la Inteligencia Artificial Entender el Alma del Estudiante?
</div>

<div class='subtitle'>
“En una era de máquinas dirigiendo humanos, ¿aún se necesita a los educadores?”
</div>
""", unsafe_allow_html=True)



elif section == "Introducción":

    st.markdown("<div class='header'>Introducción</div>", unsafe_allow_html=True)

    st.markdown("""
<div class='text'>

Imagínese a un estudiante sentado frente a su ordenador a las dos de la mañana. Frustrado, murmura para sí mismo: "Nunca voy a entender esto, soy un desastre". En ese instante, una pequeña notificación aparece en pantalla. No es un mensaje de un amigo despierto, sino una respuesta de un tutor inteligente que ha detectado ese tono de derrota y ofrece una palabra de aliento precisa para evitar que el desánimo gane la batalla.  

Esta escena, que parece extraída de una novela de Isaac Asimov, es hoy el núcleo de un debate fascinante en la psicología educativa. Ya no vemos a la Inteligencia Artificial (IA) solo como una calculadora sofisticada, sino como un sistema capaz de emular y potenciar nuestras funciones cognitivas más complejas.

</div>
""", unsafe_allow_html=True)



elif section == "Un espejo que aprende a conocernos":

    st.markdown("<div class='header'>Un espejo que aprende a conocernos</div>", unsafe_allow_html=True)

    st.markdown("""
<div class='text'>

En el corazón de esta revolución se encuentra la capacidad de los algoritmos para procesar el "Big Data", esa marea invisible de información que generamos al navegar. Como explican los investigadores Azman y Tümkaya (2025), esta integración no es solo técnica; es una oportunidad para personalizar el aprendizaje. La IA puede identificar patrones de estudio que para un profesor humano, con treinta alumnos a cargo, serían invisibles. Es, en esencia, un sistema que se adapta al ritmo y estilo de cada mente.  

Sin embargo, esta simbiosis entre tecnología y psicología no es sencilla. El paso de una enseñanza estandarizada —donde todos leen la misma página al mismo tiempo— a una personalizada por algoritmos, nos obliga a repensar qué tan autónomo es el estudiante y cuál es el nuevo rol del docente. Como sugieren Al-Zahrani y Alasmari (2024), aunque hay entusiasmo por la innovación, estamos ante una reconfiguración total de la educación, donde la ética debe ser el eje que guíe cada decisión de la máquina.

</div>
""", unsafe_allow_html=True)



elif section == "La frialdad del dato frente al matiz del ensayo":

    st.markdown("<div class='header'>La frialdad del dato frente al matiz del ensayo</div>", unsafe_allow_html=True)

    st.markdown("""
<div class='text'>

¿Podría una máquina calificar tus exámenes mejor que un profesor? La respuesta es un "sí" a medias. Investigaciones recientes de Jukiewicz y Wyrwa (2026) revelan que modelos de lenguaje como ChatGPT son asombrosamente precisos en preguntas cerradas y respuestas cortas, alcanzando niveles de eficacia humanos.  

Pero aquí aparece una grieta. Cuando se trata de evaluar la creatividad o la profundidad crítica de un ensayo universitario, la IA empieza a tartamudear. Jackaria y sus colegas (2024) observaron que, si bien la IA es impecable aplicando reglas rígidas, carece de la "piel" necesaria para captar la ironía, la pasión o la sutileza de un argumento bien construido. La máquina lee el texto, pero el humano lee entre líneas.  

Esta limitación se extiende también al bienestar emocional. Aunque existen tutores inteligentes capaces de responder al "auto-habla negativa" de un alumno para mitigar el desánimo (Thomas et al., 2024), debemos ser cautos. Jukiewicz (2025) advierte que la IA es una excelente herramienta de apoyo, pero no puede —ni debe— sustituir a un psicólogo clínico en situaciones de crisis profunda o riesgos graves de salud mental.

</div>
""", unsafe_allow_html=True)



elif section == "El dilema del algoritmo":

    st.markdown("<div class='header'>El dilema del algoritmo: ¿Aliado o vigilante?</div>", unsafe_allow_html=True)

    st.markdown("""
<div class='text'>

La eficacia de la IA en las aulas está condicionada por un "contrato ético". Según Nguyen y su equipo (2023), existen principios que no podemos negociar: transparencia, privacidad y control humano.  

El desafío más crítico es la privacidad. Bako (2025) advierte que la recolección constante de datos académicos podría convertir la escuela en un entorno de vigilancia si no existen reglas estrictas. Además, existe el riesgo del "sesgo algorítmico": si los datos con los que se entrena a la IA no representan a todos, el sistema podría acabar discriminando a minorías, perpetuando desigualdades que ya creíamos superadas (Eden et al., 2024).

</div>
""", unsafe_allow_html=True)



elif section == "El futuro":

    st.markdown("<div class='header'>El futuro: El toque humano en la era digital</div>", unsafe_allow_html=True)

    st.markdown("""
<div class='text'>

Quizás el mayor temor sea que el exceso de pantallas erosione la conexión empática entre maestro y alumno. La síntesis de las investigaciones actuales apunta hacia un modelo de "IA ética" donde la automatización nunca camina sola. Es lo que los expertos llaman human-in-the-loop: la máquina propone, pero el humano supervisa y decide.  

La integración de la IA no es un destino al que hemos llegado, sino un proceso constante de negociación. El objetivo final no es que las máquinas piensen como nosotros, sino que nos ayuden a pensar mejor, garantizando que el futuro de la educación sea tan inteligente como profundamente humano.

</div>
""", unsafe_allow_html=True)



# ---------- REFERENCIAS ----------
elif section == "Referencias":

    st.markdown("## Referencias")

    references = {

        "Al-Zahrani, A. M. (2024). Unveiling the shadows: Beyond the hype of AI in education. Heliyon, 10(10), e30696.": (
            "https://doi.org/10.1016/j.heliyon.2024.e30696",
            """Adoptando una perspectiva opuesta a las narrativas tecnológicamente optimistas, el estudio saca a la luz las "sombras" o los impactos negativos implícitos de la IA en la educación. Mediante encuestas, corrobora grandes preocupaciones sobre el aislamiento estudiantil, el sesgo de los algoritmos, la pérdida de habilidades de pensamiento crítico y la sobre-dependencia de contenido generado."""
        ),

        "Al-Zahrani, A. M., & Alasmari, T. M. (2024). Exploring the impact of artificial intelligence on higher education: The dynamics of ethical, social, and educational implications. Humanities and Social Sciences Communications, 11(1), 912.": (
            "https://doi.org/10.1057/s41599-024-03432-4",
            """Adoptando una perspectiva opuesta a las narrativas tecnológicamente optimistas, el estudio saca a la luz las "sombras" o los impactos negativos implícitos de la IA en la educación. Mediante encuestas, corrobora grandes preocupaciones sobre el aislamiento estudiantil, el sesgo de los algoritmos, la pérdida de habilidades de pensamiento crítico y la sobre-dependencia de contenido generado."""
        ),

        "Azman, Ö., & Tümkaya, S. (2025). Navigating the ethical landscape of AI integration in education: Balancing innovation and responsibility. F1000Research, 14, 299.": (
            "https://doi.org/10.12688/f1000research.160011.1",
            """El artículo provee un vistazo amplio al impacto de la Inteligencia Artificial en el aprendizaje. Resalta que su capacidad de crear tutorías personalizadas y métricas asertivas es muy prometedora, no obstante, requiere imperativamente de consejos de revisión ética escolares, desarrollo profesional constante para docentes y marcos regulatorios ajustables ante los riesgos de privacidad y manipulación sesgada de las máquinas."""
        ),

        "Bako, N. Z. (2025). Ethical AI in schools: Balancing automation, privacy, and human oversight. World Journal of Advanced Engineering Technology and Sciences, 15(01), 924-934.": (
            "https://doi.org/10.30574/wjaets.2025.15.1.0262",
            """El artículo aborda la tensión entre aprovechar los beneficios analíticos de la IA para instrucción individualizada y la necesidad de mantener a salvo la privacidad de los menores y el criterio humano. Sostiene que una implementación exitosa debe fundirse inexcusablemente con marcos regulatorios sólidos, como GDPR y COPPA, para evitar sesgos sistémicos."""
        ),

        "Eden, C. A., Chisom, O. N., & Adeniyi, I. S. (2024). Integrating AI in education: Opportunities, challenges, and ethical considerations. Magna Scientia Advanced Research and Reviews, 10(02), 006-013.": (
            "https://doi.org/10.30574/msarr.2024.10.2.0039",
            """Esta revisión analiza el panorama general de la IA en la educación, balanceando su potencial transformador para crear entornos inmersivos y automatizar tareas administrativas con los enormes desafíos éticos que representa. Subraya que la IA podría ampliar drásticamente la brecha digital y propagar discriminaciones sociales si no existe una supervisión y diseño conscientes."""
        ),

        "Jackaria, P. M., Hajan, B. H., & Mastul, A. R. H. (2024). A comparative analysis of the rating of college students' essays by ChatGPT versus human raters. International Journal of Learning, Teaching and Educational Research, 23(2), 478-492.": (
            "https://doi.org/10.26803/ijlter.23.2.23",
            """Este estudio comparativo analizó la calificación de ensayos de estudiantes universitarios filipinos realizada por tres profesores humanos y por el modelo ChatGPT 3.5. Encontró que las notas de la IA fueron leve y consistentemente más altas en cuatro rúbricas, pero la relación lineal (concordancia general) entre humanos y máquina resultó pobre, sugiriendo cautela a los docentes."""
        ),

        "Jukiewicz, M. (2025). How generative artificial intelligence transforms teaching and influences student wellbeing in future education. Frontiers in Education, 10, 1594572.": (
            "https://doi.org/10.3389/feduc.2025.1594572",
            """El estudio documenta extensamente el fenómeno de la IA generativa como un factor transformador ambivalente. Si bien optimiza la docencia y democratiza los accesos, la IA también amenaza severamente la integridad académica, promueve el asilamiento social y su uso resulta deficiente e incluso riesgoso en las áreas de salud mental y prevención del suicidio de los estudiantes."""
        ),

        "Jukiewicz, M., & Wyrwa, M. (2026). Can ChatGPT replace the teacher in assessment? A review of research on the use of large language models in grading and providing feedback. Applied Sciences, 16(2), 680.": (
            "https://doi.org/10.3390/app16020680",
            """Al analizar 42 estudios empíricos, esta investigación determina si los modelos de IA generativa logran reemplazar a los maestros evaluando y retroalimentando. Revela que las inteligencias artificiales funcionan excelentemente en cuestionarios cortos o tareas de codificación precisas, pero tambalean ante tareas complejas o altamente subjetivas, recomendando finalmente mantener su función únicamente como sistemas híbridos de soporte."""
        ),
 
        "Nguyen, A., Ngo, H. N., Hong, Y., Dang, B., & Nguyen, B. P. T. (2023). Ethical principles for artificial intelligence in education. Education and Information Technologies, 28, 4221-4241.": (
            "https://doi.org/10.1007/s10639-022-11316-w",
            """Para abordar el debate sobre si existe un consenso mundial sobre ética en la IA, este documento conceptualiza un conjunto unificado de principios éticos para la inteligencia artificial en la educación (AIED). A través del análisis de directrices emitidas por organizaciones internacionales, ofrece directrices prácticas aplicables a la gobernanza, privacidad, explicabilidad y el papel humano."""
        ),

        "Thomas, D. R., Lin, J., Bhushan, S., Abboud, R., Gatz, E., Gupta, S., & Koedinger, K. R. (2024). Learning and AI evaluation of tutors responding to students engaging in negative self-talk. In Proceedings of the Eleventh ACM Conference on Learning @ Scale (pp. 481-485). ACM.": (
            "https://doi.org/10.1145/3657604.3664700",
            """La investigación estudia a tutores interactuando en escenarios online donde los estudiantes expresan frustración personal ("autodiálogo negativo"). Encontraron que las lecciones mejoran significativamente las habilidades del tutor, y posteriormente demostraron que usar el modelo LLM GPT-4 para evaluar automáticamente las respuestas abiertas de los tutores arroja resultados altamente equiparables a la validación humana."""
        )
    }

    for ref in references:
        with st.expander(ref):
            st.write(references[ref][1])
            st.link_button("Ir al artículo", references[ref][0])
