import streamlit as st
import base64

# --- Configuración de la página ---
st.set_page_config(page_title="Mi Portafolio - Sergio Felipe García", layout="wide")

# --- Función para crear etiquetas ---
def create_tag(text, color="#007bff"):
    tag_html = f"<span style='background-color:{color}; color:#ffffff; padding: 4px 8px; border-radius: 12px; font-weight: bold;'>{text}</span>"
    return tag_html

# --- Barra lateral para navegación (el "aside") ---
st.sidebar.title("Sergio Felipe García")
selection = st.sidebar.radio("Ir a", ["Perfil", "Proyectos", "Certificaciones", "Formación Académica"])

# --- Contenido principal ---
# --- Contenido principal ---
if selection == "Perfil":
    st.markdown('<div style="background:linear-gradient(90deg,#0078d4,#40e0d0);padding:1.5rem 2rem;border-radius:1rem 1rem 0 0;margin-bottom:2rem;"><span style="font-size:2.5rem;font-weight:800;color:#fff;">PERFIL PROFESIONAL</span></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])

    with col1:
        # Reemplaza "tu_foto.png" con la ruta a tu foto
        try:
            st.image("PortfolioStreamlit/docs/FotoPerfilSergio.png", width=150)
        except:
            st.info("Reemplaza 'docs/FotoPerfilSergio.png' con la ruta de tu imagen de perfil.")
        
        st.header("Información de Contacto")
          
        st.markdown("""
            - 📧 **Email:** sergio.felipeg2004@gmail.com
            - 📞 **Teléfono:** +34 642 11 25 48
            - 🌐 **LinkedIn:** [linkedin.com/in/sergio-felipe-garcia/](https://www.linkedin.com/in/sergio-felipe-garcia/)
            - 🐙 **GitHub:** [github.com/sergiofgarcia](https://github.com/sergiofgarcia)
            """)

        # Botón de descarga para tu CV en PDF
        try:
            with open("PortfolioStreamlit/docs/SergioFG_CV.pdf", "rb") as pdf_file:
                PDFbyte = pdf_file.read()
            
            st.download_button(
                label="Descargar CV en PDF",
                data=PDFbyte,
                file_name="SergioFG_CV.pdf",
                mime="application/octet-stream"
            )

        except FileNotFoundError:
            st.error("Error: El archivo SergioFG_CV.pdf no se encontró en la carpeta docs.")

    with col2:
        st.title("Sergio Felipe García")
        st.subheader("Desarrollador de Aplicaciones Web (DAW) | Especialista en Microsoft Azure")
        
        st.write("---")

        st.markdown("""
            Me he formado en el desarrollo completo de aplicaciones web, desde el diseño front-end hasta la implementación 
            back-end y la gestión de bases de datos. Con el grado superior de Desarrollo de Aplicaciones Web (DAW) y un certificado oficial de Microsoft en Azure.
        """)

        st.subheader("🛠️ Tecnologías")
        tech_front = f"{create_tag('HTML', '#e34c26')} {create_tag('CSS', '#264de4')} {create_tag('JavaScript', '#f7df1e')} {create_tag('Bootstrap', '#563d7c')} {create_tag('React', '#61dafb')}"
        tech_back = f"{create_tag('Python', '#3776ab')} {create_tag('Java', '#f00')} {create_tag('Node.js', '#68a063')} {create_tag('PHP', '#777bb4')}"
        tech_db = f"{create_tag('MySQL', '#00758f')} {create_tag('MariaDB', '#003545')} {create_tag('PostgreSQL', '#336791')} {create_tag('MongoDB', '#47a248')}"
        st.markdown(f"**Front-end:** {tech_front}", unsafe_allow_html=True)
        st.markdown(f"**Back-end:** {tech_back}", unsafe_allow_html=True)
        st.markdown(f"**Bases de Datos:** {tech_db}", unsafe_allow_html=True)
        
        st.markdown("""
            <div style="background:linear-gradient(90deg,#2563eb,#06b6d4);border-radius:1em;padding:1em 1em;color:#fff; margin-top: 1rem;">
                <b>🎯 OBJETIVO PROFESIONAL</b>
                <p style="margin-top:0.5em;">
                Continuar especializándome en tecnologías cloud en el ecosistema Microsoft, especialmente que tengan 
                componentes de inteligencia artificial, para crear soluciones innovadoras que aporten valor a los negocios
                y mejoren la experiencia del usuario.
                Me gusta aprender continuamente de los demás y estoy motivado por nuevos retos.
                </p>
            </div>
            """, unsafe_allow_html=True)
    
    st.write("---")
    
    # Experiencia Laboral dentro de un expander
    st.header("Experiencia Laboral")
    with st.expander("💼 INETUM - Especialista en Microsoft Power Platform (Abril 24 - Julio 24)", expanded=True):
        st.markdown("""
        * **Desarrollo de Soluciones Web Personalizadas:** Creé aplicaciones web para la gestión de citas y reservas, mejorando la eficiencia operativa y la experiencia del usuario.
        * **Automatización de Procesos:** Implementé flujos de trabajo con Power Automate para automatizar tareas manuales, lo que incrementó la productividad y optimizó los procesos.
        * **Gestión de Bases de Datos:** Diseñé y gestioné bases de datos en Dataverse, asegurando la integridad y accesibilidad de la información para las aplicaciones.
        * **Diseño UX/UI:** Desarrollé landing pages funcionales y atractivas, enfocadas en la conversión y la satisfacción del usuario.
        """)
    

elif selection == "Proyectos":
    st.markdown('<div style="background:linear-gradient(90deg,#0078d4,#40e0d0);padding:1.5rem 2rem;border-radius:1rem 1rem 0 0;margin-bottom:2rem;"><span style="font-size:2.5rem;font-weight:800;color:#fff;">MIS PROYECTOS</span></div>', unsafe_allow_html=True)

    # --- Función para crear y alinear las tarjetas de proyecto ---
    def create_project_card(subheader, description, github_link, image_path, demo_link=None):
        # Lee y codifica la imagen a Base64 para incrustarla en el HTML
        try:
            with open(image_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode()
        except FileNotFoundError:
            st.info(f"No se encontró la imagen en la ruta: {image_path}")
            return

        # Construye los botones de enlace, incluyendo la demo si existe
        buttons_html = f'<p><a href="{github_link}" target="_blank">🔗 Ver en GitHub</a></p>'
        if demo_link:
            buttons_html += f'<p><a href="{demo_link}" target="_blank">🚀 Ver Demo</a></p>'

        # Construye el HTML completo de la tarjeta
        html_card = f"""
        <div style="
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            padding: 1rem;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
            height: 620px; /* Altura fija para la tarjeta */
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            margin-bottom: 20px;
        ">
            <div>
                <h3 style="margin-top:0;">{subheader}</h3>
                <p>{description}</p>
                {buttons_html}
            </div>
            <div style="
                display: flex;
                justify-content: center;
                align-items: flex-end; /* Para asegurar que las imágenes se pegan al final */
            ">
                <img src="data:image/png;base64,{encoded_string}" style="
                    max-width: 100%;
                    max-height: 300px; /* Altura máxima de la imagen */
                    border-radius: 4px;
                ">
            </div>
        </div>
        """
        return st.markdown(html_card, unsafe_allow_html=True)

    # Primera fila de proyectos (2 columnas)
    col1, col2,col3 = st.columns(3)

    with col1:
        description_tienda = f"Este proyecto demuestra mis habilidades en desarrollo **front-end** y mi capacidad para manejar datos dinámicos. La interfaz se conecta a una {create_tag('API', '#28a745')} simulada para obtener información de productos. La maquetación y el diseño responsivo se crearon con {create_tag('HTML', '#e83e8c')}, {create_tag('CSS', '#fd7e14')} y {create_tag('JavaScript', '#6c757d')}."
        create_project_card("🛒 Tienda Online", description_tienda, "https://github.com/SergioFelipeGarcia/Dise-o_Interfaces_Tienda?tab=readme-ov-file", "PortfolioStreamlit/docs/tienda.png", "https://tenda-api-sergio-felipe.netlify.app")

    with col2:
        description_traductor = f"Script de automatización en {create_tag('Python', '#28a745')} que traduce texto de archivos Excel, demostrando mi habilidad para procesar datos con librerías como {create_tag('Pandas', '#6f42c1')} y para integrar {create_tag('APIs', '#dc3545')}. Este proyecto resalta mi capacidad para automatizar tareas repetitivas, mejorando la eficiencia y el manejo de datos."
        create_project_card("⚙️ Traductor de Excel", description_traductor, "https://github.com/SergioFelipeGarcia/Traductor-de-excel-/tree/main", "PortfolioStreamlit/docs/traductor.png","https://traductorexcel.streamlit.app/")
        
    with col3:
         description_whatsapp = f"Aplicación de gestión de plantillas de WhatsApp desarrollada con **{create_tag('Python', '#28a745')}** y **{create_tag('Streamlit', '#6f42c1')}.** Este proyecto facilita la creación, edición y envío de mensajes predefinidos a través de la API de WhatsApp. Es ideal para automatizar comunicaciones y mejorar la eficiencia en campañas de marketing o atención al cliente."
        create_project_card("📱 Gestor de Plantillas de WhatsApp", description_whatsapp, "https://github.com/sergiofgarcia/gestor-whatsapp-templates", "docs/whatsapp_templates.png", "https://plantillawhassapp.streamlit.app/")
    # Segunda fila de proyectos (2 columnas)
    col4, col5 = st.columns(2)

    with col4:
        description_medico = f"Este proyecto es una aplicación **full-stack** que demuestra mi capacidad para construir soluciones robustas con lógica de negocio. Utilicé {create_tag('Java', '#dc3545')} (Servlets) para el back-end, {create_tag('MySQL', '#6f42c1')} para la gestión de datos, y {create_tag('HTML', '#28a745')}, {create_tag('CSS', '#ffc107')} y {create_tag('JavaScript', '#6c757d')} para la interfaz de usuario."
        create_project_card("⚕️ Servicio Médico Telefónico", description_medico, "https://github.com/SergioFelipeGarcia/Servicio-m-dico-telef-nico", "PortfolioStreamlit/docs/servicio_medico.png")

    with col5:
        description_tfg = f"Aplicación de citas médicas desarrollada como TFG, utilizando un enfoque **low-code** con **Microsoft Power Platform**. El proyecto integra {create_tag('Power Apps', '#007bff')} (UI), {create_tag('Dataverse', '#6f42c1')} (BBDD) y {create_tag('Power Automate', '#dc3545')} (automatización). Esta práctica me permitió afianzar mis habilidades en el diseño de bases de datos y la integración de sistemas."
        create_project_card("🏥 Trabajo de Fin de Grado", description_tfg, "https://github.com/SergioFelipeGarcia/TfG", "PortfolioStreamlit/docs/TFG_presentacion.png")

    # Tercera fila de proyectos (2 columnas)
    col6, col7 = st.columns(2)

    with col6:
        description_artes = f"Este proyecto es una práctica completa de **diseño web y desarrollo front-end** que demuestra mi capacidad para crear interfaces dinámicas y conectarlas a servicios de back-end. La aplicación gestiona la autenticación de usuarios y datos de forma dinámica gracias a {create_tag('Firebase', '#ffc107')}. La maquetación y el diseño responsivo se realizaron con {create_tag('HTML', '#e83e8c')}, {create_tag('CSS', '#fd7e14')} y {create_tag('JavaScript', '#6c757d')}."
        create_project_card("🥋 Página de Artes Marciales", description_artes, "https://github.com/SergioFelipeGarcia/Hito-individual-1er-trimestre-Desarrollo-web-cliente", "PortfolioStreamlit/docs/Pagina_artes_marciales2.png")

    with col7:
        description_dietista = f"Aplicación web para gestión de dietas y rutinas, creada como práctica de desarrollo **full-stack**. Demuestra mi experiencia con la lógica de negocio en {create_tag('Java', '#dc3545')}, el diseño de bases de datos con {create_tag('MySQL', '#6f42c1')} y la integración del {create_tag('front-end', '#28a745')} (HTML, CSS, JavaScript). Este proyecto resalta mis habilidades en el desarrollo de aplicaciones para servidor y la gestión del ciclo de vida del software."
        create_project_card("💪 Control de Dieta y Rutina", description_dietista, "https://github.com/SergioFelipeGarcia/Dietista", "PortfolioStreamlit/docs/dietista.png")


elif selection == "Certificaciones":
    st.markdown('<div style="background:linear-gradient(90deg,#0078d4,#40e0d0);padding:1.5rem 2rem;border-radius:1rem 1rem 0 0;margin-bottom:2rem;"><span style="font-size:2.5rem;font-weight:800;color:#fff;">CERTIFICACIONES MICROSOFT</span></div>', unsafe_allow_html=True)
    
    # --- Bloque 1: Primera fila (dos certificados) ---
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            f"""
            <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 1rem; box-shadow: 2px 2px 8px rgba(0,0,0,0.1); height: 500px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <h3 style="margin-top:0;">Certificación AZ-204: Desarrollador de Soluciones para Microsoft Azure</h3>
                    <p>Certificación oficial que valida conocimientos en el desarrollo de aplicaciones y servicios en la nube con Azure. Cubre funciones, contenedores, almacenamiento, seguridad e integración de APIs.</p>
                </div>
                <div style="display: flex; justify-content: center; align-items: flex-end;">
                    <img src="data:image/png;base64,{base64.b64encode(open("PortfolioStreamlit/docs/Certificacion_AZ-204.png", "rb").read()).decode()}" style="max-width: 100%; max-height: 250px; border-radius: 4px;">
                </div>
            </div>
            """, unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 1rem; box-shadow: 2px 2px 8px rgba(0,0,0,0.1); height: 500px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <h3 style="margin-top:0;">Power Apps Certificado</h3>
                    <p>Validación de habilidades en el diseño y desarrollo de aplicaciones personalizadas con Microsoft Power Apps. Destaca mi capacidad para construir soluciones dinámicas que mejoran la productividad.</p>
                </div>
                <div style="display: flex; justify-content: center; align-items: flex-end;">
                    <img src="data:image/png;base64,{base64.b64encode(open("PortfolioStreamlit/docs/Power_Apps_Certificacion.png", "rb").read()).decode()}" style="max-width: 100%; max-height: 250px; border-radius: 4px;">
                </div>
            </div>
            """, unsafe_allow_html=True
        )
    
    st.write("---")
    
    # --- Bloque 2: Segunda fila (dos certificados) ---
    col3, col4 = st.columns(2)

    with col3:
        st.markdown(
            f"""
            <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 1rem; box-shadow: 2px 2px 8px rgba(0,0,0,0.1); height: 500px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <h3 style="margin-top:0;">Certificación PL-900: Power Platform Fundamentals</h3>
                    <p>Validación de conocimientos fundamentales en Power Platform, incluyendo Power Apps, Power Automate y Power BI. Demuestra mi habilidad para crear aplicaciones y automatizar procesos.</p>
                </div>
                <div style="display: flex; justify-content: center; align-items: flex-end;">
                    <img src="data:image/png;base64,{base64.b64encode(open("PortfolioStreamlit/docs/Certificacion_PL_900.png", "rb").read()).decode()}" style="max-width: 100%; max-height: 250px; border-radius: 4px;">
                </div>
            </div>
            """, unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            f"""
            <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 1rem; box-shadow: 2px 2px 8px rgba(0,0,0,0.1); height: 500px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <h3 style="margin-top:0;">Especialista en Azure e Inteligencia Artificial</h3>
                    <p>Formación en programación con Python y C#, y desarrollo de soluciones en Microsoft Azure (certificaciones AZ-900 y AZ-204) e IA (AI-900). Experiencia en la creación de soluciones cloud e inteligencia artificial generativa con Azure OpenAI Service.</p>
                </div>
                <div style="display: flex; justify-content: center; align-items: flex-end;">
                    <img src="data:image/png;base64,{base64.b64encode(open("PortfolioStreamlit/docs/Titulo.png", "rb").read()).decode()}" style="max-width: 100%; max-height: 250px; border-radius: 4px;">
                </div>
            </div>
            """, unsafe_allow_html=True
        )

elif selection == "Formación Académica":

    st.markdown('<div style="background:linear-gradient(90deg,#0078d4,#40e0d0);padding:1.5rem 2rem;border-radius:1rem 1rem 0 0;margin-bottom:2rem;"><span style="font-size:2.5rem;font-weight:800;color:#fff;">FORMACIÓN ACADÉMICA</span></div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### GRADO SUPERIOR EN DAW")
        st.markdown("**Desarrollo de Aplicaciones Web**")
        st.caption("Campus fp | 2022 - 2024")
        st.write("Formación especializada en el desarrollo completo de aplicaciones web, desde el diseño frontend hasta la implementación backend y la gestión de bases de datos.")
       
        st.markdown("#### LOGROS ACADÉMICOS")
        st.markdown("""
        - **Proyecto Final de Grado (TFG):** Desarrollo de una aplicación de citas médicas con Microsoft Power Platform.
                    
        - **Hito Individual 1:** Diseño y desarrollo de una página web de fitness con HTML, CSS y JavaScript.
        """)

    with col2:
        st.markdown("#### COMPETENCIAS CLAVE")
        st.markdown("""
        - **Frontend:** HTML5, CSS3, JavaScript, React  
        - **Backend:** Node.js, PHP, Java  
        - **Bases de Datos:** MySQL, MongoDB, PostgreSQL  
        - **Mobile:** React Native, Responsive Design
        - **Azure:** Fundamentos y desarrollo de soluciones
        - **Power Platform:** Power Apps, Power Automate, Dataverse
        """)
        st.markdown("#### MÓDULOS FORMATIVOS")
        st.markdown("""
        - Programación
        - Bases de Datos
        - Sistemas Informáticos
        - Entornos Desarrollo
        - Interfaces Usuario
        - Desarrollo Web
        """)
        st.markdown("""
        <div style="background:linear-gradient(90deg,#2563eb,#06b6d4);border-radius:1em;padding:1em 1em;color:#fff;">
            <b>HABILIDADES ADQUIRIDAS</b>
            <ul>
                <li>Desarrollo web completo</li>
                <li>Gestión de proyectos</li>
                <li>Trabajo en equipo</li>
                <li>Resolución problemas</li>
            </ul>
        </div>

        """, unsafe_allow_html=True)


